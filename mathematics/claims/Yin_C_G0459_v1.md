---
author: Yin
---
# Every-positive-measure higher-lag collision improvement with complete block, onset and radical costs

This home retains the complete original analytic proof, all29equations and its exact finite symbolic control.
L263 retains the meaningful higher-lag exploration, actual contribution/freeze/review history and old fixed inputs; no Task/E execution resumes.

## Statement

Let alpha be ANY actual nonzero algebraic integer with monic minimal P(t)=sum_(j=0)^d p_j t^j in Z[t], p_d=1, d>=1, and positive TOTAL logarithmic Mahler measure m=log M(P)>0.
Nonunits, contracting roots and neutral roots are included.
Under the ORIGINAL independent difference digits mu(0)=1/2,mu(+/-1)=1/4, put

    p_N=Pr(sum_(j=0)^(N-1)eta_j alpha^j=0),
    h2=lim_(N->infinity)-log(p_N)/N,
    g(m)=log[2/(1+2^(1-exp(2m)))], W=sum_j p_j^2.

The existing independent-block collision limit is used; no Gaussian/thinned/conditioned-independent law replaces the original digits.
For N<=d, p_N=2^(-N) exactly.
For N>d, k=N-d, the monic quotient matrix B_N with columns P,...,t^(k-1)P gives the exact full constrained partition1.
Let F_i be the actual monic l2 residual of t^i P, delta_(i+1)=norm(F_i)^2, and define R from t^jP=sum_(i<=j)R_(i,j)F_i.
Put q_l=p_(d-l), U_(i,j)=q_(j-i), e=Uh and T=R U^(-1).
All finite inverses are integral, all previously defined entries remain unchanged when k grows, e ranges over exactly{-1,0,1}^k, and exp(2m)<=delta_j<=W.
Only the FIRST d original coefficient constraints are discarded in the retained finite partition5; the entire quadratic energy and original2^(-N) weights remain.

For a_min=log2, A>=a_min, b>=2, EVERY real unit upper triangular b-by-b C and EVERY outside shift x in R^b, let

    kappa(A)=min{sqrt(pi/A)exp(-pi^2/a_min),
                  exp(-25A/16)(1-2^(-3/2))}>0,
    c_a=1+2exp(-a), Lambda_b(A)=3^b sqrt(2A/exp(1)),
    epsilon(C)=sum_(0<=i<j<b,(i,j)!=(0,b-1))abs(Cij),
    rho_(A,b)(C)=2^(-b)[kappa(A)exp(-4A)min{C_(0,b-1)^2,1}
                           -Lambda_b(A)epsilon(C)]_+.

For EVERY a_j in[log2,A], the complete3^b-term block partition obeys

    sum_(e in{-1,0,1}^b)exp[-sum_j a_j((Ce)_j+x_j)^2]
       <=product_j c_(a_j)*(1-rho_(A,b)(C)),
    0<=rho_(A,b)(C)<1.

The bound is uniform over unbounded real shifts and arbitrary off-diagonal entries.
Its zero-certificate branch uses independent increasing-order elimination, not a reversed positive-part inequality.
For ANY collection I of disjoint consecutive principal blocks C_i of the ACTUAL T, with lengths b_i>=2 and actual exponent bounds A_i,

    p_N<=2^(-N)product_(j=1)^k(1+2^(1-delta_j))
                   *product_(i in I)[1-rho_(A_i,b_i)(C_i)].

All later tails are fixed during each increasing-order elimination, every square/digit/loss is charged once, and no bounded quotient alphabet or independent conditioned-digit model is assumed.
At any specified finite N the rational matrices and explicit constants give this finite bound without an asymptotic onset claim.

Count ALL exterior roots alpha_v, with full multiplicity, by r>=1.
Put s=exp(-m), beta_v=1/alpha_v,

    Bcal(z)=product_(abs(alpha_v)>1)
            (abs(beta_v)/beta_v)(beta_v-z)/(1-conj(beta_v)z),
    F=Bcal/s, F(0)=1.

The ACTUAL reversed residuals F_i* converge strongly in coefficient l2 to F, including unit-circle factors.
For EVERY fixed lag l,

    R_(i,i+l) -> [z^l](P*/F),
    T_(i,i+l) -> tau_l=[z^l](1/F)=[z^l](s/Bcal).

These follow by reversing each FINITE expansion and finite convolution; no infinite-sum limit interchange is assumed.
The reciprocal1/F is only a formal series at zero, also analytic near zero; its interior poles prevent importing F's disk-analytic/l2 budgets.
Writing

    N_+=product_(abs(alpha_v)>1)(1-alpha_v z),
    D_+=product_(abs(alpha_v)>1)(1-z/conj(alpha_v)),
    F=N_+/D_+,

both polynomials have degree r and constant1, but their leading moduli are exp(m) and exp(-m), so they differ.
Consequently there exists a FIRST nonzero lag

    1<=ell<=r<=d, tau_1=...=tau_(ell-1)=0,
    tau=tau_ell=-[z^ell]F!=0.

