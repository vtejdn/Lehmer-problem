---
author: Yin
---
# Fixed-trace moving-exponent Salem inputs and the raw relation-Gram obstruction

The complete current theorem and all necessary source/Gram/deflation/original-window proofs belong to [C494](../claims/Yin_C_G0494_v1.md#statement), adopted with [R706 current whole SELF](../audits/reviews/Yin_R_G0706_v1.md#complete-moving-exponent-whole-self-finding).
The complete original account below remains the fixed input of R547 and preserves its actual source occurrences, contributions, feasibility limitations and earlier unresolved checkpoint.
The later [C171 theorem](../claims/Yin_C_G0171_v1.md#two-block-torus-statement) separately settles coherence divergence for this same bounded-positive-measure family; that result is not inferred from the raw-Gram obstruction here.
Original R547 direct fixed-proof and source arrangements retain their actual scope/date; this maintenance supplies no extra old isolation event, new source inspection or Task/E resumption.

Date: 2026-10-18T13:55.
Human author Yin.
Root assigned one bounded source-feasibility inquiry after the constant-SPD review, with no numerical program, Gram scan or parameter evaluation.
The entropy_attainment_bridge AI authors the explicit schedule and symbolic feasibility deductions in this draft.
Root supplied the source direction and requested the fixed-seed and actual-original-degree boundaries; no independent review is claimed.

<a id="fixed-trace-moving-exponent-source"></a>
## Exact source scope and inspected passages

The existing [RY26-U001](../audits/literature/RY26/Yin_U001.md#ry26-u001) owns the inspected source formulas and their direct exterior-root expense.
This inquiry rereads the retained arXiv2608.00778v1 PDF, printed/PDF pages23--25, including the individual construction, Proposition7.1, its use in Theorem1.3 and the first counting-lemma passages, and visually checks page23.
Equation(7.2), the distinction between arbitrary admissible distinct-prime exponent choices and all sufficiently large degrees, and the exact removal2(x-1)^n are the relevant source interfaces.
The n>=10^4 hypothesis belongs to Proposition7.1's representation of EVERY sufficiently large odd integer by n primes and the resulting all-even-degrees Theorem1.3.
It is not asserted as a condition on the preceding individual interlacing construction.
No audit of the full Vinogradov/counting proof or the global Theorem1.3 is performed.

The fixed [MS05 construction source unit](../audits/literature/MS05/Yin_U001.md#ms05-u001) binds arXiv:math/0308213v2,31March2004, rather than the numbered journal edition cited by RY26.
Its corresponding construction is Lemma12 on printed/PDF pages9--10, not a local Lemma6.1.
This inquiry reads that complete proof, its Lemmas10--11 and Corollary9 on pages8--9, and the relevant interlacing inputs in Section3.
The displayed torsion-coset classification proof in Lemma10 and the prime-selection part of Lemma12 are checked directly.
The general torsion-coset exponent theorem and its Mann/Schmidt source inputs are consumed as source statements, not newly proof-audited here.
No proof-equivalence claim with the published edition is needed.

The source proof only uses that the killer exponent is even, kills every constant-x maximal torsion coset, and is pairwise coprime to the other exponents, which themselves are distinct primes not dividing it.
Being the SMALLEST such primes is used for a numerical degree upper bound, not for irreducibility or removal of cyclotomic factors.
The complete [arbitrary-distinct-prime source interface](../audits/literature/MS05/Yin_U001.md#ms05-arbitrary-distinct-prime-construction) now retains this applicability check without relying solely on RY26's word 'suggests'.

<a id="fixed-trace-moving-exponent-schedule"></a>
## One explicit schedule, with all original factors retained

Fix RY26's odd n=3, so there are four exponents and the prescribed trace is-1.
Let

    K=(product_(p prime,p<=48) p)
        lcm(1,...,ceil(8^5*5^(5/2))).

This is exactly equation(7.2) at n=3, and also the inspected [MS05 four-exponent killer specialization](../audits/literature/MS05/Yin_U001.md#ms05-four-exponent-specialization).
It is an even common killer exponent; using a common multiple of the source's minimal killer exponent preserves its torsion-coset property.
No large integer is expanded or numerically evaluated in this inquiry.
For each integer j>=1 choose

    a_j = the least prime greater than (j+1)K,
    b_j = the least prime greater than (K+a_j+3)^2,
    c_j = the least prime greater than (K+a_j+b_j+3)^2.

Existence follows from the elementary infinitude of primes; no prime gap estimate, prescribed-prime-tuple conjecture or three-primes representation theorem is invoked.
All three primes exceed K, are distinct, are coprime to K, and all tend to infinity.
The displayed square separations deliberately make every successive moving scale much larger than the preceding ones.
This is an explicit mathematical selection rule, not a prime enumeration run.

Put ell=(K,a_j,b_j,c_j) and define

    H_j(x)=2(x^2-1)product_(i=0)^3(x^ell_i-1)
             -x sum_(q=0)^3 (x^ell_q+1)product_(i!=q)(x^ell_i-1),
    N_j=H_j/2,
    P_j=N_j/(x-1)^3.

The inspected MS05/RY26 construction gives P_j in Z[x] monic irreducible, the actual minimal polynomial of a Salem number tau_j, and no further cyclotomic factor.
In detail, pairwise coprimality means that two coordinates equal to1 at a torsion specialization force x=1.
Otherwise the source torsion-coset classification forces x^K=1, producing one coordinate equal to1, while its displayed h equation forbids exactly one such coordinate.
Thus x=1 is the only possible root of unity.
At x=1 each summand in the second part has order3, its leading coefficient is a positive multiple of product ell_i times sum1/ell_i, and the first part has higher order.
Hence the exact root multiplicity is3.
The four-term parity gives H_j integral with every coefficient even, and the source interlacing proposition then leaves exactly one irreducible Salem factor.
The reciprocal-Pisot alternative in that proposition has degree two and is excluded by the actual degree d_j>2 below.
These deductions retain the source theorem's status; they do not upgrade its complete original proof audit.

The exact degrees and source trace are

    D_j=deg N_j=K+a_j+b_j+c_j+2,
    d_j=deg P_j=D_j-3=K+a_j+b_j+c_j-1,
    trace(tau_j)=-1.

The degree d_j is even because K is even and the three primes are odd.
Every projection below uses the ORIGINAL minimal polynomial P_j and window2d_j.
The factor(x-1)^3 is the complete cyclotomic correction; D_j is not substituted for d_j.
The elementary exterior-root computation already retained in RY26-U001 gives

    2<tau_j<4,
    log2<m(P_j)=log tau_j<log4.

This is a bounded-total-measure, unbounded-degree family with all three moving exponents, but is uniformly separated from the near-one regime.
It supplies no original Mahler-gap evidence and no coherence conclusion merely from its trace.

<a id="moving-exponent-raw-numerator"></a>
## Sparse multiscale numerator and the fixed-seed distinction

For q=0,1,2,3,4 write F_q(x)=x^2+(2-q)x-1.
Expanding the four products, a subset S of the four exponents contributes

    (-1)^abs(S) x^(sum_(i in S)ell_i) F_(abs(S))(x)

to N_j.
Pairing the subsets that differ only by K yields

    N_j(x)=sum_(S subset {a_j,b_j,c_j})
       x^(sum_(u in S)u) C_(abs(S))(x),
    C_q(x)=(-1)^q [F_q(x)-x^K F_(q+1)(x)], q=0,1,2,3.

Each C_q is a fixed nonzero polynomial of degree K+2 and nonzero constant coefficient.
The selected separation makes these eight coefficient blocks disjoint, with gaps tending to infinity between the moving scales.
In particular the nonzero coefficient at exponent a_j lies arbitrarily far from BOTH endpoints0,D_j.
Therefore N_j cannot be represented along this sequence as x^(r_j)f(x)+g(x) for two fixed univariate polynomials f,g: such a representation has all nonzero coefficients within fixed endpoint blocks once r_j tends to infinity.
Holding all but one exponent fixed would instead admit exactly that two-block decomposition and is deliberately not the selected schedule.
This proves the stated fixed-numerator distinction, not an assertion that no more general fixed multivariate template or alternate auxiliary representation exists.

The raw numerator still has at most48 terms and coefficient-l1 norm at most64, by its exact product expansion.
These upper bounds are independent of j, although its gaps and original degree grow.
They concern N_j=P_j(x-1)^3, not the generally dense irreducible P_j.
No trace coefficient or growth of P_j's raw coefficients is interpreted as projection coherence.

<a id="moving-exponent-gram-feasibility"></a>
## The actual remaining kernel question

The next section records the direct obstruction to transferring C160's UNIFORM RAW GRAM lower bound to this particular multiscale numerator.
The intended original projection and the bounded cyclotomic correction are unchanged.
No finite coefficient matrix is instantiated or numerically evaluated.

### An explicit vanishing Rayleigh quotient in the required window

Separate the final moving exponent by writing

    N_j(x)=A_j(x)+x^(c_j)B_j(x),
    L_j=K+a_j+b_j+2.

Both A_j and B_j are integral polynomials of degree at most L_j, with disjoint support after the indicated shift because c_j>L_j.
To see their values at1 directly, put

    R_j=(x^K-1)(x^(a_j)-1)(x^(b_j)-1),
    S_j=sum_(u in {K,a_j,b_j})(x^u+1)
                              product_(v in {K,a_j,b_j},v!=u)(x^v-1).

Then exact expansion gives

    A_j=-(x^2-1)R_j-(x/2)R_j+(x/2)S_j,
    B_j= (x^2-1)R_j-(x/2)R_j-(x/2)S_j.

The halves yield integral coefficients because S_j and R_j agree modulo2.
Here R_j has order3 at1 and S_j has order2 there, so BOTH A_j and B_j are divisible by(x-1)^2.
In particular A_j(1)=B_j(1)=0.
The earlier l1 estimate and disjoint blocks give

    ||A_j||_1+||B_j||_1=||N_j||_1<=64.

In the actual window M_j=2d_j, the full N_j relation matrix has

    r_j=M_j-D_j=d_j-3=D_j-6=K+a_j+b_j+c_j-4

columns, corresponding to N_j,xN_j,...,x^(r_j-1)N_j.
Call it T_j and set G_j=T_j^tT_j; this G_j is a coefficient Gram, not the trace-defect function G.
All columns and products fit exactly in degrees0,...,2d_j-1.
The matrix is positive definite because the shifts have distinct leading degrees.

Use the coefficient vector of

    X_j(x)=1+x+...+x^(r_j-1),       ||X_j||_2^2=r_j.

Since A_j(1)=B_j(1)=0, the polynomials

    U_j=A_j/(1-x),      V_j=B_j/(1-x)

are integral and have degree at most L_j-1.
Each coefficient is a partial sum of coefficients of A_j or B_j, respectively.
Therefore

    ||U_j||_2+||V_j||_2
       <=sqrt(L_j)(||A_j||_1+||B_j||_1)
       <=64sqrt(L_j).

There is no condition-number assumption in this elementary coefficient bound.
Exact multiplication and the triangle inequality now give

    N_j X_j=(1-x^(r_j))(U_j+x^(c_j)V_j),
    ||N_j X_j||_2<=2(||U_j||_2+||V_j||_2)
                   <=128sqrt(L_j),
    lambda_min(G_j)<=||N_jX_j||_2^2/||X_j||_2^2
                     <=16384 L_j/r_j.                (G1)

By the selected schedule c_j>(L_j+1)^2 and r_j>c_j, while L_j tends to infinity.
Thus the right side tends to zero.
The exact uniform RAW relation-Gram coercivity used in [C160](../claims/Yin_C_G0160_v1.md#fixed-seed-gram-coercivity) fails for this selected family, despite its bounded total Mahler measure, fixed raw term count, bounded raw l1 norm and bounded removed cyclotomic degree.
No eigenvalue has been numerically computed.

### Removing the fixed cyclotomic zeros loses the raw coefficient bound

This failure cannot be repaired within the four canonical integer numerators simply by partially removing the factor(x-1)^3 while retaining a uniform raw l1 bound.
Write

    W_j=K a_j+K b_j+a_j b_j.

The displayed R_j,S_j formulas show that the order-two coefficients of A_j and B_j at1 are respectively W_j and-W_j.
Consequently

    [A_j/(x-1)^2](1)=W_j,
    [B_j/(x-1)^2](1)=-W_j.

The shifted blocks remain disjoint after division by(x-1) or(x-1)^2, so

    ||N_j/(x-1)^2||_1>=2W_j -> infinity.             (G2)

For U=A_j/(x-1), one has U(1)=0 and U'(1)=W_j.
The elementary bound abs(U'(1))<=deg(U)||U||_1 and its B_j counterpart give

    ||N_j/(x-1)||_1>=2W_j/(L_j-1)>a_j -> infinity.  (G3)

The final strict inequality uses W_j>=a_j b_j and L_j-1=K+a_j+b_j+1<2b_j, which follows from the selected square separation.
For full removal, the order-three coefficient of N_j at1 is minus the sum of the four triple products, giving

    P_j(1)=-(a_j b_j c_j+K b_j c_j
                       +K a_j c_j+K a_j b_j),
    ||P_j||_1>=abs(P_j(1)) -> infinity.             (G4)

These are exact integer-coefficient deductions, not evaluations of chosen parameter values.
They do not bound the normalized coefficients of a different rational auxiliary or the actual projection kernel.
They show only that the direct C160 package of BOTH a uniformly bounded raw coefficient norm and a uniform short-Gram lower bound is unavailable for every member of the natural list

    P_j, (x-1)P_j, (x-1)^2P_j, (x-1)^3P_j.

No argument here rules out another annihilator, a scaled-preconditioned proof, cancellation in the exact projection or an estimate using the full small-eigenvalue geometry.

### Original projection, paid cyclotomic rank and actual stopping point

Let R_N be the residual projection for the r_j N_j relations in the SAME2d_j coordinate window, and let R_P be the actual C158 projection for all d_j P_j relations.
Their relation spaces are nested and their dimensions differ by exactly3.
Thus R_N-R_P is an orthogonal projection of rank3.
The already proved finite positive-semidefinite diagonal-sum inequality from [C160](../claims/Yin_C_G0160_v1.md#fixed-seed-original-factor-projection) gives

    abs(kappa_(2d_j)(R_N)-kappa_(2d_j)(P_j))<6.

This comparison keeps the original d_j normalization on both terms.
It makes the bounded-rank cyclotomic correction harmless for a possible future boundedness/divergence result, but supplies no such result itself.
The uncontrolled small-eigenvalue directions in G_j may cancel after multiplication by the relation matrix in T_j G_j^(-1) T_j^t.
Therefore(G1) does NOT imply kappa divergence, just as(G2)--(G4) do not imply it from P_j coefficient growth.

The exact sparse offsets are nevertheless explicit: N_j is the eight-block polynomial displayed above, so its autocorrelation offsets have the form

    e_0+e_1 a_j+e_2 b_j+e_3 c_j,
    abs(e_0)<=K+2,       e_1,e_2,e_3 in{-1,0,1}.

A product of h matrices with that support reaches at most

    (2h(K+2)+1)(2h+1)^3

distinct offsets, even when different tuples coincide or boundary truncation removes positions.
Hence the finite support geometry is tractable symbolically; it is uniform spectral contraction, not an uncounted graph-volume cost, that blocks C160's inverse-series proof here.
An actual future question would have to control the projection after compensating for these degenerating directions, rather than assume the failed uniform lower bound.
No such compensation theorem is supplied in this bounded step.

The n>=10001 scale is avoidable for this ONE sequence, but the explicit killer exponent is not small even at n=3.
Already its prime-product factor exceeds10^13: the factors2,3,5,7 have product210 and the eleven remaining primes from11 through47 are all greater than10.
The lcm factor is additional.
Thus even this reduced-n source input is unsuitable for a literal original-window Gram experiment, quite apart from the increasingly separated prime scales.
No small substitute for K is licensed by the current source theorem.
MS05 Section8 replaces the killer exponent by2 in reported finite computations of particular prime tuples, but explicitly leaves general cyclotomic freedom unresolved; those finite examples do not certify the moving schedule above with K=2.

This branch therefore stops at a substantive feasibility result: a genuine varying-seed bounded-measure integer family exists at the inspected source scope, but the immediate C160 transfer fails analytically and direct original-window computation is not a useful fallback.
No new J, numerical scan, Claim, strategy/Task decision, arithmetic gap or assertion about actual kappa growth is made.
The source does not presently supply a verified smaller moving-exponent replacement with the same complete cyclotomic accounting.
Further work would require a separately motivated projection estimate that handles the degenerating Gram modes, or a different actually proved input family.

<a id="moving-exponent-joint-kernel-question"></a>
## Exact unresolved quantity after the separate bounds fail

The appropriate remaining object is a JOINT normalized symbol, not the inverse matrix by itself.
Let w_r(z)=(1,z,...,z^(r-1))^t and define

    Theta_j(z)=w_(r_j)(z^-1)^t G_j^(-1)w_(r_j)(z),
    Xi_j(z)=d_j^(-1)N_j(z)N_j(z^-1)Theta_j(z).

The accepted [L321 exact coefficient projection identity](Yin_L_G0321_v1.md#residual-laurent-square-identity), applicable to the full N_j relation columns in this same window, gives

    v_(2d_j)(z^-1)^t R_N v_(2d_j)(z)=2d_j-d_j Xi_j(z),
    kappa_(2d_j)(R_N)=sum_(h!=0)abs(Xihat_j(h)).     (G5)

Every dimension and the original d_j normalization are explicit.
Together with the rank-three correction, the actual question is whether the right side of(G5) is uniformly bounded or unbounded along the selected schedule.
A proof of either behavior for this JOINT quantity would transfer to the actual P_j with additive error less than6.
The vanishing Rayleigh quotient only describes G_j and does not settle(G5), because multiplication by N_j on both sides removes the same directions that can make the inverse large.
The partial-deflation alternatives likewise require controlling their joint normalized symbols; an unbounded raw coefficient norm is not itself a projection obstruction.
This exact joint Wiener-norm question remains open after the bounded feasibility result.

<a id="moving-exponent-fixed-inputs"></a>
## Exact fixed inputs and proof boundaries

| Role | Target | Scope |
| --- | --- | --- |
| Complete construction | [MS05-U001 construction](../audits/literature/MS05/Yin_U001.md#ms05-arbitrary-distinct-prime-construction) | Actual retained manuscript, circular interlacing, common torsion-coset exponent and arbitrary eligible distinct primes, parity, exact cyclotomic removal and Salem conclusion; primary-statement acceptance and selected proof/application checks, not a whole original-proof audit. |
| Fixed killer | [Four-exponent specialization](../audits/literature/MS05/Yin_U001.md#ms05-four-exponent-specialization) | Conservative exact K for four exponents, with a support-size upper bound rather than an unsupported exact-count assertion; no numerical prime or lcm evaluation. |
| Exterior-root comparison | [RY26-U001](../audits/literature/RY26/Yin_U001.md#exterior-root-measure-expense) | Actual positive-root equation and2<tau<4 at fixed n=3; the all-large-even-degree theorem and its n>=10000 hypothesis are not used. |
| Fixed-seed comparison | [C160 complete argument](../claims/Yin_C_G0160_v1.md#argument) | The precise raw coefficient/coercivity/graph-growth sufficient package that fails here, not an assertion that all projection estimates fail. |
| Same-window correction | [C160 rank correction](../claims/Yin_C_G0160_v1.md#fixed-seed-original-factor-projection) | Nested relation subspaces and positive rank-three correction, retaining original d and common2d window; prior R530 review stays at its accepted scope. |
| Joint coefficient identity | [L321 projection identity](Yin_L_G0321_v1.md#residual-laurent-square-identity) | Exact full-column inverse-Gram Laurent symbol, used on the reducible raw numerator with its actual rank and original normalization. |
| Actual projection target | [C158](../claims/Yin_C_G0158_v1.md#statement) | Original rank-d residual kernel and all signed Fourier diagonals defining kappa; raw inverse/coefficient divergence is not a substitute. |
