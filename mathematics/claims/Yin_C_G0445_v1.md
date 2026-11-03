---
author: Yin
---
# Complete coupled Gaussian-center loss, fixed-input rates and radical boundaries

The complete original L259 mathematical argument, all24 equations and both exact controls are retained here.
L259 preserves its meaningful exploration, original contribution/freeze/checking history and fixed old review inputs.
No Task/E execution resumes.

## Statement

Let P=sum_(j=0)^d p_j t^j be the ACTUAL monic minimal polynomial of a nonzero algebraic integer alpha, d>=1, m=log M(P)>=0 and W=sum_j p_j^2.
For original iid difference digits mu(0)=1/2,mu(+/-1)=1/4 set

    p_N=Pr(sum_(j=0)^(N-1) eta_j alpha^j=0), p_0=1.

For N<=d, p_N=2^(-N).
For N>d,k=N-d, B_N=[P,tP,...,t^(k-1)P] in ALL N coefficient rows, the exact original law is

    p_N=2^(-N) sum_(h in Z^k:||B_N h||_infinity<=1)
                              exp[-(log2)h^T G_k h], G_k=B_N^T B_N.

Let delta_j be the leading-shift Gram determinant quotients; exp(2m)<=delta_j<=W.
After eliminating the first i coordinates, let S^(i) be the remaining positive Schur matrix and define the actual rational mismatch

    r_i=S^(i)_(i,i+1)/delta_(i+1)-p_(d-1), i>=0.

It depends only on the first i+2 shifts, not on the later quotient length.
For EVERY real x, a_0=log2<=a<=A,

    F_a(x)=sum_(e=-1)^1 exp[-a(e+x)^2], c_a=1+2exp(-a),
    c_a-F_a(x)>=kappa(A)min{x^2,1},
    kappa(A)=min{sqrt(pi/A)exp(-pi^2/a_0),
                         exp(-25A/16)(1-2^(-3/2))}>0.

The unique maximizing shift is0.
For ALL real r,x,y and a_0<=a,b<=A, the complete nine-term coupled sum satisfies

    sum_(e,f in{-1,0,1}) exp[-a(e+r f+x)^2-b(f+y)^2]
       <=c_a c_b-kappa(A)exp(-4A)min{r^2,1}
       <=c_a c_b[1-rho_A(r)],
    rho_A(r)=kappa(A)exp(-4A)min{r^2,1}/4 in[0,1).

For ANY disjoint pair starts I subset{0,...,k-2}, and a common A bounding both relevant(log2)delta pivots at each selected pair,

    p_N<=2^(-N) product_(j=1)^k(1+2^(1-delta_j))
                            product_(i in I)(1-rho_A(r_i)).

One may always take A=(log2)W.
Every original weight and quotient length is retained; each selected pair is charged once, and the bound is uniform over EVERY later integer tail without an independence, bounded-tail or integer-center assumption.
Only the first d coefficient constraints have been removed in this inequality.

For m>0 the actual reversed residuals converge strongly in coefficient l2 to Bcal/exp(-m), using the normalized Blaschke product for ALL expanding roots and allowing unit-circle roots.
Consequently delta_(i+1)->exp(2m) and

    r_i->T(P)=sum_(|alpha_v|>1)(alpha_v-1/conj(alpha_v)),

with every original expanding root/multiplicity included; T(P) is real.
If T(P)!=0, set A_P=(exp(2m)+1)log2 and

    rho_P=kappa(A_P)exp(-4A_P)min{T(P)^2,1}/16>0,
    g(m)=log[2/(1+2^(1-exp(2m)))].

There exists an INPUT-DEPENDENT integer i_0>=0 such that for EVERY N>d,

    p_N<=2^(-d)exp[-(N-d)g(m)]
                   (1-rho_P)^max{0,floor((N-d-i_0)/2)},
    h_2(alpha)>=g(m)-(1/2)log(1-rho_P)>g(m).

No input-uniform onset or method certifying all its future pivots is supplied.
For an actual real one-expanding-place algebraic integer1<beta<2, including Pisot/Salem inputs, T=beta-beta^-1 and one may use A_*=5log2 after its actual onset, giving

    h_2(beta)>=g(log beta)+[kappa(5log2)2^(-20)/32]
                                 min{(beta-beta^-1)^2,1}.

That coefficient is independent of degree, but the correction is only O(m^2), may vanish on varying inputs and does not improve the earlier one-expanding comparison h_2/m->1 near one.

For the actual quartic P=1-t-t^2-t^3+t^4,N6,k2, G2=5I and r0=1.
The complete nine triangularly admissible pairs have

    Z_prod=289/256, Z_tri=9/8+1/512+2^(-24),
    Z_prod-Z_tri=1/512-2^(-24)>0.

