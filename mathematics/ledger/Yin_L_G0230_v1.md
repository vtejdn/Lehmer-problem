---
author: Yin
---

# Complete companion cost and the minimum-rank tradeoff

The complete current mathematical home is [C549](../claims/Yin_C_G0549_v1.md#statement), adopted at 2026-10-22T21:00 after the [actual isolated whole review](../audits/reviews/Yin_R_G0776_v1.md#current-integral-rank-and-companion); the earlier18:52 SELF adoption remains in its decision history.
The original dated mathematics and frozen input below remain the actual inputs of R129; the original whole relationship declaration remains missing rather than silently reclassified.

Date: 2026-10-10.
The original2026-10-10 coordinating account adopted this restricted result after its separately organized noncontributor review, at that original scope.
This is fixed mathematical retention, not Task completion or acceptance of an unrestricted Claim.

<a id="companion-tradeoff-fixed-scope"></a>
## Original adopted scope and fixed review input

A general full reciprocal trace bound and the signed-versus-absolute cycle inequality give an absolute-companion Mahler lower bound for every real unitriangular matrix.
Together with the existing integral energy bound this proves that every rank7 realization of Phi2 P6 has a complete cover cost strictly greater than the retained rank8 realization.
An explicit integral rank7 representative improves height4/energy87 to height3/energy41 and decreases its absolute Salem root from 600--602 to 80--81.
The full rank14 cover, both factors, all mutation steps and exact integer congruences are retained in J50 with complete read-only replay and a different determinant verification.
No optimal cost over other ranks or unrestricted varying-input realization is asserted.


<a id="complete-retained-proof-and-review"></a>
## Complete original author proof and dated review input

## Full companion cost after minimum-rank integral realization

Date: 2026-10-10.
Starting question: Continue L226's actual integral rank7 realization of Phi2 P6.
Seek a substantially smaller complete absolute-companion Mahler cost or a reusable cost constraint, and investigate a route to varying reciprocal inputs.
Use changed exact constructions or a predeclared bounded experiment rather than another minimum-rank existence search.
All original, companion and cover factors, lattice conditions and costs must remain.


### Reuse, exact domain and the predeclared experiment

The adopted [L226 minimum-rank realization](Yin_L_G0226_v1.md#integral-rank-seven-fixed-scope) supplies an actual integral upper-unitriangular V of rank7 with p_V(t)=det(tV+V^T)=F(t)=(t+1)P6(t), where P6=t^6-t^5-t^3-t+1.
Its height4 and squared-entry sum E=87 do not measure its complete absolute-companion cost: the latter is log lambda with 600<lambda<602.
Its integer root basis lies in G0=[2] direct-sum U^3, U=[[0,1],[1,0]].
The rank8 realization retained in [L210](Yin_L_G0210_v1.md#prescribed-six-degree-padding-comparison) has a different neutral-factor cost and much smaller complete cover measure.
Neither is an optimized rank7 theorem.

The [D9 adjacent mutation](../claims/Yin_C_G0002_v1.md#mutation-and-energy) already proves that congruence by the identity outside two adjacent coordinates and by Q_a=[[0,1],[1,-a]] within them, where a=V_(i,i+1), preserves integral upper-unitriangular form and the entire p_V.
Its inverse uses [[-a,1],[1,0]] with the current adjacent entry.
We reuse this result, tracking the full integer root basis, rather than rediscovering existence or changing the target coefficients.
The [L185 positive absolute-cover theorem](Yin_L_G0185_v1.md#positive-absolute-cover-cost), its complete review, and its exact interacting-triangle family were read: they provide a universal strictly positive lower bound and examples of actual cost reductions, but do not optimize this prescribed input.
The local inputs suffice for the present finite optimization and certificate; no new external theorem is adopted.

Here V^- denotes the matrix with diagonal1 and strict-upper entries -|V_ij|.
The discovery objective is the entire m(p_(V^-)), computed numerically from its exact reciprocal polynomial.
For degree7, write p=(t+1)t^3 q(t+t^-1), where q is a real cubic.
Every trace root contributes log max(1,|z|,|z|^-1), with z+z^-1 equal to that root; all three contributions are retained, including nonreal traces.
Energy is only a secondary diagnostic.
Numerical root values select candidates and prove no inequality; a retained improvement requires an exact full-polynomial and root-location certificate.

Before execution, the first experiment is capped at60000 adjacent proposals in30 blocks of2000, using fixed seed20261012.
Each block restarts from the best complete-cost candidate found so far, initially L226's V.
A proposed matrix is rejected if its entry height exceeds6, E exceeds160, or an integer root-basis coordinate exceeds1000000.
Each accepted mutation is recorded with its direction and index.
Selection may use numerical annealing, whose constants will be fixed in the program before the run.
This is a bounded discovery domain, not an exhaustion of the mutation orbit, of all root bases, or of rank7 realizations; a best observed value is not a global or orbit minimum.
Continued programs and their actual outputs belong to the separately allocated J for this round.

<a id="trace-energy-companion-cost-bound"></a>
### 1. A target-dependent lower cost, independent of an optimization run

Let V=I+N be a real upper-unitriangular matrix of rank n>=2, let B=|N| entrywise, and put

    C=-V^-1 V^T, tau=tr C, E=sum_(i<j) N_ij^2,
    C_abs=-(I-B)^-1(I-B^T), T=tr C_abs,
    m_abs=m(det(t(I-B)+(I-B^T))).                    (1)

The logarithmic Mahler measure here includes the whole monic polynomial, with multiplicities.
Finite geometric expansion gives

    tau=-n+E+S,
    S=sum_(k=2)^(n-1) (-1)^(k+1) tr(N^k N^T),
    T=-n+E+L,
    L=sum_(k=2)^(n-1) tr(B^k B^T) >= |S|.            (2)

Indeed all traces tr(N^k) for k>=1 vanish, the k=1 mixed term is E, and entrywise triangle inequalities give |tr(N^k N^T)|<=tr(B^k B^T).
Thus the strengthening of D9's T>=E-n is

    T >= E-n+|tau-E+n|.                              (3)

This uses the actual trace coefficient of the prescribed original polynomial; it is not an assumption that the companion is isospectral to V.

Here is a reciprocal refinement of the root-sum bound used in D9.
For any real monic reciprocal polynomial p of degree n and constant1, put m=m(p), and let T_p be the sum of all roots.
If n is even, reciprocal roots can be paired as z,z^-1.
If n is odd, first remove one forced root -1, and then pair the remaining roots.
Repeated roots at1 or-1 can also be paired; equivalently the even-degree residual polynomial is t^r q(t+t^-1).
Select |z|>=1 in every pair and put u=log|z|>=0.
The pair contributes at most2cosh u to the real part of the root sum and contributes exactly u to m.
For a,b>=0,

    cosh(a+b)+1-cosh a-cosh b
      =(cosh a-1)(cosh b-1)+sinh a sinh b >=0.

Induction therefore bounds the sum of r such coshes by cosh(sum u)+(r-1).
Writing epsilon=0 for even n and1 for odd n gives

    T_p <= 2cosh m+n-2-2epsilon.                    (4)

No assumption that every trace root is real or that there is only one expanding pair occurs in this estimate.
Apply it to the complete absolute polynomial, which is reciprocal by determinant transposition.
Equations(3)--(4) imply the reusable cost constraint

    m_abs >= arcosh(max{1,
      (E-2n+2+2epsilon+|tau-E+n|)/2}).               (5)

In particular, any class with a proved lower energy and prescribed trace can use (5), provided the energy dependence on its admissible range is handled explicitly.
It is a necessary cost inequality, not a method of constructing presentations.

For every integral rank7 realization of F=Phi2 P6, tau=0 and the separately reviewed [L210 signature theorem](Yin_L_G0210_v1.md#signature-energy-fixed-scope) gives E>=13.
Hence E-7>0, and

    T>=2E-14>=12,
    m_abs>=arcosh((2E-17)/2)>=arcosh(9/2),
    M_abs>=Lambda_*=(9+sqrt77)/2.                    (6)

This holds for all such rank7 matrices, not just the L226 lattice or the present mutation orbit.
In contrast, the adopted rank8 realization has entire polynomial Phi2^2 P6 and absolute measure exactly log beta, with beta in(3/2,151/100).
Since Lambda_*>8>beta, the corresponding complete signed covers satisfy

    rank14, minimum neutral padding:
      m_cover>=log beta+log Lambda_*>2log beta;
    retained rank16 control:
      m_cover=2log beta.                             (7)

Thus the smaller neutral-factor degree provably forces a larger full absolute-cover cost in this actual input.
This compares all minimum-rank realizations with one achieved further-stabilized realization.
It is not a global optimality assertion for rank8, for arbitrary stabilization, or for other signed-cover constructions.
In particular, energy alone is not a Mahler objective; the exact target trace and reciprocal-root argument are indispensable to this deduction.

<a id="reduced-rank-seven-companion-certificate"></a>
### 2. An achieved lower-cost presentation in the original integer orbit

The following explicit matrix has all seven diagonal entries1:

    V1 =
    [1 -2  0 -2  1 -2 -1]
    [0  1  0  0 -3 -1  2]
    [0  0  1 -1 -1 -1 -2]
    [0  0  0  1  0  2  1]
    [0  0  0  0  1  1  0]
    [0  0  0  0  0  1  0]
    [0  0  0  0  0  0  1].                           (8)

Its exact integer basis in G0=[2] direct-sum U^3 is

    Q1 =
    [-12  17 -6  11 -1  4  4]
    [  1  -3  2  -2 -1 -1 -2]
    [ -3   2 -2   4  2  3  1]
    [ -1  -2 -2   2  3  2  1]
    [ -7  11 -4   7  0  3  3]
    [ 21 -26 13 -21 -2 -9 -8]
    [ -7  10 -3   6 -1  2  2].                       (9)

Direct integer multiplication gives det Q1=1 and Q1^T G0 Q1=V1+V1^T.
Thus the symmetric determinant is-2, inertia is(4,3), and every displayed column is an actual norm-two integral root; no rational change of lattice is used.
Direct polynomial expansion gives

    p_(V1)=t^7-t^5-t^4-t^3-t^2+1=Phi2 P6,
    E(V1)=41, H(V1)=3.                               (10)

One short coefficient verification, in addition to the full determinant certificate, uses C1=-V1^-1 V1^T.
Multiplication gives tr C1=0 and tr(C1^2)=2.
Reciprocity fixes the coefficient pairs, Newton's first two identities fix A=0,D=-1, and p_(V1)(1)=det G0=-2 then fixes H=-1 in the notation p=t^7+A t^6+D t^5+H t^4+H t^3+D t^2+A t+1.
This verifies all coefficients, not only a target factor.

The responsible [J50](../computations/programs/Yin_J_G0050/readme.md) retains a1539-step adjacent mutation word from the adopted L226 matrix to(8).
Its integer-only replay constructs a unimodular T with T^T V_old T=V1 and Q_old T=Q1, det T=-1.
The replay checks each full congruence and final basis, and records maximum intermediate energy160, height6 and root-basis coordinate214.
The long word is evidence of membership in that actual mutation orbit; the explicit matrices and identities(8)--(10) prove the realization without any conjecture about orbit connectivity.

The complete absolute determinant is

    p_(V1^-)=t^7-80t^6-5t^5-7t^4-7t^3-5t^2-80t+1
             =(t+1) R1(t),
    R1=t^6-81t^5+76t^4-83t^3+76t^2-81t+1,
    R1=t^3 q(t+t^-1),
    q(x)=x^3-81x^2+73x+79.                           (11)

The values q(-1),q(0),q(1),q(2),q(80),q(81) are respectively

    -76,79,72,-91,-481,5992.                         (12)

Thus all three trace roots are real, one in each of(-1,0),(1,2),(80,81).
The first two lift to four unit-circle roots.
For the third root xi, the expanding root lambda1=(xi+sqrt(xi^2-4))/2 is real.
Moreover q(80+1/80)=-205856079/512000<0, so xi>80+1/80 and

    80<lambda1<81,     m(p_(V1^-))=log lambda1.       (13)

For the root comparison at80+1/80, the other two roots lie below2; on(2,infinity) the sign of the monic cubic is the sign of x-xi.
The upper bound follows from lambda1<xi<81.
The exact residues q(0)...,q(4) modulo5 are4,2,4,1,4, so q is irreducible over Q.
The field Q(xi) is totally real, and one of its embeddings takes xi into(-1,0), making xi^2-4 negative.
Consequently xi^2-4 is not a square in that field.
The quadratic lift has degree6 over Q; hence R1 is irreducible and is a Salem polynomial.
Irreducibility is not used to discard a factor: (11) retains the entire companion even without this additional identification.

Use the same literal two-sheet signed-cover rule as D9: an upper entry a<=0 becomes a I2, while a>0 becomes [[0,-a],[-a,0]], and every diagonal block is I2.
The equal and opposite sheet subspaces give the full factorization

    p_W=p_(V1) p_(V1^-)=Phi2^2 P6 R1,
    rank W=14, H(W)=3, E(W)=82,
    m(p_W)=log beta+log lambda1.                     (14)

Its complete descending coefficient vector is

    [1,-80,-6,72,77,86,19,26,19,86,77,72,-6,-80,1].   (15)

J50 independently builds this actual14-by14 integral matrix and evaluates its pencil determinant at all15 integers from-7 to7.
Both sides have degree at most14, so these exact comparisons also certify the whole product polynomial.
There are exactly two explicitly retained Phi2 factors in(14).
Relative to L226's achieved lambda_old>600, the actual full logarithmic cover cost drops by more than log(600/81)=log(200/27), while the original polynomial and padding stay fixed.
This is a certified achieved improvement, not the infimum in the mutation orbit or among all minimum-rank matrices.

### 3. Executed scope, comparison and next mechanism

The predeclared run made all60000 proposals with seed20261012.
Of these,13331 exceeded the matrix height/energy limits, zero exceeded the root-coordinate limit, and46669 received exact coefficient computation;27786 proposals were accepted by the discovery walk.
It encountered14036 distinct absolute polynomials.
Every accepted mutation was appended to the current in-memory word; the saved evidence retains the best candidate's complete word, not all discarded walk trajectories.
The best reported candidate occurred at proposal41434.
The numerical complete companion measures were approximately6.3988228691 initially and4.3828207716 at(8); these are discovery diagnostics, superseded for the proved comparison by the exact intervals600<lambda_old<602 and80<lambda1<81.
The fixed annealing temperature decreases linearly within each block from0.8 toward0.015.
No statement about uniform sampling, global frequency, coverage of the capped matrix box or global cost optimality follows.

In the exact certificate, the signed cycle terms S from(2) are(-22,-12,0,0,0), and the corresponding absolute terms are(34,12,0,0,0).
Thus tau=-7+41-34=0 and T=-7+41+46=80, explicitly illustrating the extra absolute charge created by the cancellations required by the target.
For this achieved E=41, (6) itself gives m_abs>=arcosh(65/2), whereas the all-presentation E>=13 bound is arcosh(9/2).
A better energy presentation could lower the former estimate; it cannot evade the latter within rank7.

The useful changed conclusion is twofold: actual mutation can remove a substantial part of the cost of a poor minimum-rank representative, while the general trace/energy bound proves that optimizing within minimum rank cannot reach the inexpensive already-realized stabilized control.
This makes the neutral degree a genuine optimization variable, with its full original and companion factors charged.
For varying reciprocal inputs, (5) supplies a reusable necessary-cost test once trace, dimension and a valid energy obstruction are known.
It gives neither arbitrary integral realization nor a uniform small-measure upper-cost construction.
A discriminating next question is whether a controlled extra cyclotomic factor can systematically remove a positive trace/energy cost floor for a varying family, while keeping the complete cover cost comparable to the original measure.
No new existence search or larger sample is needed to state that remaining issue.

### 4. Contributions, self-check and current status

The coordinating agent assigned the broad cost/coverage question, allocated D97/J50, and supplied the shared execution gate.
The authoring orbit agent derived(2)--(7), designed the bounded mutation objective, implemented the discovery and separate exact certificate, and wrote the construction and all cost proofs here.
D9's mutation/cover formulas, L185's positive-cost mechanism, L210's signature/energy and rank8 control, and L226's initial realization are explicitly reused at their retained scopes.
No external novelty claim is made.
The coordinating agent received substantive checkpoints, so a subsequent review need not be blind; no other agent has contributed a derivation to this draft at the time of the author freeze.

The complete original author SELF account is retained in [R738](../audits/reviews/Yin_R_G0738_v1.md#original-g230-author-self-finding), with the actual original checking scope and date precision.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0776_v1.md#companion-cost-complete-independent-review), with its original inspected scope and relationship.
