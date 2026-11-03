---
author: Yin
---
# Complete finite Gram-pivot limits, paid windows and all-time torsion loss

The complete original L260 mathematical proof and all19 equations are retained here.
L260 preserves meaningful reuse/search/continuation, original checking and fixed old review inputs.
No Task/E execution resumes.

## Statement

Let P be the ACTUAL monic minimal polynomial of a nonzero algebraic integer alpha, degree d>=1, m=log M(P)>=0, a=exp(2m), H=||P||_2^2 and Delta=|disc P|>=1, with Delta1 at degree1.
Nonunits and torsion are allowed until the separate operator step, which requires a unit.
Let D_j be the coefficient Gram determinant of P,tP,...,t^(j-1)P, D0=1 and delta_j=D_j/D_(j-1).
Then H=delta_1>=delta_2>=...>a and delta_j->a, with EVERY finite strict inequality at every stated degree/input.

For the ORIGINAL iid difference-digit collision probability p_N, with probabilities1/2,1/4,1/4 on0,+/-1, put

    phi(x)=log[2/(1+2^(1-x))], g=phi(a),
    U_N=2^(-N), R_N=Nlog2, 0<=N<=d,
    U_N=2^(-N)product_(j=1)^(N-d)(1+2^(1-delta_j)),
    R_N=dlog2+sum_(j=1)^(N-d)phi(delta_j), N>d.

Then p_N<=U_N and R_N=-log U_N.
At EVERY fixed input R_N/N is nonincreasing for N>=1, strictly above g at every finite N and tends to EXACTLY g.
The first d averages may be equal, and U_(n+N)>=U_n U_N.
Free upper extrapolation from any one positive finite R_N/N is false for this explicit certificate at sufficiently large n.
No equality h2=g or ceiling on true entropy/other mechanisms is asserted.

For N>d,k=N-d, let C_k=log D_k-k log a and Lambda_k=sum_(j=1)^k[phi(delta_j)-phi(a)].
With ell_P=a log2/(1+2^(H-1))>0,

    R_N-Ng=d(log2-g)+Lambda_k,
    ell_P C_k<=Lambda_k<=C_k/2,
    0<=C_k<=dlog N-log Delta+2m(d-1),
    0<R_N-Ng<=d(log2-g)+(d/2)log N
                                 -(1/2)log Delta+m(d-1).

This O_P(log N) upper budget at FIXED input is not a uniform lower arithmetic gain, input-uniform onset or root-separation assumption.
Every original root, discriminant, degree and coefficient expense remains.

For an ACTUAL algebraic UNIT let D_act be its full original zero-to-zero core, K its original kernel on complex counting-measure l2(D_act), and q its real neutral dimension, counting each real neutral root once and each complex pair twice.
For each nonneutral embedding put R_v=1/(abs(v(alpha))-1) outside the circle and R_v=1/(1-abs(v(alpha))) inside.
With one representative per complex pair,

    C_non=product_(real nonneutral v)(2R_v+2)
          product_(complex nonneutral v)(2sqrt2 R_v+2)^2,
    E_N=C_non[2+sqrt(2pi N)]^q>=1,

where every empty product is1.
Then p_N<=||K^N||<=E_N p_N, ||K||<=1, and for EVERY N>=1,n>=0,

    p_n<=min{1,(E_N U_N)^floor(n/N)},
    h2>=max{0,B_N}, B_N=(R_N-log E_N)/N->g.

For N>d,

    N(B_N-g)<=d(log2-g)+(d/2)log N-(1/2)log Delta
                       +m(d-1)-log C_non-qlog[2+sqrt(2pi N)].

Neither sign of B_N-g is imposed.
Both row and rotated-column costs, every neutral/nonneutral place and the ENTIRE expense are paid on EACH repeated block.
For ANY g<c<=log2,epsilon=c-g>0, if B_N>=c at an N>d, necessarily

    N epsilon<=d[log2+m+(1/2)log N],
    N<=(d/epsilon)[log(d/epsilon)+2log2+2m-1].

