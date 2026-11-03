---
author: Yin
---
# Near-one real reciprocal models with maximal projection coherence

Date: 2026-10-18T10:54.
Human author Yin.
Root proposed adjoining a real reciprocal off-circle pair to C143's quadratic-residue model and supplied the nested-projection and rank-three Fourier-Gram mechanism.
The entropy_attainment_bridge AI supplies the complete estimates, explicit nonrational subfamily and angular equidistribution calculation below.
Both are contributors and neither can independently review this complete result.
The complete argument was developed in D43 and is now registered as a fixed proof draft for separate whole review.
Author checking is not independent review or mathematical adoption.
No numerical program or search is run.

<a id="real-coherence-model-reuse"></a>
## Exact question and reused boundaries

Can small total polynomial Mahler measure, one real off-circle pair, reciprocal symmetry and weak angular equidistribution alone force a degree-free upper bound for the actual fixed-2d residual coherence?
The coefficient domain of this test is explicitly REAL, not the integer irreducible domain of G0001.

The author read [C143's quadratic-residue model](Yin_C_G0143_v1.md#quadratic-residue-projection-model), its [actual integer lift and measure costs](Yin_C_G0143_v1.md#projection-obstruction-original-costs), and its actual [whole-reviewed decision](Yin_C_G0143_v1.md#decision-whole-reviewed-2026-10-15).
Those inputs supply the exact Gauss magnitudes, real reciprocal polynomial, positive-semidefinite diagonal-sum estimate, and arbitrarily large primes congruent 1 modulo 4.
The present extension does not alter C143's integer family, whose total measure is bounded away from zero and grows with its scale.

[L13](../ledger/Yin_L_G0013_v1.md#fixed-surplus-vanishing-measure) already gives a different real reciprocal family with one real off-circle pair, total polynomial measure tending to zero and a fixed surplus in a SHORT-WINDOW DETERMINANT.
It does not claim the present signed-diagonal coherence conclusion.
The same complete fixed-surplus argument is now retained and adopted in [C211](Yin_C_G0211_v1.md#fixed-surplus-vanishing-measure); this current locator does not change the original L13 comparison input or its dated review binding.
[L318's projection estimate](Yin_C_G0600_v1.md#all-residual-columns-signed-diagonal-coherence) gives the general square-root upper bound; its elementary matrix proof applies to real polynomial coefficient projections without an arithmetic premise.
The finite Fourier-to-continuous-test approximation used below is already retained in [L208](../ledger/Yin_L_G0208_v1.md#actual-coset-hyperbolic-density).
The scoped local search found these adequate ingredients but no retained near-one real-coefficient square-root coherence model.
No new external result, full-source audit or novelty assertion is needed.

<a id="real-near-one-coherence-statement"></a>
## Statement

Let ell be a rational prime congruent 1 modulo 4.
Let S be the nonzero quadratic residues modulo ell, zeta=exp(2pi i/ell), and

    r=(ell-1)/2,
    d=r+2=(ell+3)/2,
    N=2d=ell+3,
    Q_ell(t)=product_(a in S)(t-zeta^a).

For any epsilon>0 set tau=exp(epsilon) and

    P_(ell,epsilon)(t)=(t-tau)(t-tau^(-1))Q_ell(t).   (1)

This is a monic real reciprocal squarefree polynomial of degree d, with constant coefficient 1.
It has exactly one positive real off-circle pair and all its remaining r roots on the unit circle.
Its TOTAL polynomial logarithmic Mahler measure is exactly epsilon.

For any real monic polynomial H of degree h<N, let R_H be the orthogonal projection in the SAME N-coordinate coefficient space onto the complement of all H multiples of degree below N.
Thus R_H has rank h.
For P=P_(ell,epsilon), define the actual fixed-window signed-diagonal coherence by

    a_j(P)=sum_(i=0)^(N-1-j)(R_P)_(i,i+j),
    kappa_(2d)(P)=(2/d)sum_(j=1)^(N-1)|a_j(P)|.

Then, uniformly for every epsilon>0,

    sqrt(ell)-8 < kappa_(2d)(P) <= sqrt(ell+2).       (2)

In particular kappa_(2d)(P)/sqrt(ell) tends to 1 as ell tends to infinity, uniformly in epsilon.
The lower bound is meaningful as a growing positive bound for sufficiently large ell; no positivity beyond the actual definition is inferred from its negative values at small ell.

For the explicit choice

    tau_ell=1+1/ell,
    epsilon_ell=log(1+1/ell),

the total measure tends to zero and every P_(ell,epsilon_ell) has a nonrational coefficient.
Its angular empirical root measures converge weakly to circle Haar probability.
More explicitly, for every nonzero integer n not divisible by ell,

    |(1/d)sum_(all roots alpha) (alpha/|alpha|)^n|
       <=(sqrt(ell)+3)/(ell+3),                    (3)

whereas the same angular average is exactly 1 when ell divides n.
In particular (3) holds uniformly for 1<=|n|<=ell-1, but a moving alias at frequency ell lies inside the kernel's degree window N-1=ell+2.
This distinction is part of the result, not an omitted uniform-frequency hypothesis.

The following complete arithmetic-boundary assertions are also part of the statement.
The coefficients of Q_ell lie in K_ell=Q(sqrt(ell)); its nontrivial coefficient conjugate satisfies Q_ell Q_ell^conj=Phi_ell.
For tau=(ell+1)/ell, the primitive integer clearing of its reciprocal quadratic is

    A_ell=[ell t-(ell+1)][(ell+1)t-ell],

with logarithmic measure 2log(ell+1).
The primitive integer clearing of the complete quadratic coefficient norm P P^conj is A_ell^2 Phi_ell, with logarithmic measure 4log(ell+1).

There is also the following variant with algebraic-integer coefficients and roots.
For a=floor(sqrt(ell)), u_0=(sqrt(ell)-a)^2, and ANY positive integer j satisfying u=u_0^j<=ell^(-2), let

    B(t)=t^2-(2+u)t+1,
    lambda>1 be its larger real root,
    epsilon=log lambda,
    P=B Q_ell.

Then P is nonrational, all its coefficients are algebraic integers in K_ell, all its roots are algebraic integer units, and 0<epsilon<=sqrt(u)<=1/ell.
It has the same real reciprocal squarefree root geometry and bounds (2)--(3).
If lambda_+^conj is the larger root of B^conj, then lambda_+^conj>1+u^conj>=1+ell^2.
The full quadratic coefficient norm is the monic constant-one integer polynomial

    P P^conj=Phi_ell B B^conj,
    m(P P^conj)=epsilon+log(lambda_+^conj)>2log ell.

The word conjugate in this assertion refers to the complete nontrivial coefficient-field conjugation, with all roots of its polynomial retained.
Neither these displayed nonrational models nor their changed-degree complete norms are asserted to be irreducible integer near-one inputs.
The full proofs and costs of both variants are in the final two argument sections.

<a id="argument"></a>
<a id="same-window-projection-inclusion"></a>
## Actual polynomial projections and the two added root directions

For Q=Q_ell use the r-by-N evaluation matrix

    E_(a,j)=zeta^(a j), a in S, 0<=j<N.

Its first r columns form a nonsingular Vandermonde matrix because the r roots are distinct.
Its kernel consists precisely of coefficient vectors of complex polynomials of degree below N divisible by Q.
The actual coefficient residual projection therefore equals

    R_Q=E^*(EE^*)^(-1)E.                             (4)

The same statement holds for P using its d distinct roots, so R_P has rank d.
Every P multiple is a Q multiple, since Q divides P.
Their relation spaces are therefore nested in the reverse direction to their residual spaces:

    range(R_Q) subset range(R_P).

It follows that

    D=R_P-R_Q

is an orthogonal projection of rank d-r=2.
Indeed the inclusion gives R_P R_Q=R_Q R_P=R_Q, and then D^*=D and D^2=D.
Thus D is positive semidefinite and trace(D)=2.
There is no root-separation, Vandermonde-conditioning or epsilon-dependent perturbation cost in this exact inclusion.
All matrices R_Q,R_P,D are real: the underlying real polynomials have real relation matrices, and the complex formulas compute their complex-linear extensions.

## Three extra Fourier coordinates and the complete correction price

The first ell columns of E are orthogonal finite Fourier rows.
The remaining three columns, at indices ell,ell+1,ell+2, repeat the columns with exponents 0,1,2.
Let W be this r-by-3 final block.
Then

    EE^*=ell I_r+WW^*.

Set B=ell^(-1)E^*E and H=B-R_Q.
The finite positive matrix ell I_r+WW^* has inverse at most ell^(-1)I_r, so H is positive semidefinite.
The difference of the two inverses has rank at most rank(WW^*)<=3, hence rank(H)<=3.
Taking traces gives the exact cost

    trace(H)=Nr/ell-r=3r/ell.                        (5)

No estimate of the three nonzero eigenvalues separately is needed.
Together with the preceding section this gives the exact decomposition

    R_P=B-H+D,
    H>=0, trace(H)=3r/ell,
    D>=0, trace(D)=2.                               (6)

For every positive-semidefinite N-by-N matrix M, the C143 estimate gives

    sum_(j=1)^(N-1)|sum_i M_(i,i+j)|
       <=sum_(i<j)|M_ij|
       <=(N-1)trace(M)/2.                           (7)

For completeness, |M_ij|<=sqrt(M_ii M_jj), and summing the latter over i<j gives
[(sum_i sqrt(M_ii))^2-trace(M)]/2, which is at most (N-1)trace(M)/2 by Cauchy-Schwarz.
This prices the complete off-diagonal corrections from H and D, including frequencies not retained in the lower bound.

<a id="gauss-diagonal-lower-bound"></a>
## Gauss sums survive both corrections

Write S_j=sum_(a in S)zeta^(a j).
C143's exact calculation gives S_j real and

    |1+2S_j|=sqrt(ell),
    |S_j|>=(sqrt(ell)-1)/2,  1<=j<ell.              (8)

The j-th upper diagonal sum of B is (N-j)S_j/ell.
Apply the triangle inequality in the subtractive direction to (6), keep only the baseline frequencies 1,...,ell-1, and use (7) on the full H,D corrections.
Since

    sum_(j=1)^(ell-1)(N-j)=(ell-1)(ell+6)/2,

this yields

    kappa_(2d)(P)
      >=[(ell-1)(ell+6)/(ell(ell+3))](sqrt(ell)-1)
        -3(ell-1)(ell+2)/(ell(ell+3))
        -4(ell+2)/(ell+3).                          (9)

For ell>=5 the first bracket is greater than 1, the second subtracted quantity is less than 3, and the third is less than 4.
Thus (9) is strictly greater than sqrt(ell)-8, proving the lower part of (2).
Every root and the original d,N normalization have been retained.

The upper bound is the reused L318 projection calculation.
For clarity, if R is a real rank-d orthogonal projection in N dimensions and a_j=sum_i R_(i,i+j), then

    sum_j a_j^2/(N-j)
       <=sum_(i<j)R_ij^2
       =[d-sum_i R_ii^2]/2
       <=d(N-d)/(2N).

Cauchy-Schwarz over the N-1 diagonals and sum_j(N-j)=N(N-1)/2 give

    (2/d)sum_j|a_j|<=sqrt((N-1)(N-d)/d).

Substituting N=2d=ell+3 proves the upper part of (2).
This proof uses only projection rank and the actual coefficient window, so its use on the real polynomial (1) introduces no unsupported integer premise.

<a id="real-model-equidistribution-and-domain"></a>
## Equidistribution and the explicit missing arithmetic

The angular empirical measure has the r points zeta^a for a in S and two additional atoms at 1.
For ell not dividing n its Fourier coefficient is

    (S_n+2)/d=(1+2S_n+3)/(ell+3).

Equation (8), applied to n modulo ell, proves (3).
For ell dividing n every angular point has n-th power 1, giving the exact alias.
Thus every fixed nonzero Fourier coefficient tends to zero as ell grows through the primes congruent 1 modulo 4, since eventually ell does not divide that fixed integer.
The zero coefficient is 1.

This implies weak convergence against every continuous circle function.
Indeed the L208 finite Fejer approximation gives a trigonometric polynomial uniformly within any prescribed eta>0 of the fixed continuous function.
For that fixed polynomial only finitely many Fourier coefficients are involved, and their convergence was just established.
The two uniform approximation errors are at most 2eta, since both empirical and Haar measures have total mass 1.
Let ell tend to infinity and then eta to zero.
No uniform approximation of a degree-growing kernel or moving test is asserted.

For tau_ell=1+1/ell, the quadratic factor in (1) is rational, and its t coefficient is -(tau_ell+tau_ell^(-1)).
The coefficient of t^(r-1) in Q is -S_1.
Since 1+2S_1 is real of modulus sqrt(ell), it equals either sqrt(ell) or -sqrt(ell), and S_1 is irrational.
Therefore the coefficient of t^(d-1) in P is

    -S_1-(tau_ell+tau_ell^(-1)),

which is irrational.
This proves directly that the displayed near-one family is outside Q[t], and hence outside the monic irreducible integer-unit domain.
It is not obtained by selecting only some embeddings of an actual irreducible integer input and retaining its old arithmetic claims.

The positive exterior root tau_ell itself has primitive integer minimal polynomial ell t-(ell+1), of Mahler measure log(ell+1), not epsilon_ell.
It is not an algebraic integer unit.
The factor Q contains only one quadratic-residue half of the primitive ell-th roots, not their complete rational conjugacy orbit.
Those two precise arithmetic failures explain why the small real-polynomial measure cannot be substituted into G0001 or the actual-conjugate hypotheses of C159.

Root additionally identified the exact quadratic coefficient-field and denominator boundary, which can be verified here without a new source input.
In fact Q_ell has coefficients in Q(sqrt(ell)).
To see this directly, express each elementary symmetric root coefficient as an integer sum of powers zeta^j, with multiplicities counted before collection.
Multiplication of every chosen residue by a fixed element of S permutes the chosen subsets, so the integer coefficient counts are constant on S and on its nonresidue complement separately.
Each coefficient consequently has the form c_0+c_R S_1+c_N T_1, where T_1 is the sum over nonresidues and S_1+T_1=-1.
Since 1+2S_1 is either sqrt(ell) or -sqrt(ell), all these coefficients lie in Q(sqrt(ell)).
Multiplication by a nonresidue interchanges the two root sets and the two counts; the nontrivial quadratic conjugation interchanges S_1 and T_1.
Thus the coefficient conjugate Q_ell^conj is exactly the nonresidue-root polynomial, and

    Q_ell Q_ell^conj=(t^ell-1)/(t-1)=Phi_ell(t).     (10)

For lambda=(ell+1)/ell, the exact primitive integer clearing of its reciprocal quadratic is

    A_ell(t)=ell(ell+1)t^2-[2ell(ell+1)+1]t+ell(ell+1)
             =[ell t-(ell+1)][(ell+1)t-ell].       (11)

The three coefficients have gcd 1 because the middle coefficient is 1 modulo ell(ell+1).
Its multiplicative Mahler measure is (ell+1)^2 and its logarithmic measure is 2log(ell+1), rather than epsilon_ell.
Replacing the missing half-orbit by the full Phi_ell and clearing the quadratic therefore gives A_ell Phi_ell, whose logarithmic measure is still 2log(ell+1).
Taking the full quadratic coefficient-field norm of the original P instead gives the rational polynomial [(t-lambda)(t-lambda^(-1))]^2 Phi_ell; its primitive integer clearing is A_ell^2 Phi_ell and has logarithmic measure 4log(ell+1).
These products are primitive by the same monic/Gauss content convention used in C143, and Phi_ell contributes zero Mahler measure because every root is on the circle.
Neither repair preserves a small TOTAL integer-polynomial measure, the original degree, or an unproved projection estimate after that change.
This verification credits root's added observation; no rational or integral near-one counterexample is asserted.

<a id="quadratic-integer-coefficient-variant"></a>
## Stronger variant: algebraic-integer coefficients with a paid missing conjugate

Root supplied the following stronger construction to distinguish failure of rational Galois closure from failure of coefficient integrality over a larger field.
Let K_ell=Q(sqrt(ell)), put a=floor(sqrt(ell)), and set

    u_0=(sqrt(ell)-a)^2,
    u_0^conj=(sqrt(ell)+a)^2,
    Norm_(K_ell/Q)(u_0)=(ell-a^2)^2>=1.

Both elements are algebraic integers, with 0<u_0<1 and u_0^conj>1.
Choose any positive integer j with u=u_0^j<=ell^(-2); such an integer exists since u_0^j tends to zero.
Its conjugate u^conj satisfies

    u u^conj=Norm(u_0)^j>=1,
    u^conj>=1/u>=ell^2.

Define B(t)=t^2-(2+u)t+1 and let lambda>1 be its larger real root.
Its other root is lambda^(-1)>0.
Writing epsilon=log lambda, one has 2cosh(epsilon)=2+u and cosh(epsilon)>=1+epsilon^2/2, hence

    0<epsilon<=sqrt(u)<=1/ell.                     (12)

Now P=B Q_ell has all coefficients in the ring of algebraic integers of K_ell, is monic with constant coefficient 1, and has exactly the same root geometry and projection bounds (2)--(3).
Its total real-polynomial measure tends to zero by (12).
The roots of P are algebraic integer units: roots of Q are roots of unity, while a root and its inverse from the monic B are integral over the algebraic integers and hence algebraic integers over Z.
This strengthens the model's coefficient and root integrality but still does not supply complete rational conjugacy or a polynomial in Z[t].
Root also observed an immediate coefficient check: u=A_0+B_0 sqrt(ell) with integers A_0,B_0 by its displayed power construction, while Q_ell's leading-next coefficient is 1/2 minus or plus sqrt(ell)/2.
The coefficient of sqrt(ell) in the leading-next coefficient of P is therefore -B_0 minus or plus 1/2, which is nonzero.
Hence P is nonrational for every allowed j, without a parameter-avoidance condition.

Indeed the conjugate quadratic B^conj has larger root lambda^conj_+>1+u^conj.
For x>1 the function x+x^(-1) is strictly increasing, and at x=1+u^conj its value is less than 2+u^conj, proving this strict inequality.
Thus

    log(lambda^conj_+)>log(1+u^conj)
                         >=log(1+ell^2)>2log ell.   (13)

The full quadratic coefficient norm is exactly

    P P^conj=Phi_ell B B^conj in Z[t].              (14)

It is monic of constant coefficient 1; its coefficients are rational algebraic integers because they are fixed by the nontrivial quadratic conjugation.
Its total logarithmic Mahler measure is

    m(P P^conj)=epsilon+log(lambda^conj_+)>2log ell.

Also m(P^conj)=log(lambda^conj_+)>2log ell whereas m(P)=epsilon<=1/ell.
Therefore P cannot equal P^conj and is not rational, with no need to assume that one particular displayed coefficient avoids accidental cancellation.
The exact missing conjugate, rather than a denominator, now pays the large original measure after rational Galois completion.
No claim that P P^conj is irreducible, or that it retains the original degree and projection coherence, is required or made.
This variant uses only the elementary quadratic conjugation and the original proof above; it requires no Pell theorem, numerical parameter selection or new external input.

## Consequence and author check

The full result simultaneously retains small TOTAL polynomial measure, a single positive real off-circle pair, squarefreeness, reciprocity, weak angular equidistribution and the ACTUAL fixed-2d coefficient projection, yet has maximal-order square-root coherence.
Thus those geometric and weak-equidistribution properties alone do not supply the desired degree-free coherence bound.
The moving alias and the nonrational coefficient domain remain explicit.
In particular this does not refute an arithmetic statement controlling all degree-linear frequencies of the complete conjugates of an irreducible integer unit.

This strengthens the scope discriminator beyond C143's large-measure integer inputs and L13's different near-one real determinant example.
It supplies neither an actual integer near-one counterexample nor an upper coefficient budget on the intended arithmetic class.
The missing useful mechanism must exploit such arithmetic constraints or use a paid test estimate different from generic coherence.

The author checked relation-space inclusion directions, both ranks, same-window rather than padded-window projections, all three extra Fourier columns, positivity and exact trace of H, the full two-sided correction costs, the Gauss phases and diagonal counts, every d,N scalar, uniformity in epsilon, squarefreeness, the explicit irrational coefficient and exterior-root minimal polynomial, the fixed-frequency-first weak-convergence argument, quadratic coefficient conjugation, primitive rational clearing, and all root and norm costs of the algebraic-integer coefficient variant.
No independent review, native numerical evidence or acceptance is asserted.
Root supplied the construction and nested/finite-rank mechanism, the rational Galois/denominator comparison, and the algebraic-integer coefficient variant; the present author supplied the complete quantitative implementation and scope checks.
The fixed registration retains the complete scope discriminator, both arithmetic-boundary variants and every author-check limit.
No numerical experiment, source-audit revision or mathematical acceptance is asserted by registration.


## Current assessment
[Selected decision](#decision-current-complete-fejer-proof-home)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T11:00 |
| status | open |
| reason | Register the complete near-one real-coefficient projection-coherence model, uniform square-root bounds, fixed-frequency and moving-alias distinction, rational denominator expense and algebraic-integer coefficient variant with its full quadratic norm cost, for separate whole review. Root and the drafting agent are contributors. This is not an integer near-one counterexample or mathematical acceptance. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every prime ell congruent1 modulo4 and every epsilon>0, actual N=2d coherence bounds, explicit weak angular convergence and alias, both exact arithmetic-boundary variants and all complete norm expenses. |
| argument | [Complete argument](#argument) | Same-window projection inclusion, rank-three Fourier Gram correction, exact PSD and Gauss diagonal costs, sharp-order upper comparison, fixed-test convergence, coefficient conjugation, rational clearing and all quadratic algebraic-integer variant costs. |
| dependency | [Accepted quadratic-residue model](Yin_C_G0143_v1.md#quadratic-residue-projection-model) | Real reciprocal Q, exact Gauss magnitudes and positive-semidefinite diagonal-sum inequality; its accepted argument also retains the elementary infinite-prime and primitive-content interfaces used here. No large-measure integer lift is imported into the near-one model. |
| dependency | [Accepted projection upper bound](../ledger/Yin_L_G0318_v1.md#all-residual-columns-signed-diagonal-coherence) | Actual coefficient-window coherence normalization and elementary rank-d projection upper bound, explicitly checked here on the broader real-coefficient domain without invoking its integer entropy theorem. |
| dependency | [Finite Fejer approximation](../ledger/Yin_L_G0208_v1.md#actual-coset-hyperbolic-density) | Only uniform approximation of a fixed continuous circle function by finite trigonometric polynomials, to pass from fixed Fourier coefficients to weak angular convergence. No lattice-coset or arithmetic assertion is used. |

### Decision whole-reviewed-2026-10-18

| Field | Value |
| --- | --- |
| date | 2026-10-18T11:03 |
| status | proved |
| reason | Adopt the complete actual-projection scope discriminator after R386's whole noncontributor review, including uniform sharp-order coherence, fixed versus moving frequencies, both coefficient-field variants and full conjugate/denominator costs. The original unrestricted integer Mahler problem is not refuted or resolved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every prime ell congruent1 modulo4 and every epsilon>0, actual N=2d coherence bounds, explicit weak angular convergence and alias, both exact arithmetic-boundary variants and all complete norm expenses. |
| argument | [Complete argument](#argument) | Same-window projection inclusion, rank-three Fourier Gram correction, exact PSD and Gauss diagonal costs, sharp-order upper comparison, fixed-test convergence, coefficient conjugation, rational clearing and all quadratic algebraic-integer variant costs. |
| dependency | [Accepted quadratic-residue model](Yin_C_G0143_v1.md#quadratic-residue-projection-model) | Real reciprocal Q, exact Gauss magnitudes and positive-semidefinite diagonal-sum inequality; its accepted argument also retains the elementary infinite-prime and primitive-content interfaces used here. No large-measure integer lift is imported into the near-one model. |
| dependency | [Accepted projection upper bound](../ledger/Yin_L_G0318_v1.md#all-residual-columns-signed-diagonal-coherence) | Actual coefficient-window coherence normalization and elementary rank-d projection upper bound, explicitly checked here on the broader real-coefficient domain without invoking its integer entropy theorem. |
| dependency | [Finite Fejer approximation](../ledger/Yin_L_G0208_v1.md#actual-coset-hyperbolic-density) | Only uniform approximation of a fixed continuous circle function by finite trigonometric polynomials, to pass from fixed Fourier coefficients to weak angular convergence. No lattice-coset or arithmetic assertion is used. |
| review | [Whole real-coherence finding](../audits/reviews/Yin_R_G0386_v1.md#real-coherence-whole-independent-finding) | Complete frozen statement and proof through both arithmetic variants, all three declared direct interfaces, exact trace/rank/normalization constants and full rational-conjugacy boundary. |


### Decision current-complete-fejer-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-22T01:58 |
| status | proved |
| reason | Maintain only the existing finite-Fejer proof input as the complete same-object C501 home after reading the full consumer and the complete fixed continuous-function approximation argument. The actual use remains uniform approximation of one fixed continuous circle function and its two probability-measure errors; no Salem, lattice-coset or arithmetic assertion is imported. Every other field except this actual date/reason, all nonmatching relation and review tuples/scopes, old decisions and complete mathematics remain unchanged. Old reviewers retain their actual old inputs and are not represented as having read C501; no whole review, independent-coverage upgrade or research Task/E is created. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every prime ell congruent1 modulo4 and every epsilon>0, actual N=2d coherence bounds, explicit weak angular convergence and alias, both exact arithmetic-boundary variants and all complete norm expenses. |
| argument | [Complete argument](#argument) | Same-window projection inclusion, rank-three Fourier Gram correction, exact PSD and Gauss diagonal costs, sharp-order upper comparison, fixed-test convergence, coefficient conjugation, rational clearing and all quadratic algebraic-integer variant costs. |
| dependency | [Accepted quadratic-residue model](Yin_C_G0143_v1.md#quadratic-residue-projection-model) | Real reciprocal Q, exact Gauss magnitudes and positive-semidefinite diagonal-sum inequality; its accepted argument also retains the elementary infinite-prime and primitive-content interfaces used here. No large-measure integer lift is imported into the near-one model. |
| dependency | [Accepted projection upper bound](Yin_C_G0600_v1.md#all-residual-columns-signed-diagonal-coherence) | Actual coefficient-window coherence normalization and elementary rank-d projection upper bound, explicitly checked here on the broader real-coefficient domain without invoking its integer entropy theorem. |
| dependency | [Finite Fejer approximation](Yin_C_G0501_v1.md#actual-coset-hyperbolic-density) | Only uniform approximation of a fixed continuous circle function by finite trigonometric polynomials, to pass from fixed Fourier coefficients to weak angular convergence. No lattice-coset or arithmetic assertion is used. |
| review | [Whole real-coherence finding](../audits/reviews/Yin_R_G0386_v1.md#real-coherence-whole-independent-finding) | Complete frozen statement and proof through both arithmetic variants, all three declared direct interfaces, exact trace/rank/normalization constants and full rational-conjugacy boundary. |