Restoring ALL coefficient constraints leaves exactly five pairs and

    Z_full=9/8, p6=9/512, Z_tri-Z_full=1/512+2^(-24).

These distinguish the coupled-center loss from a further lower-row feasibility loss; a finite loss alone is not a rate theorem.
No numerical or J calculation is claimed for this complete symbolic control.

For EVERY monic P=Q(t^r) with integer r>=2 the actual adjacent mismatches are identically zero at ALL times, by exact residue-block Schur separation.
In particular this occurs on the ACTUAL irreducible nontorsion family

    r=2^j>=2, P_r=t^(2r)-t^r-1, alpha_r=phi^(1/r),
    [Q(alpha_r):Q(phi)]=r, M(P_r)=phi=(1+sqrt5)/2.

This fixed-positive-measure nonreciprocal family has T(P_r)=0, rather than a near-one counterexample or zero original growth.
Its actual field-basis/residue decomposition gives, for EVERY N,

    p_N(alpha_r)=product_(a=0)^(r-1) p_(n_a)(phi),
    n_a=#{0<=j<N:j=a mod r}, sum_a n_a=N.

For fixed r, applying the seed bound on each sufficiently long stream retains the complete O(r(1+i_0)) delay and a paired-loss exponent at least N/2-r(3+i_0)/2.
There is NO erroneous division of the limiting chronological improvement by r.
No arbitrary-polynomial independent-stream decomposition, all-input density of useful losses, varying-degree uniform onset, uniform entropy floor or Lehmer gap is established.

<a id="argument"></a>
## Complete argument

### Adequate original-law, Hardy, radical and rate inputs