At a separately justified fixed m<=m0 with c>g(m0), this is an O_(c,m0)(dlog(d+1)) necessary window for THIS paid pivot-product certificate.
No exhaustive search, true mixing-time bound or exclusion of other certificates is inferred.

For EVERY integer r>=0,d=2^r and actual irreducible torsion input P=t^d+1=Phi_(2d), at k=ud+v,0<=v<d,

    D_k=(u+1)^(d-v)(u+2)^v, delta_j=1+1/ceil(j/d).

For EVERY N=Qd+v,0<=v<d, set b_Q=binom(2Q,Q)/4^Q,b0=1,A0=1 and

    A_Q=2^(-Q)product_(ell=1)^(Q-1)(1+2^(-1/ell)), Q>=1.

The entire actual law and product are exactly

    p_N=b_Q^(d-v)b_(Q+1)^v,
    U_N=A_Q^(d-v)A_(Q+1)^v.

A_Q=b_Q at Q0,1,2, but A3=(3/16)(1+1/sqrt2)>5/16=b3.
As Q grows, log A_Q=-(log2/2)log Q+O(1) and log b_Q=-(1/2)log Q+O(1), by summable elementary log-cosh/binomial-ratio errors without a Stirling constant.
At FIXED d as N->infinity,

    log(U_N/p_N)=[d(1-log2)/2]log N+O_d(1)->infinity,
    log(E_N U_N)=[d(1-log2)/2]log N+O_d(1)->infinity.

Here q=d,C_non1 and the full actual-core norm is1 at every fixed time, including d1.
This scalar product plus this particular phase-free grid expense eventually gives a vacuous block certificate on these torsion controls.
No corresponding obstruction to sharper covariance/lattice methods, varying nontorsion families, true entropy gain or unrestricted Mahler gap is proved.

<a id="argument"></a>
## Complete argument

### Adequate actual Gram, classical limit, original-law and operator inputs