Thus EVERY actual positive-measure input is covered, even when its adjacent statistic is identically zero.
Set

    b=ell+1<=r+1<=d+1,
    A_P=(exp(2m)+1)log2,
    rho_P=kappa(A_P)exp(-4A_P)min{tau^2,1}/2^(b+3)>0.

There exists an input-dependent integer i0>=0 such that for ALL N>d,

    p_N<=2^(-d)exp[-(N-d)g(m)]
          *(1-rho_P)^max{0,floor((N-d-i0)/b)},
    h2>=g(m)-(1/b)log(1-rho_P)>g(m).

The exact short-length value2^(-N), degree boundary d, unfinished final block and ALL-future quantifier are retained.
The onset follows only from fixed-input coefficient convergence; no effective all-future onset algorithm, uniform rate, useful degree-linear horizon or input-uniform correction is proved.
The first mass abs(tau) can shrink, ell can grow, and the explicit3^b perturbation threshold,2^b factor and density1/b remain charged.
The stronger adjacent constant and one-expanding h2/m->1 comparison remain distinct established results.
Strict improvement over g(m) is not domination of every known comparison or a positive entropy/Mahler floor.

For EVERY r=2^j>=2, the ACTUAL minimal polynomial P_r=t^(2r)-t^r-1 has degree2r by the full norm(-1) square-root tower, alpha_r=phi^(1/r), and m=log phi.
Here F=(1-phi z^r)/(1-phi^(-1)z^r), so ell=r,tau_r=1 and EVERY adjacent T_(i,i+1)=0 at EVERY finite i.
The generic contiguous block still pays b=r+1, whereas the special exact original-law residue product retains its established absence of an asymptotic1/r rate loss only for this family.
At the exact finite length N=3r+1, k=r+1,

    B_N^T B_N=3I, R=I,
    U=I-E_(0,r), T=I+E_(0,r), c=5/4,
    Z_prod=(25/16)c^(r-1),
    Z_tri=(3/2+1/32+2^(-14))c^(r-1),
    Z_full=(3/2)c^(r-1), p_(3r+1)=2^(-(3r+1))Z_full,
    Z_prod-Z_tri=(1/32-2^(-14))c^(r-1)>0,
    Z_tri-Z_full=(1/32+2^(-14))c^(r-1)>0.

All nine triangular endpoint terms and the five FULLY feasible origin/axis endpoint pairs are proved exactly from coefficients(-u,-u-v,u-v,v), with every lower constraint retained in Z_full.
This distinguishes higher-lag center loss from the separately discarded lower-row loss.
The family is nonreciprocal and has fixed positive measure, not a near-one construction.
No program, numerical root approximation, sphere sample or new J artifact is needed.
The theta source interface remains at its existing accepted Nat26 formula depth, Smy08 at its existing measure-one precision scope, with no new source proof/PDF reading.
The coordinator's separate D131 exploration is not a premise; no inverse-series l2 or moment budget is imported from it.
No varying-degree total-loss control, unrestricted gap or Task completion follows.

<a id="argument"></a>
## Complete argument

The entire original Sections1--7/equations1--29 follow, with current adequate hrefs at exactly their already proved scopes.
Original family labels identify the actual fixed inputs; their complete mechanisms, not merely more general conclusions, were compared.

<a id="higher-lag-centers-reuse-and-domain"></a>
### 1. Reuse, original law and the changed conclusion

Date: 2026-10-10.
The original argument introduces no computational experiment.