The complete original Sections1--7/equations1--24 follow without mathematical abridgment.
Their original2026-10-10 pre-adoption and Task-active language remains chronology, not a new authorization to run research or another agent's D127 argument.
The concrete monic quotient bijection, full original constrained Gaussian partition, three-consecutive-point theta truncation, correct leading Schur pivots and full monic Mahler residual bound are already sufficiently proved in [C436](Yin_C_G0436_v1.md#argument), at its Sections4--6 scope.
Its positive Fourier series and convex omitted-tail comparison, including all real shifts and a>=log2, are the precise inputs to the quantitative first-mode estimate here.
The actual source formulas are sufficiently retained in [Nat26 U003](../audits/literature/Nat26/Yin_U003.md#nat26-u003) at the original formula/statement/application depth; this use is local reuse of that accepted interface, not a new external reading occurrence or source-book proof audit.

The entire original [L101](../ledger/Yin_L_G0101_v1.md) closure/strong-limit mechanism is sufficiently retained in [C296](Yin_C_G0296_v1.md#argument), whose Sections1--2 were compared in full.
It factors P*=Bcal O, proves cyclicity of EVERY |c|<=1 factor directly (including tapered boundary-factor inverses with exact(n+1)^(-1/2) error), proves closure of finite products and the closed isometric Blaschke range, then derives strong convergence of nested actual projections to s Bcal.
This supplies the exact affine-slice minimizer and pivot/first-coefficient limits used below, rather than a generic spectral-factor statement or unit-circle invertibility assumption.
Only that actual relation-space mechanism is consumed; no unrelated cubic posterior conclusion is required.

The old L231 input needed here is precisely the ACTUAL radical irreducibility/relative-degree and unobserved chronological return product already adequately proved in [C212](Yin_C_G0212_v1.md#radical-collision-control).
Its square-root tower with rational field norm equal to-1 proves degree2r before using field independence, and then the independent original residue streams give the full product with no1/r loss.
No all-selector weighted-lift or partial-observation theorem from L231 is needed as a new premise.
The complete [C235 greedy/one-expanding comparison](Yin_C_G0235_v1.md#argument), including its accepted parameter-dependent support interface, is only the stronger pre-existing near-one comparison; no BV20/MS25 source proof or broader source claim is added.
For the actual collision-rate limit, [C280's concatenation/subadditivity/Fekete argument](Yin_C_G0280_v1.md#binary-flow-renyi-rate-comparison) applies to every nonzero algebraic integer, including nonunits; it requires no chronological unit quotient or BV20 premise.

<a id="coupled-centers-reuse-and-domain"></a>
### 1. Reuse, original law and the changed question

Date:2026-10-10.
The current Task, rules for reuse/records and Yin's writing policy were read.
No mathematical program or new J is needed for the finite symbolic controls below.

The precise question is whether retaining the discrepancy between an allowed integer triple and its Gaussian center improves the product of independent three-point maxima in [L256](../ledger/Yin_L_G0256_v1.md#triangular-gaussian-collision-fixed-scope).
A local search of the G ledger and source-audit material for shifted Gaussians, three-point sums, Schur centers and lower coefficient constraints located the exact partition and accepted theta-formula interface in L256; [L101](../ledger/Yin_L_G0101_v1.md#endpoint-row-hardy-closure) supplies the actual reversed relation-space closure and strong coefficient limit, including unit-circle roots.
These suffice for the derivation here.
[L255](../ledger/Yin_L_G0255_v1.md#full-covariance-state-cost-fixed-scope) is a related actual-state geometry route, not a proof premise.
[L231](../ledger/Yin_L_G0231_v1.md#golden-fiber-fixed-scope) supplies an actual irreducible radical control and its exact original-law decomposition.
No additional source theorem is used or new literature-priority claim made.
In particular, the theta transformation below is reused at L256's exact accepted Nat26 statement scope; no new source-proof inspection is claimed.

The root coordinator supplied the broad question and separately investigates finite Gram-pivot growth in D127.
Neither that unfinished proof nor any new root derivation is a premise here.
All new two-variable inequalities, their assembly, the center limit application and controls below are by structural_research for Yin.
The present record is author work, not independent review.

Let P(t)=sum_(j=0)^d p_j t^j be the ACTUAL monic minimal polynomial of a nonzero algebraic integer alpha; p_d=1, d>=1.
Set m=log M(P)>=0 and W=sum p_j^2.
The original independent difference digits satisfy

    mu(0)=1/2, mu(+1)=mu(-1)=1/4,
    p_N=Pr(sum_(j=0)^(N-1) eta_j alpha^j=0).

For N>d put k=N-d, B_N=[P,tP,...,t^(k-1)P] in its full N coefficient rows, and G_k=B_N^T B_N.
Monic division identifies every return word uniquely as eta=B_N h, h in Z^k.
Thus, exactly as in L256,

    p_N=2^(-N) sum_(h in Z^k: ||B_N h||_infinity<=1)
                         exp[-(log2) h^T G_k h].        (1)

All original digit weights are present; this is not an auxiliary Gaussian probability law.
If N<=d then p_N=2^(-N).
General algebraic integers are allowed.
No chronological integer quotient kernel or unit-only state-space conclusion is needed below.

For j>=1 write D_j for the Gram determinant of the first j shifts, D_0=1, and delta_j=D_j/D_(j-1).
The existing monic residual argument gives

    exp(2m)<=delta_j<=W.                               (2)

The upper bound is simply the squared norm W of the unprojected shift.
The upper triangular retained digit constraints are

    e_i=h_i+sum_(j=i+1)^(k-1) p_(d+i-j) h_j in{-1,0,1},
       0<=i<k.                                        (3)

Coefficients of P outside0,...,d are zero.
Removing the first d coefficient inequalities enlarges(1), as in L256.
The new estimate does NOT yet restore all those removed inequalities: it retains an additional coupling already inside(3) and the original quadratic energy.
Section5 separately evaluates the removed constraints on an actual control.

<a id="quantitative-three-point-center-loss"></a>
### 2. A uniform three-point deficit away from the correct center

Put a_0=log2.
For a>=a_0 define

    F_a(x)=sum_(e=-1)^1 exp[-a(e+x)^2],
    c_a=1+2 exp(-a).

The sign of x is immaterial.
L256 proves F_a(x)<=c_a for every real x using the accepted Gaussian theta formula and a convex paired-tail subtraction.
We need a quantitative form uniform over a bounded interval.
For A>=a_0 set

    kappa(A)=min{sqrt(pi/A) exp(-pi^2/a_0),
                 exp(-25A/16)(1-2^(-3/2))}>0.          (4)

Then, for a_0<=a<=A and EVERY real x,

    c_a-F_a(x)>=kappa(A) min{x^2,1}.                   (5)

Here is the full bound, including large shifts.
First take |x|<=1/2.
In L256's theta identity all Fourier coefficients are nonnegative, while its omitted paired tail at x is at least the tail at0.
Keeping just the first nonconstant Fourier mode gives

    c_a-F_a(x)
       >=2sqrt(pi/a) exp(-pi^2/a)(1-cos(2pi x))
       >=16sqrt(pi/A) exp(-pi^2/a_0) x^2.              (6)

The last step uses 1-cos(2pi x)>=8x^2 on this interval; for example sin(pi|x|)>=2|x| follows from concavity on[0,pi/2].
There is no sign cancellation among the remaining theta modes.

By evenness it remains to take x>=1/2.
For1/2<=x<=3/4, the triple centered at1 is at least as large as the triple centered at0: replacing its leftmost term by its rightmost term changes the sum by exp[-a(x-2)^2]-exp[-a(x+1)^2]>=0.
Hence F_a(x)<=F_a(x-1), and |x-1| is between1/4 and1/2.
Equation(6) gives deficit at least sqrt(pi/A)exp(-pi^2/a_0).

For3/4<=x<=3/2 that same improvement is at least

    exp[-a(x-2)^2](1-exp[-a(6x-3)])
       >=exp(-25A/16)(1-2^(-3/2)).                   (7)

The improved triple is itself at most c_a, so(7) is a lower bound on c_a-F_a(x).
For x>=3/2 every term of F_a(x) decreases with x, and its value at3/2 is already covered.
Equations(6)--(7), evenness and min{x^2,1}<=1 prove(5).
In particular the unique maximizing shift is x=0.
The constant is deliberately coarse, but explicit and positive; the argument keeps both endpoints of the exponent interval.

<a id="uniform-two-variable-mismatch-loss"></a>
### 3. Two coupled triples lose a uniform factor

For a_0<=a,b<=A, r,x,y real, consider the COMPLETE coupled nine-term sum

    T_(a,b,r)(x,y)=sum_(e,f in{-1,0,1})
                       exp[-a(e+r f+x)^2-b(f+y)^2].

It satisfies

    T_(a,b,r)(x,y)
       <=c_a c_b-kappa(A) exp(-4A) min{r^2,1}
       <=c_a c_b[1-rho_A(r)],
    rho_A(r)=kappa(A) exp(-4A) min{r^2,1}/4.          (8)

Both inequalities are uniform over ALL real x,y, without any distribution or boundedness hypothesis on the later variables that will create those shifts.
For |y|>=1, sum first over e and use(5) on the outer triple:

    T<=c_a F_b(y)<=c_a(c_b-kappa(A)).

Since c_a>=1, this is stronger than the first inequality of(8).
For |y|<=1, at least one of |x+r|,|x-r| is at least |r|.
For that choice f=+1 or-1, the inner deficit in(5) is at least kappa(A)min{r^2,1}, and its outer weight is at least exp(-4A).
The other two inner deficits are nonnegative.
Using F_b(y)<=c_b proves the first inequality.
Finally c_a,c_b<=2, so division by their product gives the second.
Formula(4) gives kappa(A)<1, whence0<=rho_A(r)<1; it is positive precisely when r!=0.

This is not a product of probabilities or independent choices.
It is a pointwise bound on the coupled nine terms.
It will therefore remain valid after summing arbitrary later integer tails.
An exactly centered outer triple cannot simultaneously center all three inner triples when r!=0; that is the mechanism absent from the one-variable maxima.

To identify its actual algebraic parameter, eliminate the first i coordinates of G_k by completing squares, with0<=i<=k-2.
Let S^(i) denote the remaining positive Schur matrix, indexed i,...,k-1.
Put

    r_i=S^(i)_(i,i+1)/delta_(i+1)-p_(d-1).             (9)

The first term is the coefficient of h_(i+1) in the first completed square; the second is the corresponding coefficient in the actual digit constraint(3).
These are rational numbers determined by the first i+2 shifts of P and do not depend on k once k>=i+2.
The complete first two squares have the form

    delta_(i+1)(h_i+u h_(i+1)+linear(later h))^2
    +delta_(i+2)(h_(i+1)+linear(later h))^2.

For any fixed later h, substitute e=e_i, f=e_(i+1) from(3).
The allowed e,f range independently over the nine digit pairs, but their Gaussian energy becomes exactly

    a(e+r_i f+x)^2+b(f+y)^2,
    a=(log2)delta_(i+1), b=(log2)delta_(i+2),           (10)

for real x,y depending on the later h.
No independence of the ENERGY or of the original returned digits is asserted.
The quadratic remainder after these two squares does not depend on e,f.
The remaining constraints in(3) also involve only later h.
This establishes the exact interface for(8).

Consequently, let I be any set of pair starts in{0,...,k-2} with disjoint pairs{i,i+1}.
If a common A bounds (log2)delta_(i+1) and (log2)delta_(i+2) for all i in I, then

    p_N<=2^(-N) product_(j=1)^k(1+2^(1-delta_j))
                         product_(i in I)(1-rho_A(r_i)). (11)

One may always use A=(log2)W.
To prove(11), discard only the first d constraints, then eliminate coordinates in increasing order.
At a selected pair use(8)--(10); at any other coordinate use L256's single-triple estimate.
Both bounds are uniform over every surviving integer tail.
The same Schur complement remains after each eliminated coordinate, so the delta_j and r_i are those in(9), with no reset or duplicated boundary cost.
Finite triangular admissibility contains exactly3^k integer h, so no infinite-series interchange is involved.
This proves the COMPLETE original-law bound with full degree N-d, all original weights and every selected pair charged once.

Formula(11) is stronger than L256 when any selected r_i is nonzero.
A single improved factor is only a finite loss; a rate gain requires linearly many factors.
We establish that next at an explicit fixed-input scope, without asserting a uniform onset.

<a id="actual-center-limit-and-rate-correction"></a>
### 4. Actual center limits and a strictly stronger fixed-input comparison

Let F_i(t) be the monic orthogonal residual of t^i P against P,...,t^(i-1)P in coefficient l2.
Its degree is d+i and squared norm is delta_(i+1).
When forming F_(i+1), only the multiple of F_i can change the coefficient just below the leading term, since all earlier residuals have lower degree.
Its multiplier is S^(i)_(i,i+1)/delta_(i+1).
Therefore

    [t^(d+i)] F_(i+1)=p_(d-1)
                        -S^(i)_(i,i+1)/delta_(i+1)
                     =-r_i.                          (12)

For m>0 reuse L101's actual reversed relation-space limit.
Write P*(z)=z^d P(1/z), E_j=span{P*,zP*,...,z^(j-1)P*}, and let U_j be the orthogonal projection of1 onto E_j in coefficient H2.
With the normalized Blaschke product

    Bcal(z)=product_(|alpha_v|>1)
       (|b_v|/b_v)(b_v-z)/(1-conj(b_v)z),
    b_v=1/alpha_v, s=Bcal(0)=exp(-m)>0,

L101 proves U_j->s Bcal strongly in coefficient l2, including when P has unit-circle roots.
The reversed residual F_i*(z)=z^(d+i)F_i(1/z) is precisely the minimum-norm member of E_(i+1) whose constant coefficient is1.
Indeed reversal preserves norm and sends every permissible monic combination to that affine slice.
For U=U_(i+1), projection orthogonality gives U(0)=||U||^2>0, so this minimizer is U/U(0).
Hence

    F_i* -> Bcal/s in coefficient l2,
    delta_(i+1) -> exp(2m).                           (13)

This reuses an existing strong projection limit; no new finite-degree convergence rate, pivot-growth estimate or D127 input is being asserted.

Taking the first coefficient in(12)--(13) gives the exact limit

    r_i -> T(P):=sum_(|alpha_v|>1)
                         (alpha_v-1/conj(alpha_v)).    (14)

The sum includes every root, with both members of a complex pair, and is real.
To verify the coefficient, logarithmically differentiate each normalized factor at0: its logarithmic derivative is -1/b_v+conj(b_v)=-alpha_v+1/conj(alpha_v).
Thus [z]Bcal/s=-T(P).
This also fixes the sign in(14).
The argument is entirely about the actual polynomial; an arbitrary list of conjugates is not substituted for it.

Assume T(P)!=0.
Set

    A_P=(exp(2m)+1)log2,
    rho_P=kappa(A_P) exp(-4A_P) min{T(P)^2,1}/16>0.    (15)

There is an input-dependent integer i_0 such that for every i>=i_0 the two relevant pivots are at most exp(2m)+1 and |r_i|>=|T(P)|/2.
Choose consecutive disjoint pairs beginning at i_0.
Since min{r_i^2,1}>=min{T(P)^2,1}/4, (11) and delta_j>=exp(2m) give, for EVERY N>d,

    p_N<=2^(-d) exp[-(N-d)g(m)]
          (1-rho_P)^max{0,floor((N-d-i_0)/2)},
    g(m)=log[2/(1+2^(1-exp(2m)))].                    (16)

This bound retains the complete finite boundary/onset cost d+i_0.
The existence of i_0 follows from(13)--(14), but no uniform bound or efficient procedure to certify its all-future condition is claimed.
Finite windows can instead use the explicitly computable rational parameters in(11), without invoking i_0.
Passing to the actual collision entropy rate gives

    h_2(alpha)>=g(m)-(1/2)log(1-rho_P)>g(m).           (17)

This is a strict improvement of THAT general comparison on the stated T(P)!=0 scope.
It is not asserted to improve every existing entropy bound, nor to prove a positive uniform gap.
The quantity in(15) can be extremely small and can vanish along varying inputs.

For a real one-expanding-place input1<beta<2 with every other conjugate of modulus at most1, m=log beta and T(P)=beta-beta^(-1)>0.
This includes the actual Pisot/Salem setting.
Since exp(2m)<4, one may replace A_P by the constant A_*=5log2 after an input-dependent onset.
Define

    rho_beta=kappa(5log2) 2^(-20)
                           min{(beta-beta^(-1))^2,1}/16.

Equations(16)--(17) hold with this rho_beta and its actual onset.
In particular

    h_2(beta)>=g(log beta)
       +[kappa(5log2)2^(-20)/32]
                            min{(beta-beta^(-1))^2,1}. (18)

We used -log(1-x)>=x for0<=x<1.
The displayed coefficient is independent of degree, but the onset need not be, and the added term is only of order m^2 near zero.
The pre-existing [L30](../ledger/Yin_L_G0030_v1.md) comparison h_2/m->1 at this one-expanding-place near-one scope is stronger than the leading coefficient log2 here.
Thus(18) is evidence that true coupled-center loss can accumulate, not a new near-one growth floor or a claim to the best rate.
The original-law, full-multiplicity and time/degree boundaries remain explicit.

<a id="quartic-center-versus-lower-row-control"></a>
### 5. Exact quartic control separates the two sources of loss

Take the actual quartic Salem polynomial P=1-t-t^2-t^3+t^4 and N=6, so k=2.
Its coefficient energy is W=5 and adjacent autocorrelation is0; thus G_2=5I, delta_1=delta_2=5, and r_0=0-p_3=1.
This is an actual mismatch before any limiting argument.

Write h=(u,v).
The last two coefficient constraints are

    v in{-1,0,1}, u-v in{-1,0,1}.

The triangularly retained partition contains exactly nine pairs, with energy5(u^2+v^2).
Its unnormalized value is

    Z_tri=(1+2*2^(-5))
              +2(2^(-5)+2^(-10)+2^(-25))
           =9/8+1/512+2^(-24).                       (19)

For v=0 the values of u are-1,0,1.
For v=1 they are0,1,2, and for v=-1 their negatives; this verifies every term in(19).
The L256 product of separate maxima is

    Z_prod=(1+2^(-4))^2=289/256.

Consequently the exact loss caused by the coupled centers, with the lower rows STILL discarded, is

    Z_prod-Z_tri=1/512-2^(-24)>0.                     (20)

Now restore every coefficient constraint.
The full product vector is

    B_2 h=(u, v-u, -u-v, -u-v, u-v, v).

The first and last coefficients force u,v in{-1,0,1}.
If both are nonzero, either their equal signs violate |-u-v|<=1 or their opposite signs violate |u-v|<=1.
Exactly five pairs remain: (0,0),(+/-1,0),(0,+/-1).
Thus

    Z_full=1+4*2^(-5)=9/8,
    p_6=2^(-6) Z_full=9/512,
    Z_tri-Z_full=1/512+2^(-24).                       (21)

This exact nine-pair calculation keeps all original probabilities and distinguishes a center-coupling loss from an additional lower-row feasibility loss.
Their sum is1/256 before the prefactor2^(-6).
No numerical scan or J52 rerun was used.
The full coefficient list and all nine cases above are the complete symbolic evidence; this is not a claimed general finite-alphabet reduction for longer quotients.
A positive loss at this six-digit window alone would not imply a limiting rate; Section4 provides a separate, correctly charged accumulation argument for the center part.

<a id="actual-radical-adjacent-center-obstruction"></a>
### 6. A genuine nontorsion obstruction to fixed adjacent-center coverage

A nonzero total Mahler measure does NOT force any r_i in(9) to be nonzero.
Suppose P(t)=Q(t^r) for an integer r>=2 and monic Q.
Then p_(d-1)=0.
The Gram entry of two shifted copies is zero unless their shift indices have the same residue modulo r, since their coefficient supports otherwise are disjoint.
Eliminating any initial list of coordinates preserves this residue-block separation: every Schur correction pairs entries through the same residue class.
Thus S^(i)_(i,i+1)=0 and

    r_i=0 for ALL i.                                 (22)

This is an exact all-time obstruction for the SPECIFIED adjacent-pair parameter, not a statement that coupled constraints or actual growth vanish.

It occurs on the actual irreducible nontorsion family from L231:

    r=2^j>=2, P_r(t)=t^(2r)-t^r-1,
    alpha_r=phi^(1/r), phi=(1+sqrt5)/2.

The existing field-norm argument proves actual degree2r and M(P_r)=phi.
All r expanding roots have modulus phi^(1/r), their sum is zero, and their reciprocal-conjugate sum is zero, agreeing with T(P_r)=0.
This family has fixed positive Mahler measure and already known positive original growth.
Neither a near-one family nor a failure of every ordering is exhibited.

Indeed an arithmetic change of ordering repairs this PARTICULAR obstruction without losing a factor r in the chronological rate.
Split both the original digit polynomial and its quotient by exponent residues modulo r.
Multiplication by P_r acts on each stream as multiplication by Q(t)=t^2-t-1.
All original digit weights and integer constraints split as products.
The actual field basis1,alpha_r,...,alpha_r^(r-1) over Q(phi), with relative degree r, also gives the exact return identity

    p_N(alpha_r)=product_(a=0)^(r-1) p_(n_a)(phi),
    n_a=#{0<=j<N:j congruent to a mod r},
    sum_a n_a=N.                                     (23)

This is the retained L231 original-law decomposition at zero disclosure, not an inferred independence after conditioning on a shared endpoint.
Apply(16) to the seed on each stream.
There are at most r separate initial costs and r rounding errors.
For example, once all n_a>2, the paired-loss exponent is at least

    sum_a max{0,floor((n_a-2-i_0)/2)}
       >=N/2-r(3+i_0)/2.                             (24)

The right side may be negative at short times, where the nonnegative left side is used.
Thus for fixed r the asymptotic extra loss is again one half per chronological digit, not one divided by2r; the finite delay is O(r(1+i_0)).
This is a useful exact repair when a true residue decomposition exists.
It gives no general right to reorder arbitrary P into independent streams or a varying-degree uniform onset.
Higher-stride or genuinely coupled multivariate center conditions remain to be identified on general multiple-expanding inputs.

<a id="coupled-center-next-gates-and-scope"></a>
### 7. What this changes, and what remains open

The finite bound(11) preserves a measurable loss discarded by the separate three-point maxima: a rational mismatch in the actual polynomial's Schur center.
It is uniform over the full later integer tail, so the estimate neither selects a typical independent mask nor truncates large quotient states.
Equations(14)--(18) show that the losses truly accumulate for fixed inputs with T(P)!=0, including every actual one-expanding Pisot/Salem input1<beta<2.
The proof does not use a finite-state approximation, the L255 full-core norm, or an uncharged seam.
Its original-law rate transfer is direct from all sufficiently long N with a fully displayed input-dependent onset.

The exact quartic control proves that restoring lower rows can add further loss beyond center coupling, while the genuine radical control proves fixed adjacent coupling can be completely blind on nontorsion inputs.
A changed next test is to retain groups of lower coefficient constraints together with their conditional centers, or identify an algebraically chosen lag/order that gives a quantitative density of losses without charging the same constraint repeatedly.
The relevant uniform obligation is NOT merely that a finite mismatch exists.
It is a time-linear total loss with a useful coefficient and a justified degree/time onset, surviving the full original law on the claimed input class.
The present correction vanishes near one and its onset can vary with the input; no unrestricted Lehmer or affine-growth gap is proved.
All G0001 routes remain active and unresolved.

The accepted L101 strong closure result and L256 theta statement have been used at their actual scopes; no new source intake, imported spectral-factor theorem, numerical evidence, J allocation or other agent's current proof is a dependency.
The exact finite control was checked symbolically from all nine retained pairs, so no machine execution is claimed.
Independent full review is still required before adoption.



### Actual checking and source boundaries

This whole home was checked against the entire original L259 body, R158 and the exact consumed C436/C296/C212/C235/C280 mechanisms, with Nat26's existing formula interface unchanged.
The9 triangular quartic pairs and5 fully admitted pairs were checked symbolically in the complete displayed proof, retaining the prefactor2^-6 and both distinct rational losses.
No mathematical program, J, numerical scan, Gram-pivot producer, other agent's current proof or machine execution is newly claimed.
The general conclusions follow from the all-real-shift inequality, actual strong limit and exact irreducible residue decomposition, not extrapolation of those finite pairs.
Original R158 is known SELF because the brief supplied the claimed outcomes before review; its no-contribution and no-author-repair facts remain unchanged at that relationship.
No external source pages, source proofs or PDF were newly read/acquired, and no existing source unit's date/depth/reader was expanded.

## Current assessment
[Selected decision](#decision-complete-whole-self-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:20 |
| status | open |
| reason | Retain the entire original coupled-center proof and all24 equations, every original-law/nonunit/real-shift/tail/pair/onset/root/degree control and radical blindspot/repair boundary, with adequate existing theta/Hardy/radical/rate mechanisms. No program, new source occurrence/proof or Task/E execution is performed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact full theorem](#statement) | Every actual nonzero algebraic integer, all finite N/real shifts/disjoint pairs/later tails, conditional T(P)!=0 all-root rate and input-dependent onset, one-expanding limit, full9/5 quartic control, every dyadic radical/stream/degree/negative boundary. |
| argument | [Complete proof](#argument) | All original Sections1--7/equations1--24 and exact consumed source/Hardy/monic partition/radical/rate interfaces, every constant/sign/constraint/pair/limit/control/cost step. |
| dependency | [Exact original-law and theta proof](Yin_C_G0436_v1.md#argument) | Sections4--6 only: monic integer quotient/original weights, full constrained partition and retained triples, complete theta/tail maximum, leading Schur conventions and monic Mahler lower pivot. |
| dependency | [Actual Hardy closure and strong projection limit](Yin_C_G0296_v1.md#argument) | Entire Sections1--2 closure/outer-factor cyclicity including circle roots, closed Blaschke range and nested actual strong projection limit; no unrelated cubic posterior premise. |
| dependency | [Actual radical degree and original return product](Yin_C_G0212_v1.md#radical-collision-control) | Actual dyadic golden field-norm(-1) tower/degree2r/relative degree r, full original independent residue product and no1/r rate loss; no partial-observation/weighted-lift theorem. |
| dependency | [Existing stronger one-expanding comparison](Yin_C_G0235_v1.md#argument) | Full actual greedy separation and one-expanding h_2/m->1 comparison with accepted parameter-dependent support boundary only, no new source proof/optimality claim. |
| dependency | [Actual collision-rate existence](Yin_C_G0280_v1.md#binary-flow-renyi-rate-comparison) | Independent concatenation, collision subadditivity and Fekete limit for the original algebraic flow, no unit-only or BV20 assertion. |
| dependency | [Accepted theta formula interface](../audits/literature/Nat26/Yin_U003.md#nat26-u003) | Only exact positive Gaussian Fourier transform and original nome/principal-root conventions at existing statement/formula/application depth, with no new external source occurrence or historical book-proof audit. |

### Decision complete-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:22 |
| status | proved |
| reason | Adopt after the actual whole C445/R649 SELF check of every original Section1--7/equation1--24, the all-real-shift uniform deficit/nine-term inequality, original-law Schur/disjoint-pair elimination, actual Hardy/all-root T(P) limit and fully paid input-specific onset, one-expanding comparison and both complete quartic/radical controls. Adequate C436/C296/C212/C235/C280 and existing Nat26 statement interfaces were actually compared at their consumed scopes; no numerical/J/producer/source-book proof or Task/E execution is performed. Original R158 is known SELF from its pre-supplied claimed outcomes, without changing old whole verdict, no-contribution or no-repair facts. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact full theorem](#statement) | Every actual nonzero algebraic integer, all finite N/real shifts/disjoint pairs/later tails, conditional T(P)!=0 all-root rate and input-dependent onset, one-expanding limit, full9/5 quartic control, every dyadic radical/stream/degree/negative boundary. |
| argument | [Complete proof](#argument) | All original Sections1--7/equations1--24 and exact consumed source/Hardy/monic partition/radical/rate interfaces, every constant/sign/constraint/pair/limit/control/cost step. |
| dependency | [Exact original-law and theta proof](Yin_C_G0436_v1.md#argument) | Sections4--6 only: monic integer quotient/original weights, full constrained partition and retained triples, complete theta/tail maximum, leading Schur conventions and monic Mahler lower pivot. |
| dependency | [Actual Hardy closure and strong projection limit](Yin_C_G0296_v1.md#argument) | Entire Sections1--2 closure/outer-factor cyclicity including circle roots, closed Blaschke range and nested actual strong projection limit; no unrelated cubic posterior premise. |
| dependency | [Actual radical degree and original return product](Yin_C_G0212_v1.md#radical-collision-control) | Actual dyadic golden field-norm(-1) tower/degree2r/relative degree r, full original independent residue product and no1/r rate loss; no partial-observation/weighted-lift theorem. |
| dependency | [Existing stronger one-expanding comparison](Yin_C_G0235_v1.md#argument) | Full actual greedy separation and one-expanding h_2/m->1 comparison with accepted parameter-dependent support boundary only, no new source proof/optimality claim. |
| dependency | [Actual collision-rate existence](Yin_C_G0280_v1.md#binary-flow-renyi-rate-comparison) | Independent concatenation, collision subadditivity and Fekete limit for the original algebraic flow, no unit-only or BV20 assertion. |
| dependency | [Accepted theta formula interface](../audits/literature/Nat26/Yin_U003.md#nat26-u003) | Only exact positive Gaussian Fourier transform and original nome/principal-root conventions at existing statement/formula/application depth, with no new external source occurrence or historical book-proof audit. |
| review | [Actual whole SELF finding](../audits/reviews/Yin_R_G0649_v1.md#coupled-center-whole-self-finding) | Entire statement/argument/all necessary fixed inputs, every original law/real shift/tail/pair/pivot/root/degree/onset/control/source/negative limit; no fresh isolated review claim. |

