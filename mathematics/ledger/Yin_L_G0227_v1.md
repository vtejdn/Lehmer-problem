---
author: Yin
---

# Partial observation fibers and weighted integral lifts

The complete current mathematical home is [C556v2](../claims/Yin_C_G0556_v2.md#statement), adopted at 2026-10-22T19:07 after the [actual current whole SELF](../audits/reviews/Yin_R_G0742_v1.md#current-conditional-golden-whole-self-finding).
The original dated mathematical argument and frozen input below remain the actual input of R126; its original missing relationship declaration is not an explicit unknown or an inferred sharing classification.

Date: 2026-10-10.
The original2026-10-10 coordinating account adopted this restricted result after its separately organized noncontributor review at that original scope.
This is fixed mathematical retention, not Task completion or acceptance of an unrestricted Claim.

<a id="conditional-fiber-fixed-scope"></a>
## Original adopted scope and fixed review input

For the actual parity/carry process, enlarged affine boundary disclosure gives a correctly costed comparison and an exact collision formula over a binary observation kernel weighted by real integer height-one multiples of the minimal polynomial.
Binary rank or local injectivity alone is insufficient: an actual cyclotomic family has increasingly wide injective subcubes and still zero asymptotic information rate.
A nontorsion alpha>2 control gives the exact positive partial-observation rate.
A full finite-time arithmetic weighted-lift deficit is sufficient for a uniform positive collision rate, but that additional deficit is not proved on near-one nontorsion inputs.
All boundary, degree, lag and binomial-tail costs are retained.


<a id="complete-retained-proof-and-review"></a>
## Complete original author proof and dated review input

## Arithmetic endpoint fibers under partial mask disclosure

Date: 2026-10-10.
Starting question: Use L223's valid independent partial-disclosure mechanism to test actual conditional endpoint fibers or a new algebraic constraint coupling the integral recurrence and binary collisions.
Seek a discriminator or stronger actual endpoint information bound beyond proportional rate transfer, keeping degree, chronological time, overlap information and all original probabilities.
Bold conjectures and exact controls may be explored without presuming a uniform entropy floor.



### Reuse and actual setup

The current S2 question and [L223](Yin_L_G0223_v1.md#partial-mask-fixed-scope) retain a valid independent-disclosure experiment, its full-mask reconstruction and its relative collision-information bound.
[L219](Yin_L_G0219_v1.md#parity-carry-exact-endpoint-information) supplies the exact original-law parity/carry identity and at most2d boundary bits.
The [L92 increment identity](Yin_L_G0092_v1.md#binary-increment-js-divergence) and [L93 rank/time obstruction](Yin_L_G0093_v1.md#power-orbit-inverse-time-cost) delimit replacing arithmetic endpoint information by a finite rank count.
This round retains the actual conditional fiber rather than declaring the dependent mask an independent summand selector.
No external theorem or program is used below; the elementary cyclotomic fact needed for a control is proved where used.
These are new local deductions from the displayed original-law model; no originality claim is made.

Let alpha be an algebraic unit with its actual monic minimal polynomial P(t)=sum_(i=0)^d p_i t^i, p_0 in{-1,1}.
All logarithms are natural.
Let xi_j be two-sided independent fair bits, Y_j=sum_i p_i xi_(j-i), sigma_j=Y_j mod2 in{0,1}, and C_j=(Y_j-sigma_j)/2.
The parity output is the COMPLETE original iid fair binary process.
Put S_n=sum_(j=0)^(n-1) sigma_j alpha^j and T_n=sum_(j=0)^(n-1) C_j alpha^j.
The unchanged binary collision probability is p_n=Col(S_n), where Col of a finite probability law means the sum of squared atom masses.

Write ell=min{i>=1:p_i is odd}, w=d-ell, and

    G(t)=P(t) mod2,
    F(t)=t^(-ell)(G(t)+1) in F_2[t].                 (1)

F has constant term1 and degree w, including F=1 when w=0.
The shifted mask is Z_k=sum_(a=0)^w F_a xi_(k-a) mod2.
It is the same Z as L223: a fixed complement and shift identify it with the actual predictable carry mask.
The observation window V_n=(Z_k:-d<=k<=n-1) has n+d iid fair bits.
The independent selector A includes every coordinate of this window with probability theta in[0,1); it is independent of all xi.
K_n(theta) is the average Col(law(T_n|A,V_A)), over both the selector and the actual observed values, exactly as in L223.

For the construction below n>=d, N=n-d and the full boundary vector is

    E=(xi_j:-d-w<=j<=-1 or N<=j<=n-1),
    b=2d+w.                                         (2)

There are exactly b distinct boundary bits; the N remaining input bits xi_0,...,xi_(N-1) are independent of E.
The extra w past bits, beyond L219's boundary, are needed because the earliest Z in V_n uses inputs through -d-w.
They cannot be omitted.
Denote by Q_n(theta) the average conditional collision after ALSO revealing E.
This is a separate auxiliary observation experiment on the same law, not a free change to K_n.

<a id="partial-mask-boundary-linear-fiber"></a>
### 1. The complete linear fiber and its boundary cost

For a fixed selector A, form the binary matrix L_A from the coefficient map

    u=(u_0,...,u_(N-1)) -> (coeff_k(F(t)U(t)):k in A),
    U(t)=sum_(j=0)^(N-1) u_j t^j.                    (3)

Indices of A range over -d,...,n-1.
Rows outside0,...,N+w-1 are zero.
Put r_A=rank_F2 L_A and H_A=ker L_A, of dimension N-r_A.
Conditional on E=e and the observed values, the remaining input vector is uniform on one affine translate of H_A.
This follows by direct linear algebra: Z_A is an affine function of those inputs with constant part determined by e, and every nonempty fiber of a linear map on a fair cube has the same size.
In particular, every pair of independent draws from this conditional input law can be generated by choosing its first point and then independently choosing u uniformly from H_A and flipping the coordinates with u_j=1.

There is an explicit comparison with the original L223 observation:

    K_n(theta)<=Q_n(theta)<=2^b K_n(theta).           (4)

The lower bound is conditional Jensen.
For the upper bound fix A and an observed value v.
Since (E,V_A) is a linear image of finitely many independent fair bits, E conditioned on V_A=v is uniform on an affine set of R elements, where R<=2^b.
If a_(x,e)=Pr(T_n=x,E=e|V_A=v), then the refined collision is R sum_(x,e) a_(x,e)^2, while the unrefined collision is sum_x (sum_e a_(x,e))^2.
The former is at most R times the latter.
Average over v and A.
This argument uses the uniform linear boundary fibers; a generic arbitrary b-bit observation need not satisfy this averaged-collision bound.

For each fixed input, Q_n and K_n have identical lower and upper exponential rates.
With varying inputs the cost b log2/n is explicit, and is additional to L219's endpoint comparison.
Combining(4) with that comparison also gives

    p_n<=2^(2d) Q_n(theta),
    Q_n(theta)<=2^(4d+w) p_n^kappa,
    kappa=(1-theta)/(1+theta).                        (5)

The first inequality uses K_n>=Col(T_n)>=2^(-2d)p_n.
For the second, (4) and L223 give the sharper exponent b+2d*kappa in place of4d+w; the displayed weaker integer-degree charge is convenient and valid because kappa<=1.
Neither estimate assumes a positive original rate.

<a id="exact-mask-kernel-height-one-enumerator"></a>
### 2. Exact collision decomposition into genuine integer relations

For a binary polynomial v of degree<n, define

    R_alpha(v)=Pr{sum_(j:v_j=1) epsilon_j alpha^j=0}, (6)

where the signs epsilon_j are independent fair signs; set R_alpha(0)=1.
The signs here are a device for evaluating a particular exact probability below, not an independent-thinning representation of T_n.

For each fixed A, let Q_n(A) average the collision after observing E and Z_A over their actual values.
Then

    Q_n(A)=2^(-N+r_A) sum_(u in H_A) R_alpha(GU),
    Q_n(theta)=E_A Q_n(A).                           (7)

All multiplication GU and FU in these formulas is in F_2[t].
To prove(7), average the affine-fiber pair construction of Section1 over the first input and all observations.
Its first full input is again the unconditional fair input.
Flipping its internal coordinates u leaves E unchanged, so it leaves the boundary term in S_n+2T_n=B_n unchanged.
The parity output changes by GU, which has degree at most d+N-1=n-1.
Thus equality of the two T_n endpoints is equivalent to

    sum_(j:(GU)_j=1) (2 sigma_j-1) alpha^j=0.

For each fixed u, the entire original sigma process is iid fair.
Averaging the first input therefore gives exactly(6); this independence is used only AFTER the boundary and observation averages, not conditional on their realized values.
The distribution of u is uniform on H_A independently of that first input, since the kernel depends only on A.
This proves(7), including N=0.

The relation probability in(6) has the following exact arithmetic form.
For u in F_2^N let a_P(u) count the integer polynomials H of degree<N such that

    H mod2=U,
    every coefficient of P H lies in{-1,0,1}.        (8)

This is a finite set, because P H then has degree<n and each such product is chosen from at most3^n polynomials; multiplication by P is injective.
Since its parity is GU, its nonzero coefficients have EXACTLY the support of GU.
Monic integer division and minimality of P give

    R_alpha(GU)=a_P(u) 2^(-wt(GU)).                   (9)

Indeed every sign assignment on that support gives a polynomial R with coefficients±1 there and zero elsewhere.
R(alpha)=0 is equivalent to R=P H with H in Z[t], degree<N.
Reducing modulo2 gives G(H mod2)=GU, so cancellation in F_2[t] gives H mod2=U.
Conversely every H in(8) gives exactly one sign assignment.
Here wt denotes number of nonzero binary coefficients.
At u=0, (8) forces PH even and height at most1, hence H=0 and a_P(0)=1.

Equations(7)--(9) separate two obligations which a parity-rank argument would conflate.
H_A is the exact binary observation kernel.
Its contribution to an ACTUAL endpoint collision is the count of genuine bounded-coefficient integer multiples of the actual P, with a specified quotient modulo2 and the correct sign probability.
A vector satisfying binary congruences alone does not give an actual collision.
The count is neither a count of all integer multiples nor an unweighted substitute for the original word law.


<a id="diagonal-disclosure-floor-and-sharp-positive-control"></a>
### 3. The diagonal information ceiling and an exact positive control

The observation matrix has only M=N+w potentially nonzero rows, indexed0,...,N+w-1.
Any subset of its first N rows is independent, since their leading N-by-N matrix is lower triangular with diagonal1.
Consequently, with B_0 the number of selected first N rows and B the number of selected potentially nonzero rows,

    B_0<=r_A<=B,
    E 2^(r_A) lies in[(1+theta)^N,(1+theta)^(N+w)].  (10)

Selected zero rows outside this interval contribute no rank.
The term u=0 in(7) always has probability1.
Therefore

    Q_n(theta)>=[(1+theta)/2]^N,
    K_n(theta)>=2^(-b)[(1+theta)/2]^(n-d).           (11)

For every fixed actual unit, the upper exponential rate of K_n is thus at most log(2/(1+theta)).
This is an information ceiling caused by the same-input diagonal in the surviving affine fiber, with its exact boundary cost.
It is not a positive lower rate.

The ceiling is attained on an actual non-torsion unit.
Take alpha=(3+sqrt5)/2>2, with irreducible minimal polynomial t^2-3t+1; its discriminant5 is not a rational square.
No nonzero polynomial with coefficients in{-1,0,1} vanishes at alpha: a largest term alpha^j has magnitude greater than sum_(i<j)alpha^i, because alpha>2.
Thus R_alpha(GU)=0 for every nonzero u and every n.
Equation(7) is exactly its diagonal term, and(10) gives

    [(1+theta)/2]^N <= Q_n(theta)
       <=(1+theta)^w [(1+theta)/2]^N.               (12)

Together with(4), this proves the ACTUAL partial-disclosure limit

    lim_(n->infinity) -log K_n(theta)/n
        =log(2/(1+theta)).                          (13)

Here d=2, ell=1, w=1 and b=5; no hidden convergence cost is needed.
The original binary endpoints are collision-free, so p_n=2^(-n) and h_2=log2.
Formula(13) is an exact test of the coupled observation law, stronger than merely inserting h_2 into the proportional lower bound from L223.
Its Mahler measure alpha exceeds2, so it supplies neither a near-one test nor a uniform gap.
The same reasoning applies whenever an actual P has no nonzero height-one multiple.

<a id="local-input-flip-integer-obstruction"></a>
### 4. What an input flip must lift integrally

Consider a single internal flip u=t^j,0<=j<N.
Its parity support is t^j G.
A signed polynomial on this support vanishing at alpha, after removing t^j, has degree d and leading coefficient±1.
Minimality and monicity of P force it to equal±P.
Hence

    R_alpha(t^j G)=0   if max_i |p_i|>1;
    R_alpha(t^j G)=2^(1-wt(G))
                       if every p_i lies in{-1,0,1}. (14)

In the second case exactly the two sign assignments P and -P work; every coefficient outside the support is zero.
In the first case the obstruction is deterministic: no input and no sign assignment gives such a one-bit endpoint collision with the boundary held fixed.
This uses the actual integer coefficients, not only their parity.
More generally, (8)--(9) identify the precise required lift for every multi-bit flip.

An important limitation is that deleting all colliding cube edges does not force large endpoint information.
The following actual high-degree family strengthens that warning from one-bit changes to every coordinate cube with no repeated residue class.

<a id="torsion-wide-subcube-injectivity-control"></a>
### 5. An actual family with wide local injectivity and zero total rate

Let r=2^k,k>=0, and let alpha be a primitive (210r)-th root of unity.
Put beta=alpha^r.
Its actual minimal polynomial and that of beta are

    P_r(t)=Phi_210(t^r),   degree P_r=48r,
    P_0(t)=Phi_210(t),     degree P_0=48.             (15)

Here Phi denotes the polynomial whose roots are the primitive roots of the indicated order.
For completeness, these are actual minimal polynomials, not presumed irreducible input relations.
The usual elementary cyclotomic irreducibility argument is short.
The monic polynomials Phi_m have integer coefficients by induction in t^m-1=product_(a|m)Phi_a.
If f is a monic irreducible integer factor containing a primitive root zeta and a prime p not dividing m sends zeta to a root zeta^p in a different irreducible factor g, then f divides g(t^p).
Modulo p, g(t^p)=g(t)^p, so the reductions of f and g have a common irreducible factor.
Their product divides t^m-1, contradicting its squarefreeness modulo p.
Thus every such prime power map preserves the roots of f.
Every exponent coprime to m is a product of primes not dividing m, so f contains all primitive roots.
This proves irreducibility.
For m=210r, a root whose r-th power has exact order210 has exact order210r because r is a power of two and210 contains exactly one factor2.
Thus the roots and degrees in(15) agree; the degree count is phi_Euler(210r)=48r.
Also [Q(alpha):Q(beta)]=r, so1,alpha,...,alpha^(r-1) are independent over Q(beta).

The required coefficient larger than1 is visible without a table or computation.
Inclusion-exclusion in the factorization of t^105-1 gives

    Phi_105(t)=
      (1-t^105)(1-t^7)(1-t^5)(1-t^3)
      /[(1-t^35)(1-t^21)(1-t^15)(1-t)].              (16)

Its coefficients through degree7 are1,1,1,0,0,-1,-1,-2, obtained by dividing1-t^3-t^5-t^7 modulo t^8 by1-t.
Since105 is odd, negating its primitive roots gives Phi_210(t)=Phi_105(-t).
Thus P_0 has coefficient+2 at degree7 and coefficient-1 at degree1.
In particular max|P_0,i|>1, while the filter parameters for P_r are ell=r and w=47r.
The coefficient norm ||P_r||_1 equals ||P_0||_1, independently of r.

**Every subcube using at most one input coordinate in each residue class modulo r is endpoint-injective.** More precisely, take any finite internal index set J subset{0,...,N-1} with distinct residues modulo r, fix every other input bit in the full window used by E,V_n,T_n, and vary the bits of J.
All2^|J| carry endpoints are distinct.
This is true for every choice of the fixed bits and every n>=48r.
In particular a full r-bit consecutive internal window has an exactly uniform endpoint law after all other bits have been fixed, wherever that window is located.

To prove it, take the nonempty difference u between two such inputs.
It has at most one monomial t^(a+r k_a) in each residue class a.
Since G_r(t)=G_0(t^r), the support of G_r U is a disjoint union, by residue class, of translated copies of the support of G_0.
Any signed relation on that support decomposes at alpha as

    sum_(active a) alpha^a beta^(k_a) R_a(beta)=0,  (17)

where each R_a has degree48, coefficient±1 precisely on the support of G_0, and zero elsewhere.
Independence of1,...,alpha^(r-1) over Q(beta) forces every R_a(beta)=0.
Minimality of P_0 would then make R_a=±P_0, contradicting its coefficient+2.
There is no such signed relation.
Equation(7)'s underlying pair identity therefore proves the deterministic injectivity, without making any claim that these subcubes are independent after partial mask observation.
Their size is at most r=degree(P_r)/48, even when the chosen coordinates are widely separated.

Despite this strong local injectivity, every fixed member has ZERO unconditional and partially observed endpoint rate.
Let C_* be the integer ceil((||P_0||_1+1)/2).
Every carry lies in[-C_*,C_*], and alpha has order210r.
Grouping endpoint coefficients by exponent modulo210r gives the support bound

    #support(T_n)<=(2 C_* n+1)^(210r).               (18)

Every conditional law uses this same support, whatever the observation.
Hence both K_n(theta) and Q_n(theta) are at least its reciprocal; their exponential rates are zero for each fixed r.
The original binary endpoint likewise has support at most(n+1)^(210r) and zero rate.
The degree grows with r, and no limit uniform in r is inferred.

There are explicit multi-flip relations bypassing the local obstruction.
Since alpha^(105r)=-1, the genuine height-one polynomial t^(105r)+1 is divisible in Z[t] by P_r.
Let H=(t^(105r)+1)/P_r, of degree57r, and U=H mod2.
It is nonzero: otherwise P_r H would have all coefficients even.
Its support is contained in multiples of r, and has at least two terms; a single term would contradict(14).
For n>=105r+1 the vector U fits the internal interval of length N=n-48r, and G_r U=t^(105r)+1.
The associated sign relation has probability1/2.
For every theta<1 there is positive probability that all coordinates where FU is nonzero are undisclosed, so this is an actual surviving off-diagonal contribution to(7).
No claim of shortest relation or its exact selected rank is made.

This control refutes a uniform accumulation inference from injectivity on all such local input cubes, including arbitrarily large r and arbitrary positions.
It is torsion and therefore does not refute a theorem that uses additional nontorsion near-one arithmetic.
Its purpose is to show exactly which actual global relation data the local test has omitted.

<a id="arithmetic-lift-weight-sufficient-gate"></a>
### 6. A costed arithmetic sufficient condition beyond proportional transfer

Equations(7)--(9) give a concrete sufficient target involving actual relation weights.
Write k_A=N-r_A and

    W_P(A)=sum_(u in H_A) a_P(u) 2^(-wt(GU)).       (19)

Fix0<theta<tau<1 and0<delta<=1.
Suppose the actual input and length n obey the following additional ARITHMETIC hypothesis:

    W_P(A)<=2^((1-delta) k_A)
    for every selector on the M=N+w active rows
    selecting at most tau M of those rows.          (20)

This hypothesis is not proved for nontorsion near-one inputs.
It asks for a quantitative deficit in weighted integral lifts inside the binary kernel, not merely a rank estimate or absence of some short flips.
With it, there is a completely explicit original-law consequence:

    p_n <= 2^(2d) {
       2^(-delta[(1-tau)(n-d)-tau w])
        +exp[-(n-ell) D(tau||theta)] },              (21)

where

    D(tau||theta)=tau log(tau/theta)
             +(1-tau)log((1-tau)/(1-theta))>0.

Indeed the number B of selected active rows is Bin(M,theta).
On B<=tau M, k_A>=N-B>=(1-tau)N-tau w.
By(7) and(20), Q_n(A)<=2^(-delta k_A).
On the exceptional event Q_n(A)<=1.
For any s>0, Markov's inequality and the exact binomial generating function give Pr(B>tau M)<=exp(-s tau M)(1-theta+theta e^s)^M.
Taking e^s=tau(1-theta)/(theta(1-tau)) gives the displayed exp(-M D) bound.
Finally p_n<=2^(2d)Q_n from(5).
This proof works also when the first term in(21) exceeds1; then it is simply uninformative at that finite time.

If(20) held for all sufficiently large n of a fixed input with fixed theta,tau,delta, it would yield

    h_2(alpha)>=min{delta(1-tau)log2,D(tau||theta)}.  (22)

A uniform conclusion across varying inputs would require those three parameters to be fixed independently of input, together with an actual proof of(20) at each input; no such proof is supplied.
At finite time all degree and lag costs remain in(21).
In particular the first prefactor after expanding its exponent is2^(2d+delta(d-tau ell)), and the second carries2^(2d) exp(ell D).
Coefficient height and possible long integer quotients have not disappeared: they are precisely the unresolved counting content of a_P(u) and(20).
An input-dependent positive delta that tends to zero does not solve the common gap.

The positive control in Section3 has W_P(A)=1 and satisfies(20) with delta=1.
The torsion controls in Section5 cannot satisfy a fixed positive-delta instance for all sufficiently large n, because(21) would contradict(18).
This supplies a discriminator for the proposed arithmetic hypothesis rather than presuming it from kernel dimensions.
A next bounded test could track the first genuinely nonlocal PH relation classes in this exact enumerator, or prove a restricted counting deficit after using nontorsion assumptions.
No observation mask is substituted for independent digit selection, and no proportional-rate estimate has been promoted to a new source of growth.

### Contribution and author verification

The coordinating AI supplied the broad continuation question only and no mathematical derivation in this draft.
The assigned structural_research AI developed Sections1--6, including the enlarged boundary, exact binary-kernel/height-one-lift decomposition, the diagonal ceiling and exact positive control, the all-subcube torsion control and the costed sufficient gate.
L219 and L223 are reused at their explicit fixed scopes.
The elementary polynomial, finite-field, probability and cyclotomic arguments needed for the new deductions are included above.
No source-wide audit, new external adoption, program, numerical test or independent review is claimed.

The complete original author SELF account is retained in [R742](../audits/reviews/Yin_R_G0742_v1.md#original-g227-author-self-finding), at its original input and actual date precision.

The changed result is an exact arithmetic interface and two actual controls.
In particular it identifies genuine integer lifting, beyond binary filter rank, as the unresolved content of these conditional endpoint fibers.
That original author verification was not an independently organized proof review or the later adoption.


Author freeze: 2026-10-09T21:55.
The original freeze covers complete Sections1--6, equations(1)--(22), both controls and all contribution/limitation statements subsequently inspected in R126.
No continuing program or J was used.
Only this assigned D was written.
The original author account did not assert independent review, later adoption or Task completion.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0778_v1.md#endpoint-fiber-complete-independent-review), with its original inspected scope and relationship.