The needed extension is a uniform loss for a finite block of retained integer digits when the ADJACENT center mismatch vanishes.
A local G-ledger/reuse screen identifies [L259](Yin_C_G0445_v1.md#argument) as the exact adjacent result and failure control, [L256](Yin_C_G0436_v1.md#argument) as the complete original return partition, and [L101](Yin_C_G0296_v1.md#strong-endpoint-coefficient-limit) as the actual reversed residual limit.
These provide a workable mechanism; no further external theorem is needed.
The theta transformation underlying L259 is reused at its already accepted Nat26 statement/formula scope, not independently audited here.
No literature-priority assertion is made.
[L260](Yin_C_G0448_v1.md#argument) separates the unchanged pivot limit from a new coupling loss; its finite determinant estimate is not a premise below.

The coordinator supplied the broad higher-lag question only.
The coordinator's separate unfinished D131 coefficient/moment exploration is not an input and was not read for this proof.
The new finite-block perturbation inequality, coefficient-convolution limit, first-nonzero-lag argument and their assembly below are by structural_research for Yin.
Existing L259/L101 arguments retain their recorded authors and review relationships.

Let P(t)=sum_(j=0)^d p_j t^j be the ACTUAL monic minimal polynomial of a nonzero algebraic integer alpha, with p_d=1 and degree d>=1.
Put

    m=log M(P)>=0, W=sum_(j=0)^d p_j^2.

The original independent difference digits have probabilities mu(0)=1/2 and mu(+1)=mu(-1)=1/4.
Write

    p_N=Pr(sum_(j=0)^(N-1) eta_j alpha^j=0),
    h_2(alpha)=lim_(N->infinity) -log(p_N)/N.

Existence of this original binary collision rate is the retained concatenation/subadditivity interface in L256.
No tilted, independently thinned, or Gaussian probability law replaces mu.

For N>d put k=N-d and let B_N have columns P,tP,...,t^(k-1)P in ALL N coefficient rows.
Monic division identifies every return uniquely with eta=B_N h for h in Z^k.
L256 gives the exact identity

    p_N=2^(-N) sum_(h in Z^k: ||B_N h||_infinity<=1)
                        exp[-(log2)||B_N h||_2^2].       (1)

For N<=d, p_N=2^(-N).
These word-mass identities permit nonunits; no unit-only chronological state kernel is used.

The accepted [Smy08 measure-one/Kronecker interface](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization), including its p.322 irreducible-polynomial precision guard, identifies m>0 here with alpha being nonzero and not a root of unity.
That existing accepted statement is sufficient; its original-source proof is not newly audited.
The result proved below is a strictly positive fixed-input correction to L256's function

    g(m)=log[2/(1+2^(1-exp(2m)))].                      (2)

For EVERY actual input with m>0, some block length b<=d+1 and rho_P>0 give h_2>=g(m)-log(1-rho_P)/b>g(m).
The finite inequality retains d, b and an input-dependent all-future onset.
This removes the T(P)!=0 coverage condition from the adjacent argument; it does not provide a uniform correction, a uniform onset, or a positive Mahler gap.

<a id="true-digit-coordinate-square-matrix"></a>
### 2. The complete triangular energy in actual digit coordinates

For i>=0 let F_i be the monic coefficient-l2 residual of t^i P against P,...,t^(i-1)P.
Its squared norm is delta_(i+1)>0.
Define the infinite upper triangular coefficients R_(i,j) by the finite identities

    t^j P=sum_(i=0)^j R_(i,j) F_i, R_(j,j)=1.

These are the usual Gram--Schmidt expansion coefficients, not an independently chosen matrix.
For the first k columns,

    ||B_N h||_2^2=sum_(i=0)^(k-1) delta_(i+1)
                     (sum_(j=i)^(k-1) R_(i,j)h_j)^2,
    exp(2m)<=delta_j<=W.                              (3)

The pivot bounds and their limit are already proved in L256/L259.
Each entry R_(i,j) is rational and depends on P and j only; extending k does not change it.

Set q_l=p_(d-l) for0<=l<=d and q_l=0 otherwise.
Thus P*(z)=z^d P(1/z)=sum q_l z^l has q_0=1.
Let U be the unit upper triangular matrix U_(i,j)=q_(j-i).
The last k actual coefficient constraints in(1) are exactly

    e=Uh in{-1,0,1}^k.                               (4)

Because U is integral with diagonal1, its finite inverse is integral.
Write `v_l=[z^l](1/P*(z))`; then (U^(-1))_(i,j)=v_(j-i), by finite coefficient convolution.
In particular(4) parametrizes exactly3^k integer h, with no multiplicity or index loss.
Dropping ONLY the first d coefficient inequalities in(1) therefore yields

    p_N<=2^(-N) sum_(e in{-1,0,1}^k)
        exp[-sum_(i=0)^(k-1) a_i
                 (e_i+sum_(j>i) T_(i,j)e_j)^2],
    a_i=(log2)delta_(i+1), T=R U^(-1), T_(i,i)=1.     (5)

All matrices in(5) are their k-by-k principal parts.
Every fixed entry of T agrees as k grows, because its product uses only indices between its row and column.
In particular

    T_(i,i+1)=R_(i,i+1)-p_(d-1),                     (6)

which is precisely L259's adjacent mismatch.
It is T, rather than R by itself, that measures the discrepancy from the allowed INTEGER digit centers.
Formula(5) retains every original probability and the complete quadratic energy.
Its retained digits are summation coordinates, not independent digits under the conditioned original law.

<a id="uniform-finite-block-center-deficit"></a>
### 3. A finite-block loss uniform over all outside tails

Put a_min=log2.
For A>=a_min use L259's explicit constant

    kappa(A)=min{sqrt(pi/A) exp(-pi^2/a_min),
                 exp(-25A/16)(1-2^(-3/2))}>0,
    c_a=1+2exp(-a),
    Lambda_b(A)=3^b sqrt(2A/exp(1)).                 (7)

Here exp(1) is Euler's number, distinguished from the digit vector e.
L259 proves, for a_min<=a,b<=A and ALL real r,x,y,

    sum_(e,f in{-1,0,1}) exp[-a(e+rf+x)^2-b(f+y)^2]
       <=c_a c_b-kappa(A)exp(-4A)min{r^2,1}.         (8)

This is a complete nine-term inequality with unrestricted real shifts.
It includes the large-shift case; no bounded-tail hypothesis is omitted.

Consider a block of b>=2 digits with exponents a_j in[a_min,A], arbitrary real outside shifts x_j, and a unit upper triangular b-by-b real matrix C.
Define its complete partition

    Z_C(x)=sum_(e in{-1,0,1}^b)
         exp[-sum_(j=0)^(b-1) a_j((Ce)_j+x_j)^2].

Let r=C_(0,b-1), and retain as a comparison matrix only that corner entry: C^0=I+r E_(0,b-1).
Write

    epsilon(C)=sum_(0<=i<j<b, (i,j)!=(0,b-1)) |C_(i,j)|,
    eta_A(r)=kappa(A)exp(-4A)min{r^2,1},
    rho_A,b(C)=2^(-b)[eta_A(r)-Lambda_b(A)epsilon(C)]_+,
    [u]_+=max{u,0}.                                  (9)

Then, uniformly over EVERY x in R^b,

    Z_C(x)<=product_(j=0)^(b-1)c_(a_j)
                                  [1-rho_A,b(C)].    (10)

To prove this, the middle b-2 coordinates in C^0 factor as single triples.
Their maxima are c_(a_j); applying(8) to the first and last coordinates gives

    Z_(C^0)(x)
       <=(c_(a_0)c_(a_(b-1))-eta_A(r))
                                  product_(j=1)^(b-2)c_(a_j)
       <=product_j c_(a_j)-eta_A(r).                 (11)

Empty products when b=2 equal1.
Positivity of the first factor in(11) follows from(8), or from eta_A(r)<1<=c_(a_0)c_(a_(b-1)).

For each off-diagonal entry C_(i,j), differentiating an individual exponential summand gives absolute value at most

    2a_i |(Ce)_i+x_i| exp[-a_i((Ce)_i+x_i)^2]
       <=sqrt(2a_i/exp(1))<=sqrt(2A/exp(1)).          (12)

Here |e_j|<=1 and all other Gaussian factors are at most1.
The elementary maximum in(12) occurs at |(Ce)_i+x_i|=1/sqrt(2a_i).
Summing all3^b terms and integrating along the line segment from C^0 to C proves

    |Z_C(x)-Z_(C^0)(x)|<=Lambda_b(A)epsilon(C)         (13)

for unrestricted x and matrix entries.
No compactness of the shift domain or unproved uniform-continuity assertion is used.
If the bracket in(9) is positive, combine(11)--(13) and product c_a<=2^b to get(10).
If it is nonpositive, eliminate digits from first to last using L259's single-triple maximum; this gives Z_C<=product c_a and establishes(10) with rho=0.
Finally0<=rho<1 because kappa(A)<1 and b>=2.

For the ACTUAL matrix T in(5), choose any collection of disjoint consecutive blocks I, with starts i and lengths b_i>=2.
Let C_i be the corresponding principal submatrix of T and choose A_i bounding the actual a_j in that block.
The full finite original-law inequality is

    p_N<=2^(-N) product_(j=1)^k(1+2^(1-delta_j))
                       product_(i in I)[1-rho_(A_i,b_i)(C_i)].
                                                               (14)

Eliminate e in increasing order.
At a chosen block, fix every later e; all its dependence becomes the vector x in(10).
After applying the uniform bound, only the original later squares remain.
At unselected positions use the single-triple maximum.
The outside coordinates need neither a probability law nor a height cutoff.
Blocks are disjoint so no square, digit or loss is charged twice.
At worst A_i=W log2 is available for every block.
All sums have finitely many terms, even though the original integer quotients are not assumed to lie in an input-independent alphabet.

Formula(14) is an effective finite inequality from rational R,U,delta and explicit real constants; a positive bracket in(9) is a sufficient certificate, not a necessary condition for a true block loss.
Larger perturbations or other nonzero entries can still lose mass even if this particular certificate returns zero.

<a id="all-lag-actual-center-limits"></a>
### 4. Actual higher-lag limits from reversed residuals

Assume m>0.
For every expanding root alpha_v, with its full multiplicity, put b_v=1/alpha_v and

    Bcal(z)=product_(|alpha_v|>1)
           (|b_v|/b_v)(b_v-z)/(1-conj(b_v)z),
    s=Bcal(0)=exp(-m)>0, F(z)=Bcal(z)/s.              (15)

Conjugate roots occur together, so F has real coefficients and F(0)=1.
L259 derives from L101 the actual strong residual limit

    F_i*(z):=z^(d+i)F_i(1/z) -> F(z)
                                      in coefficient l2,
    delta_(i+1) -> exp(2m).                           (16)

For clarity about the consumed scope, reversing the affine set of monic combinations of P,...,t^iP gives the elements of span{P*,zP*,...,z^iP*} with constant coefficient1.
If U_(i+1) is the projection of1 onto that space, its least-norm element is U_(i+1)/U_(i+1)(0), and U_(i+1)(0)=||U_(i+1)||^2.
L101 gives U_(i+1)->s Bcal including unit-circle factors.
Division by the limiting nonzero value s^2 gives(16).
This is the already retained interface, with no new convergence rate.

Write f_(i,l)=[z^l]F_i* and f_l=[z^l]F.
Reverse the finite expansion t^jP=sum_(i<=j)R_(i,j)F_i at total degree d+j:

    P*(z)=sum_(a=0)^j R_(j-a,j) z^a F_(j-a)*(z).

For j>=l, taking coefficient l gives the exact identity

    q_l=sum_(a=0)^l R_(j-a,j) f_(j-a,l-a).           (17)

Induction on l now shows that every fixed upper diagonal has a limit

    R_(i,i+l) -> r_l,
    sum_(l>=0) r_l z^l=P*(z)/F(z)                    (18)

as a formal power-series identity.
For l=0 the entries equal1.
For l>0 isolate the term a=l in(17), whose residual coefficient f_(j-l,0) is1.
All other terms converge by the earlier diagonal induction and(16), giving r_l=q_l-sum_(a<l)r_a f_(l-a).
This is exactly the stated convolution and proves existence, not just a putative limit equation.

Since U^(-1) has coefficients `v_l=[z^l](1/P*)`, the finite multiplication in(5) and(18) give

    T_(i,i+l) -> tau_l,
    sum_(l>=0) tau_l z^l=1/F(z)=s/Bcal(z).           (19)

Only finitely many coefficients are used at a fixed l.
The reciprocal in(19) is a formal series at0 (also analytic near0); it is not asserted analytic throughout the unit disk, where Bcal has zeros.
In particular tau_1=T(P) from L259, which checks the sign and the digit-coordinate normalization.

Let r be the number of expanding roots, counted with multiplicity.
It is at least1 and at most d.
The normalization in(15) gives the elementary rational expression

    F(z)=N_+(z)/D_+(z),
    N_+(z)=product_(|alpha_v|>1)(1-alpha_v z),
    D_+(z)=product_(|alpha_v|>1)(1-z/conj(alpha_v)).    (20)

Both polynomials have degree r and constant1.
They cannot be identical: the moduli of their leading coefficients are exp(m) and exp(-m), respectively.
Thus N_+-D_+ is a nonzero polynomial with constant0, and its first nonzero coefficient occurs at some

    1<=ell<=r<=d.

Division by the constant-one denominator and then inversion show

    f_1=...=f_(ell-1)=0, f_ell!=0,
    tau_1=...=tau_(ell-1)=0,
    tau:=tau_ell=-f_ell!=0.                           (21)

This proves finite-lag coverage for EVERY actual m>0 input.
No lower bound on |tau| uniform in m, degree or root configuration is asserted.
No moment estimate or result from D131 has been used.

<a id="all-positive-mahler-block-rate-correction"></a>
### 5. A strictly improved collision comparison for every m>0

Take the first nonzero lag ell from(21), and set

    b=ell+1<=d+1,
    A_P=(exp(2m)+1)log2,
    eta_*=kappa(A_P)exp(-4A_P)min{tau^2,1}/4,
    rho_P=eta_*/(2^(b+1))
         =kappa(A_P)exp(-4A_P)min{tau^2,1}/2^(b+3)>0.
                                                               (22)

For a block beginning at i, let C_i be T on i,...,i+b-1.
Every strict upper entry except its corner has lag less than ell, so(19)--(21) imply epsilon(C_i)->0, while (C_i)_(0,b-1)->tau.
The same holds simultaneously for all the finitely many entries of the block, even though their starting indices are i plus fixed offsets.

It follows that there is an input-dependent integer i_0>=0 such that for ALL i>=i_0,

    (log2)delta_(i+j+1)<=A_P for0<=j<b,
    |T_(i,i+ell)|>=|tau|/2,
    Lambda_b(A_P)epsilon(C_i)<=eta_*/2.               (23)

All exponents remain at least log2 by(3).
The elementary inequality min{x^2,1}>=min{tau^2,1}/4 when |x|>=|tau|/2 shows eta_(A_P)(T_(i,i+ell))>=eta_*.
Hence(9), (22) and(23) give rho_(A_P,b)(C_i)>=rho_P for every such block.

Choose consecutive disjoint blocks beginning at i_0.
For EVERY N>d their number is max{0,floor((N-d-i_0)/b)}.
Formula(14), the lower pivot bound in(3) and(2) imply

    p_N<=2^(-d) exp[-(N-d)g(m)]
                 (1-rho_P)^max{0,floor((N-d-i_0)/b)}.
                                                               (24)

For N<=d the exact value remains2^(-N).
This is an original-law bound for all lengths, not an extrapolation from a selected finite return value.
Its density is1/b, and both the degree boundary d and the onset i_0 are retained.
Taking logarithms, dividing by N and using the existing collision-rate limit gives

    h_2(alpha)>=g(m)-(1/b)log(1-rho_P)>g(m) for m>0.  (25)

For ell=1, L259 has a better constant because no perturbation estimate is needed.
The point of(25) is the absence of the former nonzero-adjacent-sum hypothesis.
The proof is equally valid for nonunits because it uses only the actual original word partition, not an integer state recurrence requiring p_0=+/-1.

The onset in(23) is an existence consequence of a fixed-input strong coefficient limit.
No rate uniform in P, effective all-future onset algorithm, or degree-linear usable horizon has been proved.
At a specified finite N, formula(14) instead uses the actual computable finite matrices and does not depend on(23).
The factor3^b in the sufficient perturbation threshold, the factor2^b in rho_P, and the density1/b are explicit costs of this proof, not constants silently suppressed as input changes.

<a id="exact-nonadjacent-radical-control"></a>
### 6. A true all-adjacent-zero family and its exact finite block

Use the actual irreducible family retained in [L231](Yin_C_G0212_v1.md#radical-collision-control), with its complete original-law interpretation:

    r=2^j>=2, P_r(t)=t^(2r)-t^r-1,
    alpha_r=phi^(1/r), phi=(1+sqrt5)/2,
    d=2r, m=log phi.                                 (26)

The seed t^2-t-1 has field norm-1.
At each successive square-root extension the current root has rational norm-1, which rules out its being a square in its current field; the extension doubles the degree and again has root norm-1.
This recalls the accepted irreducibility proof, so(26) is not a formally padded polynomial.
Its degree and fixed positive Mahler measure are actual.

The expanding roots satisfy alpha_v^r=phi.
Since they all have modulus phi^(1/r), (20) simplifies to

    F(z)=(1-phi z^r)/(1-phi^(-1)z^r),
    1/F(z)=(1-phi^(-1)z^r)/(1-phi z^r).

Thus ell=r and tau_r=phi-phi^(-1)=1, while every lower positive coefficient is zero.
Moreover L259's residue-block argument gives T_(i,i+1)=0 at EVERY finite i, not just in the limit.
The nonadjacent block in(22)--(25) nevertheless has positive gain.
Its generic bound pays b=r+1 and hence tends to zero as r grows even though |tau|=1 and m is fixed.
L259's separate exact residue decomposition is stronger on this special family and removes that asymptotic1/r cost.
It is not silently available for an arbitrary irreducible input.

There is also a completely explicit finite test, requiring no numerical limiting argument.
Take N=3r+1, k=r+1.
The only nonzero coefficients of P_r are at0,r,2r.
Its squared norm is3, its lag-r autocorrelation is

    (-1)(-1)+(-1)(1)=0,

and its other autocorrelations for lags1,...,r-1 vanish by disjoint supports.
Therefore the COMPLETE k-column Gram matrix is3I, R=I, and

    U=I-E_(0,r), T=U^(-1)=I+E_(0,r).                 (27)

The comparison block in Section3 is exact, with corner1 and epsilon=0.
All middle coordinates contribute c=1+2*2^(-3)=5/4.
The complete endpoint pair sum is

    Z_pair=sum_(e,f in{-1,0,1})2^[-3((e+f)^2+f^2)]
          =3/2+1/32+2^(-14).

Indeed f=0 contributes5/4; each of f=+1 and f=-1 contributes1/8+1/64+2^(-15).
These are all nine terms.
The unmodified product, triangular retained sum and FULL constrained sum are respectively

    Z_prod=(25/16)(5/4)^(r-1),
    Z_tri=(3/2+1/32+2^(-14))(5/4)^(r-1),
    Z_full=(3/2)(5/4)^(r-1),
    p_(3r+1)=2^(-(3r+1)) Z_full.                    (28)

To justify the full value, split quotient and product coefficient indices modulo r.
The r-1 singleton quotient streams may take h=-1,0,1, and each contributes5/4.
In the length-two stream, with quotient coordinates u,v, the full seed product is

    (t^2-t-1)(u+vt)=(-u)+(-u-v)t+(u-v)t^2+v t^3.

The first and last constraints force u,v in{-1,0,1}; if both are nonzero then either |u+v|=2 or |u-v|=2.
Exactly the five origin/axis pairs remain, and their Gaussian sum is1+4*2^(-3)=3/2.
This proves every constraint and all original factors in(28), rather than assuming lower rows harmless.

The exact two losses are consequently

    Z_prod-Z_tri=(1/32-2^(-14))(5/4)^(r-1)>0,
    Z_tri-Z_full=(1/32+2^(-14))(5/4)^(r-1)>0.         (29)

This distinguishes the higher-lag center loss from the still-discarded lower coefficient constraints, on genuine inputs where the adjacent certificate is identically blind.
The family is nonreciprocal and has fixed positive measure; it is not claimed as a near-one family or new proof of its previously known positive growth.
Equations(27)--(29) are a complete symbolic finite control, not a computer enumeration and not a claim about every finite block.

<a id="higher-lag-uniformity-and-next-gate"></a>
### 7. Exact limits and the next quantitative gate

The new conclusion is general fixed-input COVERAGE: every actual nonzero algebraic integer with m>0 has a strictly stronger original collision-rate comparison than the unmodified pivot function g(m).
This includes all its expanding, contracting and neutral conjugates, and nonunits at the word-mass scope.
The correction is assembled from actual integer quotient constraints and genuine residuals; an arbitrary prescribed root list, bounded quotient alphabet, independent conditioned-digit model, or finite-modulus relaxation is not substituted for the original problem.

Several boundaries remain essential.
First, the mass of the first usable coupling tau can tend to zero, ell can grow up to the number of expanding roots, and the sufficient perturbation threshold can be exponentially small in b.
Second, fixed-input coefficient convergence supplies no uniform bound on i_0.
Third, the first d original coefficient constraints remain discarded in(5), except in the explicitly evaluated control(28).
Retaining them is a separate possible source of loss; the current theorem does not quantify it in general.
Fourth, a positive strict correction to g(m) need not exceed other established comparisons.
In the one-expanding-place near-one setting, [L30](Yin_C_G0235_v1.md#one-expanding-comparison) still gives the stronger leading comparison h_2/m->1, whereas the adjacent specialization here inherits the small additional term already discussed in L259.

The reciprocal function in(19) must be distinguished from the analytic function F=Bcal/s in(16).
Its poles are inside the disk, so a coefficient-l2 or unit-circle energy identity for F would NOT automatically apply to 1/F.
The coordinator independently emphasized this direct/inverse boundary during this round; no coefficient budget from the separate D131 was used.
The present finite-lag existence proof only compares two degree-r polynomials and then uses finitely many formal coefficients.

A discriminating next question is whether a collection of genuine finite couplings, possibly grouped or ordered differently, can provide a loss whose TOTAL density survives varying degree and m->0 after all perturbation and onset costs.
The radical control already shows that the generic contiguous-block estimate can lose density unnecessarily, while also showing precisely why its special residue repair cannot be assumed in general.
A useful extension must quantify this cumulative gain or couple it to actual lower-row feasibility; merely locating another nonzero finite coefficient would repeat the now-proved coverage step.

No uniform entropy floor, lower Mahler bound, or unrestricted Task completion follows.
The varying-input quantitative gate remains open; present maintenance resumes no Task/E execution.

### Actual whole checking and source limits

The maintaining agent read all L263/R162 and checked every matrix/order/quotient constraint, all two-branch block constants and unrestricted shifts, finite coefficient-limit induction/real multiplicities, first-lag/all-future onset assembly, original factors and complete radical degree/Gram/nine-term/five-pair/lower-row control against the actual C436/C445/C296/C212/C235 mechanisms.
Smy08-U001 was read only as the retained accepted normalization/precision interface; Nat26-U003 is sufficient at its original statement/formula/application depth.
No new source occurrence/proof/PDF, program/native artifact, numerical computation, producer or Task/E execution was introduced.
The original author check was at2026-10-10T01:26.
R162 records shared G0001 history and a review brief but not their exact initial proof-relevant content/order; its prior reviews/necessary fixed inputs alone do not establish proof contribution or isolation.
Its original whole mathematical pass/date/verdict remain, with relationship UNKNOWN at full Sections1--7/equations1--29/source/control scope.
The present actual whole SELF supplies no fresh isolation and closes no historical whole review obligation.

## Current assessment
[Selected decision](#decision-complete-whole-self-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-21T21:18 |
| status | open |
| reason | Retain the complete original every-positive-measure finite-lag theorem and all29 equations, actual original digit constraints/strong residual mechanism, uniform real-tail perturbation with both branches, all-future onset/full degree and density costs, and complete actual radical9/5/lower-row symbolic controls. Existing C436/C445/C296/C212/C235 and accepted Smy08/Nat26 scopes suffice; no new source proof, numerical/native experiment or Task/E execution. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact whole theorem](#statement) | Every actual nonzero algebraic integer with total m>0, all finite lengths/blocks/real tails, actual R/U/T entries and every fixed lag, full first-nonzero-lag coverage/all-future onset/density/constants, complete actual radical and every source/negative limit. |
| argument | [Entire proof](#argument) | Complete original Sections1--7/equations1--29, original monic partition/finite coordinate identity, both block branches, derivative/unbounded shift bound, finite reversal/convolution, full exterior-root argument, all-length assembly and exact9/5 radical/lower-row controls. |
| dependency | [Complete original return partition/pivots](Yin_C_G0436_v1.md#argument) | Actual nonzero-integer/nonunit original word masses and monic quotient/whole Schur energy, all-shift triple maxima, Jensen pivot bounds and existing collision-rate convention; no unit-only state extension. |
| dependency | [Complete adjacent pair/residual/repair proof](Yin_C_G0445_v1.md#argument) | Full all-real-shift9-term pair deficit with exact kappa, actual residual normalization and every-finite adjacent blindspot plus true radical stream repair; no conditional T(P)!=0 restriction is imported into the new coverage conclusion. |
| dependency | [Actual Hardy closure/strong limit](Yin_C_G0296_v1.md#strong-endpoint-coefficient-limit) | Complete Section1 closure/outer-factor cyclicity incl unit-circle roots and Section2 strong nested projection limit, yielding actual normalized residuals; no posterior or inverse l2 budget. |
| dependency | [Actual golden field degree/product law](Yin_C_G0212_v1.md#radical-collision-control) | Entire norm(-1) dyadic tower/degree2r/relative degree r and original independent residue product, no factor1/r or artificial padding. |
| support | [Stronger one-expanding comparison](Yin_C_G0235_v1.md#one-expanding-comparison) | Exact parameter-dependent support/greedy Renyi rate squeeze and conditional small-m h2/m->1, no uniform horizon/new source proof. |
| dependency | [Accepted measure-one precision](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Only existing normalization and p322 irreducible measure-one/Kronecker guard; no new original-source theorem-proof audit or source occurrence. |
| dependency | [Accepted theta formulas](../audits/literature/Nat26/Yin_U003.md#nat26-u003) | Existing Fourier/nome/positive-Gaussian formula scope underlying C445's locally proved bound, no new source passage/PDF or book-proof reading. |

### Decision complete-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T21:21 |
| status | proved |
| reason | Adopt after the actual C459/R664 whole SELF check of all original Sections1--7/equations1--29, actual monic original-law/finite-entry identities, every real-tail block derivative and both positive-part branches, strong residual/fixed finite convolution and first-nonzero actual lag, full all-future onset/boundary/density/perturbation costs and complete symbolic radical9/5/lower-row control. Adequate existing C436/C445/C296/C212/C235 and accepted Smy08/Nat26 mechanisms were compared at their actual scopes; no source-proof/PDF/producer/numerical/Task execution occurred. Original R162 whole UNKNOWN and author09:26 SELF remain, with no fresh isolation, useful uniform onset, total-loss near-one control or gap inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact whole theorem](#statement) | Every actual nonzero algebraic integer with total m>0, all finite lengths/blocks/real tails, actual R/U/T entries and every fixed lag, full first-nonzero-lag coverage/all-future onset/density/constants, complete actual radical and every source/negative limit. |
| argument | [Entire proof](#argument) | Complete original Sections1--7/equations1--29, original monic partition/finite coordinate identity, both block branches, derivative/unbounded shift bound, finite reversal/convolution, full exterior-root argument, all-length assembly and exact9/5 radical/lower-row controls. |
| dependency | [Complete original return partition/pivots](Yin_C_G0436_v1.md#argument) | Actual nonzero-integer/nonunit original word masses and monic quotient/whole Schur energy, all-shift triple maxima, Jensen pivot bounds and existing collision-rate convention; no unit-only state extension. |
| dependency | [Complete adjacent pair/residual/repair proof](Yin_C_G0445_v1.md#argument) | Full all-real-shift9-term pair deficit with exact kappa, actual residual normalization and every-finite adjacent blindspot plus true radical stream repair; no conditional T(P)!=0 restriction is imported into the new coverage conclusion. |
| dependency | [Actual Hardy closure/strong limit](Yin_C_G0296_v1.md#strong-endpoint-coefficient-limit) | Complete Section1 closure/outer-factor cyclicity incl unit-circle roots and Section2 strong nested projection limit, yielding actual normalized residuals; no posterior or inverse l2 budget. |
| dependency | [Actual golden field degree/product law](Yin_C_G0212_v1.md#radical-collision-control) | Entire norm(-1) dyadic tower/degree2r/relative degree r and original independent residue product, no factor1/r or artificial padding. |
| support | [Stronger one-expanding comparison](Yin_C_G0235_v1.md#one-expanding-comparison) | Exact parameter-dependent support/greedy Renyi rate squeeze and conditional small-m h2/m->1, no uniform horizon/new source proof. |
| dependency | [Accepted measure-one precision](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Only existing normalization and p322 irreducible measure-one/Kronecker guard; no new original-source theorem-proof audit or source occurrence. |
| dependency | [Accepted theta formulas](../audits/literature/Nat26/Yin_U003.md#nat26-u003) | Existing Fourier/nome/positive-Gaussian formula scope underlying C445's locally proved bound, no new source passage/PDF or book-proof reading. |
| review | [Actual whole SELF finding](../audits/reviews/Yin_R_G0664_v1.md#higher-lag-whole-self-finding) | ENTIRE exact statement/argument/actual dependencies, every original-law/nonunit/finite-block/real-tail/both-branch/strong-limit/fixed-lag/first-lag/all-N/onset/density/cost case and exact radical9/5/lower-row/source/negative boundary; original R162 whole UNKNOWN remains. |

