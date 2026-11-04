---
author: Yin
---

# Explicit integer-coefficient modulus for capacity and determinant convergence

Date: 2026-10-11T19:48.
Human author Yin.
Provenance: project deduction, a quantitative refinement of the exact fixed-input C18 capacity rate within the unchanged [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract).
Root is the substantive author of the entire D19 candidate and the new coefficient-only escape corollary.
Separate whole/extraction review is required.
Classical discriminant/Vandermonde/root-bound mechanisms are credited without a novelty claim.

## Statement

Let P be an ACTUAL monic irreducible minimal polynomial of a nontorsion algebraic integer unit alpha, ORIGINAL degree d>=2, coefficient height H=max_j|p_j|>=1, and ACTUAL O_0=Z[alpha].
E_T is C16/C18's finite rational-packet infimum in allowed window[0,T], with positive normalized rational weights, every value a NONZERO O_0 integer and every aggregate positive lag zero.
The formal-real domain retains the same whole integer remainder condition and has the same infimum.
Total m=log M(P), c is the number of ALL original circle roots, N=T+1, and D_T=det(A_T A_T^T).

Define the explicit positive RATIONAL constants

    R=H+1, b=d(2d-1)-1, s=(2R)^(-b),
    a=s/(R+1), r=1-a,
    lambda=s^(d(d-1))*[(1-r^2)/d]^(d-1),
    B=2d(2R)^(d-1)/lambda,
    N_0=ceil max{2,4d/(lambda*s),
                    4d^2/(lambda^2*a^2),
                    16d/(lambda*a^2)}.

**A. Effective complete-root modulus.**
For EVERY N>=N_0,

    D_T>=(lambda/2)^d N^c exp(2Tm)/|disc P|,
    exp(-2Tm/d)<=E_T
       <=min{1,B N^(1-c/d)exp(-2Tm/d)},
    0<=m-[-d/(2T)]log E_T
       <=[d log B+(d-c)log N]/(2T).

This includes unit-circle roots and an explicit original degree/coefficient-height modulus.
With the canonical scalar single-Haar trace tau(1)=1, m=log Delta_tau(P(U)); no normalized matrix trace is substituted.

**B. Coefficient-only escape and optional certified refinement.**
Necessarily m>=-log r>=a>0.
Consequently the integer

    N_*=ceil max{N_0,2B R^2 d^2/a^2}

depends ONLY on d,H, and satisfies E_(N_*-1)<=1/4.
A finite rational admissible packet of energy strictly below1/2 therefore exists in that allowed window.
More generally a supplied certified0<eta<=m permits replacing a by eta in this threshold.
No optimizer, explicit packet algorithm, small denominator or degree-linear universal bound is asserted.
The positive floor a tends rapidly to0 with degree/height; it is an elementary separation bound, not an unrestricted Lehmer gap.

**C. All arithmetic costs retained.**
For every N>=N_0 a finite rational packet can be chosen with energy less than twice the positive upper expression in A and weighted normalized log-norm income

    0<=Lambda<=[log(2B)]/2+(d-c)log N/(2d).

This is weighted income only.
Its ACTUAL least coefficient denominator q, integer numerators F_j=qf_j, final least weight denominator M and copied full signed product remain those of that packet, with Res(P,F_j)=q^d Norm(f_j(alpha))!=0 and all d embeddings/contents/signs retained.
No individual norm, q/M, packet-size or auxiliary-height bound is claimed.

## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption-20261022)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-11T19:48 |
| status | open |
| reason | Register the complete03:42 D19 quantitative argument and the separately explicit coefficient-only escape consequence. The original whole-author finding, when completed, does not retrospectively cover that new assembly; actual C extraction and bridge review remain pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual original integer-unit domain/O_0, explicit d/H constants, ALL sufficiently large finite windows, capacity-rate modulus and huge coefficient-only escape only. |
| argument | [Argument](#argument) | COMPLETE03:42 D19 Sections1--9/equations1--9 plus the complete new local coefficient-only escape bridge below; no necessary proof remains in a rolling draft. |
| dependency | [Exact capacity domain, finite bound and root-block identity](Yin_C_G0018_v1.md#statement) | Adopted unconditional finite upper/lower capacity inequality and complete complex-scaled original-root Gram identity; includes its exact C17/Sch09 resolved inputs and inspection limits. |
| dependency | [Generic-monic complete-root expense](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Original rational packet norms/resultants, final weights and actual support width for the weighted income estimate, without reciprocal lifting or small-height assumptions. |


### Decision organized-reviewed

| Field | Value |
| --- | --- |
| date | 2026-10-11T19:56 |
| status | proved |
| reason | Adopt the completed separate noncontributor finding for this exact registered scope and selected fixed argument. Complete original histories, current repairs, source inspection limits and all costs remain; no uniform efficiency, unrestricted gap or Task completion is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual original integer-unit domain/O_0, explicit d/H constants, ALL sufficiently large finite windows, capacity-rate modulus and huge coefficient-only escape only. |
| argument | [Argument](#argument) | COMPLETE03:42 D19 Sections1--9/equations1--9 plus the complete new local coefficient-only escape bridge below; no necessary proof remains in a rolling draft. |
| dependency | [Dependency](Yin_C_G0018_v1.md#statement) | Adopted unconditional finite upper/lower capacity inequality and complete complex-scaled original-root Gram identity; includes its exact C17/Sch09 resolved inputs and inspection limits. |
| dependency | [Dependency](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Original rational packet norms/resultants, final weights and actual support width for the weighted income estimate, without reciprocal lifting or small-height assumptions. |
| review | [Current finding](../audits/reviews/Yin_R_G0790_v1.md#c23-effective-capacity-extraction-finding) | Exact registered statement, selected complete argument, changed interfaces and dependencies in this physical version; preserved original reviews are not silently expanded. |


### Decision isolated-whole-review-adoption-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T21:33 |
| status | proved |
| reason | Adopt the separately assigned complete mathematical inspection of this actual fixed statement and entire selected argument at its actual SELF relationship. Its recorded initial finding preceded old target verdict comparison, but the initial fixed argument included completed author-validation conclusions beyond the necessary mathematical derivation. Preserve the exact current mathematical domain, complete proof, source-depth and native-execution limits, all earlier findings and their original relationships, and every arithmetic and physical-window charge. No new uniform construction, optimality or Task/E resumption is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Actual original integer-unit domain/O_0, explicit d/H constants, ALL sufficiently large finite windows, capacity-rate modulus and huge coefficient-only escape only. |
| argument | [Argument](#argument) | COMPLETE03:42 D19 Sections1--9/equations1--9 plus the complete new local coefficient-only escape bridge below; no necessary proof remains in a rolling draft. |
| dependency | [Dependency](Yin_C_G0018_v1.md#statement) | Adopted unconditional finite upper/lower capacity inequality and complete complex-scaled original-root Gram identity; includes its exact C17/Sch09 resolved inputs and inspection limits. |
| dependency | [Dependency](Yin_C_G0010_v2.md#direct-exact-covariance-window-inequality) | Original rational packet norms/resultants, final weights and actual support width for the weighted income estimate, without reciprocal lifting or small-height assumptions. |
| review | [Complete current SELF finding](../audits/reviews/Yin_R_G0790_v1.md#current-effective-capacity) | Complete current fixed statement and entire selected argument, actual required mathematical interfaces and all quantifier, source and execution limits; initial direct reconstruction precedes old target verdict comparison. |

## Argument

The complete new coefficient-only bridge is proved first; it supplements, without changing, the subsequently retained03:42 D19 freeze.
Every separation, conditioning, block-error and finite-threshold proof from that freeze is physically present below.
The same adopted C18 finite inequality supplies the only capacity upper-bound transfer; C16 weak duality alone is not used as a substitute.

<a id="coefficient-only-escape-bridge"></a>
### Local coefficient-only escape bridge

The all-circle implication below is the classical Kronecker statement, identified and elementarily checked in [Smy08-U001](../audits/literature/Smy08/Yin_U001.md#smy08-height-normalization) at printed p.322.
That link is known-result attribution; the complete companion-matrix proof needed here is supplied locally, without importing an uninspected original source proof.

All original roots have absolute product1 because the monic constant coefficient is+/-1.
If none lay outside the unit circle, all would have modulus1.
The original polynomial is irreducible in characteristic0, so its roots are distinct.
Its integer companion matrix is diagonalizable over C with those distinct circle eigenvalues; every positive power is uniformly bounded in one fixed matrix norm.
There are only finitely many integer matrices in that bound.
Thus two positive powers coincide.
The companion is invertible (determinant+/-1), so some positive power is the identity and every eigenvalue, in particular alpha, is a root of unity.
This contradicts the nontorsion hypothesis.
There is therefore an actual original outside root of radius rho>1.

D19 Section3, reproduced below with its complete reciprocal-squarefree-product proof, gives rho^-1<=r.
Its full original-root contribution implies

    m=sum_i log max(1,|alpha_i|)>=log rho
      >=-log r=-log(1-a)>=a.

The last inequality follows by integrating1/(1-x)>=1 on0<=x<=a.
It has no desired uniform gap as a premise.
Substituting the CERTIFIED lower bound eta=a into the complete D19 Section6 argument gives exactly N_* and E_(N_*-1)<=1/4.
By the definition of a finite-packet infimum a rational packet has energy strictly below1/2, without an attainment assertion.
This additional bridge is a new actual C assembly, authored by root and requiring the separate extraction review; the original D19 author's freeze and its whole-review scope remain unchanged.

## Effective coefficient bounds for the integer capacity escape window

Date: 2026-10-12.
Human author Yin; root AI author work on G0001.
This responsible draft quantifies the exact C18 root-block remainder using degree and coefficient height.
Author development only; no native mathematical program or new execution allowance.
The unrestricted Lehmer contract remains unresolved.

<a id="effective-capacity-reuse"></a>
## 1. Question, exact reuse and scope

The adopted [C18 capacity theorem](Yin_C_G0018_v1.md#statement) proves a fixed-input determinant rate and a local original-root block asymptotic, with its complete proof at [the block calculation](Yin_C_G0018_v1.md#integer-capacity-gram-rate-and-conditioning).
Its proof explicitly pays radial gaps, circle-phase separation and block conditioning, but leaves their convergence modulus input-dependent.
The present question is to bound those costs directly by ORIGINAL degree and integral coefficient height, allowing circle roots.
This is a finite effective refinement, not a degree-linear uniform-gap theorem.

Before the present proof, root read that complete C18 calculation, its finite capacity inequality, the [Smy08 discriminant/separation unit](../audits/literature/Smy08/Yin_U003.md#smy08-discriminant-separation), [L144's Salem degree-and-measure separation argument](../ledger/Yin_L_G0144_v1.md#degree-measure-separation-bound) and the already retained L4/L241 Gram/cost comparisons.
Local targeted searches found no explicit coefficient-only modulus for THIS integer-value complementary capacity.
Those older separation and Gram mechanisms are credited; no novelty or priority is inferred from this bounded search.
All estimates newly needed below are proved locally.
In particular no uninspected root-separation theorem, strong Szego theorem or Cauchy determinant formula is invoked.

Throughout P is an ACTUAL monic irreducible nontorsion integer-unit polynomial, of original degree d>=2, with H=max_j|p_j|>=1.
The order is O_0=Z[alpha].
The exact C16/C18 admissible domain uses finite RATIONAL coefficient packets, positive normalized RATIONAL final weights, NONZERO actual integral residues, and every aggregate positive lag zero in allowed window[0,T].
The formal-real class retains the same full integer remainder condition and has the same infimum.
We use C18's already adopted finite inequality, which relies on the exact adopted C17 strong duality; C16 weak duality alone is insufficient for its upper bound.
No restriction to unit residues or a fixed norm inventory is introduced.

<a id="effective-capacity-statement"></a>
## 2. Explicit coefficient-dependent bounds

Put

    R=H+1,
    b=d(2d-1)-1,
    s=(2R)^(-b),
    a=s/(R+1),  r=1-a,
    lambda=s^(d(d-1))*[(1-r^2)/d]^(d-1),
    B=2d(2R)^(d-1)/lambda.                         (1)

All are explicit positive RATIONAL constants, with 0<s<=1, 0<a<1, 0<r<1 and 0<lambda<=1.
They depend on d,H only.
Let

    N_0=ceil max{2,4d/(lambda*s),
                  4d^2/(lambda^2*a^2),
                  16d/(lambda*a^2)}.              (2)

Let c be the number of ALL original roots of P on the unit circle, m the TOTAL logarithmic Mahler measure, N=T+1 and D_T=det(A_T A_T^T) for the actual power-basis remainder matrix.
The following bounds hold for EVERY N>=N_0:

    D_T >= (lambda/2)^d N^c exp(2Tm)/|disc P|,

    exp(-2Tm/d)<=E_T
       <=min{1, B N^(1-c/d) exp(-2Tm/d)},           (3)

and consequently

    0<=m-[-d/(2T)]log E_T
       <=[d log B+(d-c)log N]/(2T).                (4)

This is an effective degree-and-COEFFICIENT-height modulus for C18's exact capacity rate, including circle zeros of P(U).
The capacity is an infimum; no optimizer or bounded q/M is inferred.

If 0<eta<=m is a supplied CERTIFIED lower bound, define

    N_esc=ceil max{N_0,2B R^2 d^2/eta^2}.          (5)

At the allowed window T=N_esc-1, one has E_T<=1/4 and there exists a finite rational admissible packet with energy STRICTLY below1/2.
The assertion gives an explicit window and existence, not its rational coefficients/weights or a native construction algorithm.
The constants may be extremely large; no bound T<=C*d independent of d,H,eta is asserted.
A near-one sequence requires eta to tend to zero, so this result does not supply the missing uniform Lehmer gate.

For each N>=N_0 a rational packet may also be chosen with energy less than twice the positive upper expression in(3).
Its weighted normalized log-norm income Lambda satisfies the explicit bound

    0<=Lambda<=[log(2B)]/2
                    +(d-c)log N/(2d).             (6)

All actual coefficient denominators, final-weight denominators, individual norm sizes and packet size remain unbounded by this statement.
The complete original norm/resultant and width conventions are preserved in Section7.

<a id="coefficient-root-separation-proof"></a>
## 3. Elementary root bounds and reciprocal separation

Write p_0=+/-1 and P^#(t)=p_0 t^d P(t^-1).
It is monic, integral and irreducible of degree d, has the same coefficient height H, and has exactly the inverses of P's roots.
Irreducibility follows by reversing any proposed nontrivial factorization.
Either P^#=P, or their irreducibility makes them coprime over Q.
Define Q=P in the first case and Q=P P^# in the second.
Thus Q is a monic, integral, SEPARABLE polynomial of degree n<=2d, and its root set contains every original root and its inverse.
Real coefficients also retain conjugates.

For any root z of either monic factor, if |z|>1 then

    |z|^d<=H sum_(j=0)^(d-1)|z|^j
             <H |z|^d/(|z|-1).

Hence |z|<H+1=R; all roots of Q are bounded by R.
Reciprocal closure also gives |z|>=1/R.
Since the nonzero integer discriminant of Q has absolute value at least1, and every pairwise root distance is at most2R, a selected distinct pair z,w satisfies

    1<=|disc Q|
       <=|z-w|^2(2R)^(n(n-1)-2).

Therefore |z-w|>=(2R)^(-(n(n-1)/2-1))>=s.
This crude direct bound uses the ORIGINAL polynomial or its coprime reciprocal product; it does not falsely use a zero discriminant when P is reciprocal.
No number-field discriminant or order index is substituted.

For a noncircle original root z of radius rho, z and 1/conjugate(z) are DISTINCT roots of Q.
Thus |rho-rho^-1|>=s.
Let x=min(rho,rho^-1), so 1/R<=x<1.
Then

    s<=x^-1-x=(1-x)(1+x)/x
                    <=(R+1)(1-x).

It follows that x<=1-s/(R+1)=r.
Thus every original inside root and every inverse of an original outside root has modulus at most r.
Within each of those two lists all distinct distances are at least s.
Two distinct original circle roots have chord distance at least s.
These statements cover arbitrary reciprocal and nonreciprocal inputs; circle roots are retained rather than separated radially from the circle.

<a id="effective-kernel-conditioning"></a>
## 4. Quantitative conditioning without a determinant formula

For any list z_1,...,z_l of distinct numbers of modulus at most r and mutual distances at least s, consider the Hermitian kernel

    K=(1/(1-z_i conjugate(z_j)))_(i,j=1)^l.

It is the convergent sum of positive semidefinite rank-one matrices of powers.
Its first l terms form V_l V_l^*, with V_l=(z_i^j)_(0<=j<l).
Therefore K>=V_l V_l^*>0, and

    det K>=|det V_l|^2
              =product_(i<j)|z_i-z_j|^2
              >=s^(l(l-1)),
    trace K<=l/(1-r^2).

The other l-1 eigenvalues are each at most trace K, so

    lambda_min(K)>=det K/(trace K)^(l-1)
        >=s^(l(l-1))*[(1-r^2)/l]^(l-1)
        >=s^(d(d-1))*[(1-r^2)/d]^(d-1)=lambda.      (7)

The last comparison uses l<=d and both s and(1-r^2)/d in(0,1].
For an empty block there is no eigenvalue to bound.
The intervening circle identity block has minimum eigenvalue1>=lambda.

Apply(7) to the C18 inside kernel K_I and outside inverse kernel K_O.
All their nodes satisfy Section3, so the complete limit block K_*=diag(K_I,I_c,K_O) satisfies K_*>=lambda I_d.
The proof does not hide a poorly conditioned Vandermonde constant in O_P(1).

<a id="effective-root-block-remainder"></a>
## 5. Explicit all-block error and its rational threshold

C18 gives the EXACT original-root matrix H_T=V A_T A_T^T V^*, with entries sum_(k=0)^T alpha_i^k conjugate(alpha_j)^k and determinant |disc P| D_T.
Its complex diagonal scaling R_T is1 on inside roots, N^-1/2 on circle roots and alpha_i^-T on outside roots.
Set Z_T=R_T H_T R_T^*.
The exact same scaling, including the outside phases, is used here.

Every entry of Z_T-K_* has absolute value at most

    e_N=max{r^(2N)/(1-r^2),
             2/(N*s), 1/(a sqrt N), N r^(N-1)}.    (8)

Indeed the two same-side off-circle blocks have geometric tails bounded by the first expression.
Circle diagonal errors are zero; for distinct circle roots the geometric sum has numerator at most2 and denominator |1-alpha_i conjugate(alpha_j)|=|alpha_i-alpha_j|>=s, giving the second expression.
Inside-circle entries sum a series with ratio modulus<=r and carry N^-1/2.
Outside-circle entries, reindexed after the complex scaling, obey the same bound, giving the third expression.
In an inside-outside entry, its k-th summand has modulus at most r^k r^(T-k)=r^T, so the whole sum is at most N r^T.
This argument covers the resonant product alpha_i conjugate(alpha_j)=1 without division by zero.
Hermitian transposes cover the reverse blocks.

For N>=2, use r=1-a<=exp(-a).
The elementary exponential series gives exp(x)>=x and exp(x)>=x^2/2 for x>0.
Since 1-r^2>=a,

    r^(2N)/(1-r^2)<=1/(2a^2 N),
    N r^(N-1)<=2N/[a^2(N-1)^2]<=8/(a^2 N).        (9)

The four thresholds in(2) now make EACH expression in(8) at most lambda/(2d).
For the first, N>=16d/(lambda a^2) is more than sufficient; the other three use their corresponding displayed thresholds.
Thus every row sum is at most lambda/2.
For the Hermitian error its operator norm is bounded by its maximum absolute row sum, so

    Z_T>=K_*-lambda I_d/2>=lambda I_d/2.

Taking determinants and using |det R_T|^2=N^-c exp(-2Tm) gives the first bound in(3), with ALL original roots and the entire polynomial discriminant retained.

<a id="effective-capacity-transfer-and-escape"></a>
## 6. Transfer to energy and a certified escape window

The already adopted C18 finite inequality gives E_T<=C_d N/D_T^(1/d), with C_d=4/kappa_d^(2/d).
The cube[-1/sqrt d,1/sqrt d]^d lies in the unit ball, hence kappa_d>=(2/sqrt d)^d and C_d<=d.
Also |disc P|<= (2R)^(d(d-1)) by its full root product.
Substitute the first bound in(3) to obtain

    E_T<= (2d/lambda)(2R)^(d-1)
                    N^(1-c/d) exp(-2Tm/d).

This is the upper expression in(3).
The constant packet supplies E_T<=1, and C18's full-norm inequality supplies its positive lower expression.
Taking logarithms gives(4); T=N-1>0 by(2).
Equality of rational/formal-real infima is the already adopted C16 domain result, so no irrational field norm is invoked.

For(5), let u=2m/d>0.
Each original root has radius at most R, so m<=d log R and exp(u)<=R^2.
For N>=2, and using exp(uN)>=(uN)^2/2,

    B N^(1-c/d)exp[-u(N-1)]
       <=B exp(u) N exp(-uN)
       <=2B R^2/(u^2 N)
        =B R^2 d^2/(2m^2 N).

The second threshold in(5) makes this at most eta^2/(4m^2)<=1/4.
The first threshold retains the entire conditioning proof.
The definition of the positive finite-packet infimum then supplies a rational admissible packet with energy strictly below1/2; no attainment theorem or finite enumeration is needed.

<a id="effective-capacity-full-arithmetic-costs"></a>
## 7. Original arithmetic and weighted norm costs

For every selected rational packet, let q be its ACTUAL least common coefficient denominator, F_b=q f_b its integer numerators, omega_b its final positive normalized rational weights, and M their ACTUAL least common denominator.
Every u_b=f_b(alpha) is a nonzero O_0 integer, so all original d embeddings give

    Res(P,F_b)=q^d Norm_(K/Q)(u_b)!=0,
    Lambda=(1/d)sum_b omega_b log|Norm(u_b)|>=0.

The direct generic-monic C10 inequality, reused exactly in C18, gives Lambda<=log E/2+Tm/d after cancelling the SAME log q from log q+Lambda and log(q^2 E)/2.
No q, numerator content or norm factor is dropped before that cancellation.
Choosing a finite rational packet with energy strictly below twice the upper expression in(3) gives(6).
The full copied signed product remains product_b Res(P,F_b)^(M omega_b); this draft supplies no individual formula for a not-yet-constructed packet or bounded M.
A common Laurent shift multiplies each residue by an actual unit power of alpha, retains coefficient energy and width, and contributes its actual original norm sign to each copied factor.

The coefficient height H in(1) is that of the ORIGINAL minimal P, not the auxiliary F_b.
No maximal-order replacement, degree of alpha^k, trace-subfield norm or normalized matrix trace enters any estimate.
The scalar single-Haar determinant convention remains C18's canonical trace tau(1)=1.

<a id="effective-capacity-limits-and-self-check"></a>
## 8. Author self-check and limits

Root reconstructed the reciprocal squarefree-product guard, original and inverse root bounds, nonzero integer discriminant argument, radial versus chord separation, finite Vandermonde kernel conditioning, every block-error orientation and resonance, row-norm threshold, determinant scaling and entire C18 inequality transfer.
The escape uses only a supplied certified positive eta, and the packet-existence step uses an infimum without claiming attainment.
All formulas are theoretical; no root computation, numerical determinant, program, J, scan or source acquisition occurred.

The constants expose how coefficient height couples arithmetic separation with analytic convergence.
They are deliberately crude and can grow extremely rapidly with degree.
This is a finite effective version of the existing fixed-input capacity formula, with no unrestricted gap, sharp convergence estimate, q/M bound or degree-linear uniform escape.
It does not erase C21's first-window obstruction, nor assume the desired Lehmer gap through a hidden eta.
Separate whole noncontributor review and exact Claim organization remain pending.

<a id="effective-capacity-entire-author-freeze"></a>
## 9. Entire author freeze

2026-10-11T19:42.
Complete Sections1--9, statement and equations(1)--(9) are frozen for separate whole noncontributor review.
Root is the substantive author and cannot independently review this argument.
This is author self-review only.
G0001 remains unrestrictedly unresolved.


## Registration and preservation operation

2026-10-11T19:48: retain the COMPLETE2026-10-11T19:42 original D19 author freeze and add the explicitly selected coefficient-only consequence locally in this physical Claim.
The separate reviewer will inspect the actual summary, new bridge, full retained proof and current dependency use.
Retire the original working address only after full preservation and incoming-reference maintenance.
No native program, new execution allowance or Task completion accompanies this registration.