All original Sections1--5/equations1--19 follow, retaining every strict/weak inequality, original degree/remainder and fully paid operator boundary.
Their2026-10-10 Task-active/pre-adoption language is chronology, not renewed execution.
The precise [L4](../ledger/Yin_L_G0004_v1.md) mechanisms are sufficiently retained in [C209](Yin_C_G0209_v1.md#argument), whose complete Sections2--4 were compared against the original: primitive integral monic kernel basis, finite dual Gram equality by det(I+B^T B)=det(I+BB^T), full-root Vandermonde/Hadamard and monotone residual interpretation.
No finite reciprocal probe, failed short-window sufficient test or J114 native outcome is a premise or rerun.

Use only [Den09 U002's accepted Theorem2](../audits/literature/Den09/Yin_U002.md#finite-section-determinant): a bounded nonnegative circle symbol positive on a positive-measure set has positive finite Toeplitz sections and determinant-root limit equal to its Mahler mean.
The actual symbol is abs(P)^2, continuous and positive off finitely many circle zeros, with integrable logarithmic mean2m.
Thus D_k^(1/k)->exp(2m); positive decreasing residual ratios have that same limit by their geometric means.
This is the classical nonnegative-symbol interface, not the different bounded-invertible amenable-operator theorem.
The original Szego/Sim05 proof remains uninspected; no PDF/source-proof reading, Alexandersson adoption or new source unit is claimed.

The exact original collision product and monic Mahler residual inequality are sufficiently proved in [C436](Yin_C_G0436_v1.md#triangular-gram-collision-bound), including every original weight/constraint/pivot order and nonunit scope.
For a unit ONLY, [C432's full actual-core theorem](Yin_C_G0432_v1.md#degree-cost-reduced-original-core-norm) supplies the same law/core/counting-l2 operator, both row/rotated-column estimates, all real/complex neutral multiplicities, complete C_non and phase-free E_N.
No killed finite box, missing column bound, auxiliary Gaussian law or unpaid repeated block replaces it.

The all-window binomial control uses [C287's actual signed-basis-block proof](Yin_C_G0287_v1.md#independent-basis-block-collision), not just a rank-only inequality: modulo t^d+1 each coordinate receives independent signed fair bits, and complementation preserves its translated binomial collision law.
The all-time full torsion norm is already proved by [C419's actual-core cube indicators](Yin_C_G0419_v1.md#conditional-gaussian-cost-controls-and-limits).
Its reachability/co-returnability and signed-permutation/cube proof include degree1: every integer vector lies in the original core, and at fixed N the indicator of[-T,T]^d has squared norm ratio at least[(2(T-N)+1)/(2T+1)]^d->1, while contraction gives the opposite bound.
Thus full norm1 and actual original probability are compatible at every degree/time without a new experiment.

<a id="finite-pivot-reuse-and-domain"></a>
### 1. Reuse and precise domain

Let P be the actual monic minimal polynomial of a nonzero algebraic integer alpha, of degree d>=1.
Put m=log M(P), a=exp(2m)>=1, and Delta=|disc(P)|>=1; for degree one the discriminant is1.
These objects permit nonunits and torsion.
The full-operator applications below additionally assume alpha is a unit.

We reuse the complete integer Gram identity, decreasing prediction ratios and their fixed-input limit from [L4](../ledger/Yin_L_G0004_v1.md), including its accepted [Den09-U002](../audits/literature/Den09/Yin_U002.md#finite-section-determinant) Toeplitz-limit interface.
The latter accepts Den09 Theorem2 at statement depth; its classical source proof is not newly inspected here.
The necessary symbol is the continuous nonnegative |P|^2, positive off finitely many circle points, with logarithmic mean2m.
Thus that retained theorem applies even with unit-circle zeros.
The monic residual bound is also in [L94](../ledger/Yin_L_G0094_v1.md#endpoint-gram-mahler-entropy).
The actual collision product is precisely [L256](../ledger/Yin_L_G0256_v1.md#triangular-gram-collision-bound), and the complete operator cost is [L255](../ledger/Yin_L_G0255_v1.md#full-covariance-state-cost-fixed-scope).

A bounded local search read these inputs, the finite Gram certificate and dilation warnings in L4/L9, and L94's sharp independent-basis-block control.
They suffice for the arguments here.
A parallel bounded external search for polynomial-symbol Toeplitz Gram determinants and Schur formulas returned related leads, including the same Alexandersson connection already recorded, unadopted, in L4.
No additional external theorem or priority claim is adopted.
This work does not reprove or upgrade the classical Toeplitz theorem.

For j>=1 define
    D_j=det Gram(P,tP,...,t^(j-1)P), D_0=1,
    delta_j=D_j/D_(j-1), H=||P||_2^2.
The retained results give
    H=delta_1>=delta_2>=...>0,
    delta_j>=a,    delta_j -> a.                       (1)
In fact every finite delta_j>a.
Its residual is PQ with Q monic; equality in ||PQ||_2>=M(PQ)>=M(P) would require the modulus of PQ to be constant almost everywhere on the circle.
A polynomial of constant circle modulus is a monomial: if its first and last nonzero coefficients have distinct indices, their unique maximal nonzero Fourier lag in |PQ|^2 contradicts constancy.
But P has a nonzero root, so cannot divide a monomial.
This proves strictness without an additional arithmetic hypothesis.

Write
    phi(x)=log[2/(1+2^(1-x))], x>=1,
    g=phi(a),
and define the explicit L256 upper bound U_N and its exponent R_N by
    U_N=2^(-N), R_N=N log2,                  0<=N<=d,
    U_N=2^(-N) product_(j=1)^(N-d)(1+2^(1-delta_j)),
    R_N=-log U_N=d log2+sum_(j=1)^(N-d)phi(delta_j),
                                                   N>d. (2)
Thus the ORIGINAL collision probability satisfies p_N<=U_N.
U_N is an upper certificate, not the actual probability in general.

<a id="finite-pivot-limit-and-boundary"></a>
### 2. The exact asymptotic content of this certificate

The increments R_N-R_(N-1) are log2 for N<=d and then phi(delta_(N-d)).
Since phi is strictly increasing and phi(x)<log2 for finite x, these increments form a nonincreasing sequence tending to g.
Therefore
    R_N/N decreases to g,
    R_N/N>g for every finite N>=1.                    (3)
The first d averages can be equal; no strict monotonicity there is asserted.
This follows directly by comparing the next increment with the preceding average and then taking Cesaro means in(1).
In particular, U_(n+N)>=U_n U_N, because decreasing increments imply R_(n+N)<=R_n+R_N.
The same inequality direction is compatible with actual return concatenation, not an exponential upper extension of one finite value.

Equation(3) identifies the limit of this SPECIFIC certificate exactly, for every fixed input.
Even if every finite pivot is computed, taking N to infinity in this unmodified product yields precisely h2>=g(m), with no larger rate.
It does not say that actual h2 equals g(m), or preclude using a paid finite block or additional constraints.
Any proposed extrapolation U_n<=exp[-n R_N/N] for every n from a single finite N is false: (3) eventually makes R_n/n<R_N/N.

There is an explicit boundary estimate.
Set k=N-d and
    C_k=log D_k-k log a>=0,
    Lambda_k=sum_(j=1)^k [phi(delta_j)-phi(a)].
Then
    R_N-Ng=d(log2-g)+Lambda_k.                       (4)
For x>=1,
    x phi'(x)=x log2/(1+2^(x-1))<1/2.                (5)
Indeed put z=x log2.
The last strict bound is equivalent to e^z-4z+2>0.
This convex function has global minimum6-4log4>0 at z=log4; log4<3/2 follows, for example, from e^(3/2)>1+3/2+9/8+27/48>4.
On the whole interval a<=x<=H, also
    x phi'(x)>=ell_P:=a log2/(1+2^(H-1))>0.
Integrating with respect to log x and summing proves
    ell_P C_k<=Lambda_k<=C_k/2.                      (6)
The lower constant depends on the full coefficient norm and is not claimed uniform.

L4's full-root Vandermonde/Hadamard inequality, with the actual integer orbit Gram identity D_k=det(V_NV_N^T), gives
    Delta D_k<=N^d exp[2m(N-1)].
Consequently
    0<=C_k<=d log N-log Delta+2m(d-1),                (7)
and
    0<R_N-Ng
      <=d(log2-g)+(d/2)log N-(1/2)log Delta
                          +m(d-1),       N>d.       (8)
All degree, discriminant and coefficient dependencies are visible.
This is an upper bound on how much finite improvement this product can display, not a positive uniform lower improvement.
In particular the excess is O_P(log N) at a fixed input.
No separation of roots, limit interchange over varying P, or estimate of Delta by a nonintegral substitute is used.

<a id="paid-pivot-window-bound"></a>
### 3. Combining the product with the actual full operator

Now assume alpha is a unit.
Let q be the real dimension of its neutral embedding subspace (each real neutral root counts once, each complex pair twice), and let C_non be L255's full nonneutral cell count, with the empty product equal to1.
Its finite constant retains every expanding and contracting place and their distances from the circle.
Put
    E_N=C_non[2+sqrt(2pi N)]^q>=1.
The retained original full-core counting-l2 operator K satisfies
    p_N<=||K^N||<=E_N p_N, ||K||<=1.
Substitution of the VALID upper probability U_N therefore proves
    p_n<=min{1,(E_N U_N)^floor(n/N)},
    h2>=max{0, [R_N-log E_N]/N}.                     (9)
This is a legitimate finite-block use of the pivots; it pays the complete expense every time the block is repeated.
It is distinct from the invalid free extrapolation after(3).
Define B_N=(R_N-log E_N)/N.
At every fixed unit,
    B_N -> g(m).                                    (10)
Moreover, when N>d,
    N(B_N-g)
      <=d(log2-g)+(d/2)log N-(1/2)log Delta
        +m(d-1)-log C_non-q log[2+sqrt(2pi N)].       (11)
Neither sign of B_N-g is imposed.
Formula(11) retains exactly the neutral dimension rather than replacing it by d.

There is a useful necessary time restriction for this specified method.
Fix a desired rate c with
    g(m)<c<=log2, epsilon=c-g(m)>0.
If its paid certificate B_N is at least c for some N>d, then, by(8), log E_N>=0, log Delta>=0 and g>=0,
    N epsilon<=d[log2+m+(1/2)log N].                 (12)
Write t=N/d.
The elementary inequality log t<=epsilon t-log epsilon-1 gives
    N <= (d/epsilon)
          [log(d/epsilon)+2log2+2m-1].               (13)
To check the direction, substitute log N=log d+log t in(12), move epsilon t/2 to the left, and multiply by2/epsilon.
No assumption about a computed exact p_N is present.

Thus a fixed positive gain over g cannot be certified by merely taking arbitrarily long windows of this same product.
With a separately justified small-m range m<=m0 and c>g(m0), (13) implies a necessary O_(c,m0)(d log(d+1)) window.
This is a search restriction for the pivot-product/full-grid certificate, not an upper bound on the time needed by all methods or on a true mixing time.
A failure throughout such a window would refute only this sufficient certificate at the tested input; no such exhaustive computation is claimed here.

<a id="all-window-torsion-pivot-control"></a>
### 4. An exact all-window control and its growing loss

Take d=2^r with integer r>=0 and actual irreducible P=t^d+1=Phi_(2d).
This retains an admissible degree-d torsion control, not a nontorsion counterexample.
The coefficient Gram of k shifts has diagonal2 and entries1 at offsets +/-d, all other entries zero.
Permuting indices modulo d splits it into tridiagonal chains.
A chain of length s has determinant s+1: expansion gives T_s=2T_(s-1)-T_(s-2), T_0=1,T_1=2.

For k=ud+v, 0<=v<d, this gives
    D_k=(u+1)^(d-v)(u+2)^v,
    delta_j=1+1/ceil(j/d).                           (14)
No numerical experiment is used.
For N=Qd+v with0<=v<d, define
    b_Q=binom(2Q,Q)/4^Q, b_0=1,
    A_0=1, A_Q=2^(-Q)
          product_(ell=1)^(Q-1)(1+2^(-1/ell)), Q>=1.
Then the complete formulas are
    p_N=b_Q^(d-v)b_(Q+1)^v,
    U_N=A_Q^(d-v)A_(Q+1)^v.                          (15)
For the probability, use L94's exact torsion basis-block control: each residue coordinate has Q or Q+1 independent signed fair bits, signs only translate its binomial law, and residues use disjoint bits.
Their difference returns independently with probabilities b_Q or b_(Q+1).
Formula(14) substituted into(2) proves the U_N identity, including Q=0.
Thus(15) compares the full actual law with the exact pivot certificate on every window.

At Q=1,2 there is equality: A_1=b_1=1/2 and A_2=b_2=3/8.
Already
    A_3=(3/16)(1+1/sqrt2)>5/16=b_3,
because1/sqrt2>2/3.
The loss grows with the window.
Indeed
    log A_Q
       =-log2-(log2/2) sum_(ell=1)^(Q-1)1/ell
                     +sum_(ell=1)^(Q-1)
                           log cosh[(log2)/(2ell)]
       =-(log2/2)log Q+O(1),                         (16)
since0<=log cosh x<=x^2/2 and the squared reciprocal series converges.
The harmonic sum differs from log Q by a bounded amount by integral comparison.
Likewise b_Q/b_(Q-1)=1-1/(2Q) yields
    log b_Q=-(1/2)log Q+O(1):                        (17)
for Q>=2 the error in log(1-1/(2Q))+1/(2Q) is bounded in absolute value by a constant times Q^(-2), by the convergent logarithmic series.
The first term is a fixed constant.
This proof needs no uninspected Stirling formula or claimed asymptotic constant.

For fixed d, as N grows, the finitely many possible remainders in(15) give
    log(U_N/p_N)
       =[d(1-log2)/2]log N+O_d(1) -> infinity.       (18)
All roots are neutral and C_non=1, so the particular L255 phase-free expense is E_N=[2+sqrt(2pi N)]^d.
Therefore
    log(E_N U_N)
       =[d(1-log2)/2]log N+O_d(1) -> infinity.       (19)
At these controls the full-core operator norm is1, consistently with the existing torsion analysis.
Equation(19) says this scalar product plus that grid expense eventually gives a vacuous finite-block certificate.
It is not a statement that the exact row/column covariance bound, every lattice method, or the nontorsion core has the same defect.

<a id="finite-pivot-continuation-boundary"></a>
### 5. What changes in the next exploration

The unmodified finite-pivot product now has an exact fixed-input limiting scope, an explicit O_P(log N) upper budget for its boundary improvement, and a necessary finite time range for any proposed paid rate above g(m).
Its all-window torsion comparison exhibits a polynomial loss even though its first nontrivial window can be sharp.
Therefore a meaningful next change is to retain coupled digit constraints or actual Gaussian-center information, improve actual-order counting with its full cost, or prove a discriminating arithmetic fact within a useful finite window.
Merely computing more pivots and sending N to infinity cannot improve this product's limiting exponent.

This does not rule out a positive uniform excess in an appropriate varying-input window, prove a restriction on true h2 beyond the reused bounds, or solve the unrestricted Mahler-gap problem.
The search window in(13) depends on the desired gain and the actual m; no algorithm for deciding the full Task is supplied.
No new computation, program or J is used.
The entire present derivation is authored by the coordinator; the concurrent agents' new arguments are not premises.


### Actual whole-check and source/nonexecution limits

The complete original L260/R159 were read, all19 equations retained and the required C209/L4/Den09/C436/C432/C287/C419 mechanisms compared at their actual scopes.
Every derivative/discriminant/window inequality and complete torsion/remainder/logarithmic calculation is a written symbolic proof, not a numerical scan or unreported execution.
No program, finite-pivot producer, J114/J52 run or exhaustive search of the necessary interval was performed.
The older Alexandersson abstract/search extract remains an unadopted lead in the original research record, not a proof premise.
Den09's original Toeplitz/Szego/Sim05 proof depth and all source readers/dates remain unchanged.
R159's generic shared conversations/upstream roles do not establish its initial target-specific context, so its original entire finding remains UNKNOWN rather than being classified from those roles.
The present whole check is SELF and supplies no fresh isolation of that old scope.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:30 |
| status | open |
| reason | Retain the entire original finite-pivot proof/all19 equations, exact certificate limit/strict finite excess, all original-root discriminant/degree/coefficient costs, unit-only full-operator payment/necessary window and complete all-window torsion/binomial/logarithmic controls with adequate fixed mechanisms. No producer/native/source-proof/Task expansion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact complete theorem](#statement) | All actual nonzero algebraic integers/degrees/torsion/nonunits until unit-only operator, every finite N, strict/weak limit/discriminant cost, each chosen paid rate/window, every dyadic degree/remainder/true law/full norm and negative limit. |
| argument | [Entire proof](#argument) | Complete original Sections1--5/equations1--19 plus actual kernel/root/classical-limit/pivot/operator/binomial/core interfaces and all source/nonexecution boundaries. |
| dependency | [Actual finite Gram/root/residual mechanism](Yin_C_G0209_v1.md#argument) | Complete Sections2--4 only: saturated integral monic kernel/finite dual Gram, all-root Vandermonde/Hadamard/monotone residuals; no J114 finite-probe outcome. |
| dependency | [Accepted classical nonnegative-symbol limit](../audits/literature/Den09/Yin_U002.md#den09-u002) | Theorem2 for actual bounded abs(P)^2 positive off finitely many zeros, positive finite sections and determinant-root limit; original Szego/Sim05 proof uninspected, no invertible-only substitution. |
| dependency | [Original collision-pivot product](Yin_C_G0436_v1.md#triangular-gram-collision-bound) | Same exact original digit law, full monic quotient/leading Schur pivots/Mahler residual and upper U_N for every nonzero algebraic integer; no chronological-unit premise. |
| dependency | [Full unit operator and all costs](Yin_C_G0432_v1.md#degree-cost-reduced-original-core-norm) | Full actual zero-to-zero core/counting-l2, both row/rotated-column bounds, all places/nonneutral constants/q/full E_N/contraction/repeated-block expense; unit scope only. |
| dependency | [Actual signed-binomial control](Yin_C_G0287_v1.md#independent-basis-block-collision) | Full dyadic-cyclotomic independent coordinates/signed-bit complementation/central-binomial probabilities, with local proof of all remainders; no rank-only equality assumption. |
| dependency | [Actual all-time torsion core/norm proof](Yin_C_G0419_v1.md#conditional-gaussian-cost-controls-and-limits) | Full order reachability/co-returnability, signed-permutation cube indicators and norm1 at every fixed time, degree1 included; its older less precise expense is not used. |

### Decision complete-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:32 |
| status | proved |
| reason | Adopt after the actual whole C448/R652 SELF check of every original Section1--5/equation1--19, all finite strictness/monotone-average/derivative/discriminant bounds, actual unit-only full-operator repeated-block payment and necessary-window quantifiers, and every dyadic degree/remainder/exact probability/logarithmic/full-core-norm control. All needed C209/Den09/C436/C432/C287/C419 mechanisms were compared at their precise scopes, preserving the original accepted classical proof depth and unadopted source lead. No computation/source-proof/Task expansion. Original R159 whole UNKNOWN remains; upstream roles/unspecified shared conversations do not establish initial target isolation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact complete theorem](#statement) | All actual nonzero algebraic integers/degrees/torsion/nonunits until unit-only operator, every finite N, strict/weak limit/discriminant cost, each chosen paid rate/window, every dyadic degree/remainder/true law/full norm and negative limit. |
| argument | [Entire proof](#argument) | Complete original Sections1--5/equations1--19 plus actual kernel/root/classical-limit/pivot/operator/binomial/core interfaces and all source/nonexecution boundaries. |
| dependency | [Actual finite Gram/root/residual mechanism](Yin_C_G0209_v1.md#argument) | Complete Sections2--4 only: saturated integral monic kernel/finite dual Gram, all-root Vandermonde/Hadamard/monotone residuals; no J114 finite-probe outcome. |
| dependency | [Accepted classical nonnegative-symbol limit](../audits/literature/Den09/Yin_U002.md#den09-u002) | Theorem2 for actual bounded abs(P)^2 positive off finitely many zeros, positive finite sections and determinant-root limit; original Szego/Sim05 proof uninspected, no invertible-only substitution. |
| dependency | [Original collision-pivot product](Yin_C_G0436_v1.md#triangular-gram-collision-bound) | Same exact original digit law, full monic quotient/leading Schur pivots/Mahler residual and upper U_N for every nonzero algebraic integer; no chronological-unit premise. |
| dependency | [Full unit operator and all costs](Yin_C_G0432_v1.md#degree-cost-reduced-original-core-norm) | Full actual zero-to-zero core/counting-l2, both row/rotated-column bounds, all places/nonneutral constants/q/full E_N/contraction/repeated-block expense; unit scope only. |
| dependency | [Actual signed-binomial control](Yin_C_G0287_v1.md#independent-basis-block-collision) | Full dyadic-cyclotomic independent coordinates/signed-bit complementation/central-binomial probabilities, with local proof of all remainders; no rank-only equality assumption. |
| dependency | [Actual all-time torsion core/norm proof](Yin_C_G0419_v1.md#conditional-gaussian-cost-controls-and-limits) | Full order reachability/co-returnability, signed-permutation cube indicators and norm1 at every fixed time, degree1 included; its older less precise expense is not used. |
| review | [Actual whole SELF finding](../audits/reviews/Yin_R_G0652_v1.md#finite-pivot-whole-self-finding) | Complete exact statement/argument/all direct interfaces, every actual degree/circle-zero/nonunit-versus-unit/certificate-versus-law/finite window/torsion/remainder/full-cost/source/negative boundary; does not close original R159 whole UNKNOWN. |


### Decision complete-isolated-whole-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T21:54 |
| status | proved |
| reason | Adopt R669 after complete coordinator reading of the new isolated whole C448 finding, covering all original finite-pivot/probability/limit/discriminant/actual-operator/repeated-expense/window/dyadic proofs and exact source/negative boundaries. Preserve R159 whole UNKNOWN and all original author/current SELF scopes and dates; no native or source-proof expansion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | All actual nonzero algebraic integers/degrees/torsion/nonunits until unit-only operator, every finite N, strict/weak limit/discriminant cost, each chosen paid rate/window, every dyadic degree/remainder/true law/full norm and negative limit. |
| argument | [Exact argument](#argument) | Complete original Sections1--5/equations1--19 plus actual kernel/root/classical-limit/pivot/operator/binomial/core interfaces and all source/nonexecution boundaries. |
| dependency | [Exact dependency](Yin_C_G0209_v1.md#argument) | Complete Sections2--4 only: saturated integral monic kernel/finite dual Gram, all-root Vandermonde/Hadamard/monotone residuals; no J114 finite-probe outcome. |
| dependency | [Exact dependency](../audits/literature/Den09/Yin_U002.md#den09-u002) | Theorem2 for actual bounded abs(P)^2 positive off finitely many zeros, positive finite sections and determinant-root limit; original Szego/Sim05 proof uninspected, no invertible-only substitution. |
| dependency | [Exact dependency](Yin_C_G0436_v1.md#triangular-gram-collision-bound) | Same exact original digit law, full monic quotient/leading Schur pivots/Mahler residual and upper U_N for every nonzero algebraic integer; no chronological-unit premise. |
| dependency | [Exact dependency](Yin_C_G0432_v1.md#degree-cost-reduced-original-core-norm) | Full actual zero-to-zero core/counting-l2, both row/rotated-column bounds, all places/nonneutral constants/q/full E_N/contraction/repeated-block expense; unit scope only. |
| dependency | [Exact dependency](Yin_C_G0287_v1.md#independent-basis-block-collision) | Full dyadic-cyclotomic independent coordinates/signed-bit complementation/central-binomial probabilities, with local proof of all remainders; no rank-only equality assumption. |
| dependency | [Exact dependency](Yin_C_G0419_v1.md#conditional-gaussian-cost-controls-and-limits) | Full order reachability/co-returnability, signed-permutation cube indicators and norm1 at every fixed time, degree1 included; its older less precise expense is not used. |
| review | [Exact review](../audits/reviews/Yin_R_G0669_v1.md#finite-pivot-whole-independent-finding) | Complete exact C448v1 Statement and Argument, all equations1--19, every all-degree finite bound and unit-only full-operator cost, all dyadic exact controls and declared source/negative limits. |

