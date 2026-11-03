---
author: Yin
---

# Complete constructive integral Gram realizations and full absolute-cover spectra

The complete necessary original D60 proof is retained from [L191](../ledger/Yin_L_G0191_v1.md#retained-integral-gram-realization-proof).
The structural author supplied every new Gram/construction/example deduction; the coordinator assigned the broader question and supplied none of those derivations.
The original entire whole finding retains its scope and unknown initial independent-review relationship in [R669's later comparison of L191 and R669](../audits/reviews/Yin_R_G0669_v1.md#l191-r90-and-r812).
Reading fixed upstream interfaces is not target contribution; generic shared context does not establish complete initial isolation or actual prior target mathematics.
The exact original [listed author checks](../audits/reviews/Yin_R_G0090_v1.md#integral-gram-original-author-check-finding) remain SELF at their actual scope.
All needed complete local determinant, stabilization and absolute-cover proofs are reused at their adequate homes.
The already consumed k4 rank6/rank12 control is made fully explicit with every factor and cost.
No source/PDF reading, mathematical producer/native run, program/J or research Task/E is added.

## Statement

Let g>=1 be an integer and A=(a_ij) any symmetric integral g by g matrix satisfying

    a_ii>=sum_(j!=i)|a_ij| for every i.

Put c_ij=|a_ij| for i<j and delta_i=a_ii-sum_(j!=i)|a_ij|>=0.
For each integer N>=0 let s4(N) be its base-four digit sum, s4(0)=0, and define

    r0=sum_(i<j)s4(c_ij)+sum_i s4(delta_i),
    r=max(g,r0).

There is an explicit integer r by g matrix B with

    B^T B=A,
    sum_(u,i)B_ui^2=tr A.

For every positive c_ij=sum_k d_k4^k insert d_k copies of2^k(e_i+sign(a_ij)e_j).
For each positive residual delta_i use its corresponding2^k e_i rows.
Append zero rows if r0<g.
This constructs exactly r0 nonzero rows and r-r0 zero rows.
It proves positive semidefiniteness without assuming a converse for arbitrary integer positive-semidefinite matrices.

For A!=0 let M be the largest positive component among the c_ij,delta_i and let N count those positive components.
Then

    N<=g(g+1)/2,
    r0<=3N(1+floor(log_4 M)),
    max|B_ui|<=sqrt M.

For A=0 use r=g,B=0 separately, without log zero.
For this specifically constructed signed sparse-row B, not an arbitrary factorization, the matrix A# with diagonal a_ii and off-diagonal|a_ij| satisfies

    |B|^T|B|=A#.

Thus A# is also positive semidefinite.

Define the actual integral upper-unitriangular matrix and its full determinant by

    V=[[I_r,-B],[0,I_g]],
    p_V(t)=det(tV+V^T),
    P_A(t)=t^g det(((t+t^-1)+2)I_g-A).

Then P_A is monic reciprocal integral of degree2g and constant term one, and

    p_V=(t+1)^(r-g)P_A,
    dim V=r+g,E(V)=sum_(i<j)V_ij^2=tr A,
    A!=0 => max|V_ij|<=max(1,sqrt M).

The exact neutral factor is Phi2^(r-g) with nonnegative exponent.
The polynomial identity holds at t=0,-1 as well; no scalar or exceptional-root factor is deleted.
For the all-negative absolute presentation Vminus, replace the off-diagonal block by-|B|.
Its entire polynomial is

    p_(Vminus)=(t+1)^(r-g)P_(A#).

Let F(lambda)=0 for0<=lambda<=4 and F(lambda)=arcosh((lambda-2)/2) for lambda>4.
If lambda_i and mu_i are all eigenvalues of A and A#, respectively, counted with multiplicity, the full unnormalized logarithmic measures are

    m(p_V)=sum_i F(lambda_i),
    m(p_(Vminus))=sum_i F(mu_i).

Both eigenvalue lists are nonnegative by their explicit Gram decompositions.
The repeated endpoint quadratics at lambda=0,4 also contribute zero.
The exact two-sheet cover W has p_W=p_V p_(Vminus), with full measure the sum of these two spectral sums.
This is its complete cost, not just its largest root.

A target is sufficiently realized only when its actual trace polynomial is exhibited as det((u+2)I-A) for such an integer A.
No such A is proved for all reciprocal targets or inferred from small measure.
Every root trace in this subclass is real and at least-2.
The exact degree-ten nonreal-trace target retained in C412 cannot occur as a factor even after cyclotomic multiplication within this matrix class.
This excludes no arbitrary other Seifert/matrix class.

For every integer k>=4 take A_k=[[1,1],[1,k]], with h=s4(k-1).
The construction has r0=r=1+h and nonnegative B with row(1,1) and the base-four coordinate rows(0,2^j) for k-1.
Then

    P_k=t^4+(3-k)(t^3+t^2+t)+1,
    Q_k(u)=u^2+(3-k)u+1-k,
    P_k=t^2Q_k(t+t^-1),
    p_(V_k)=Phi2^(h-1)P_k,
    dim V_k=3+h<=3+3(1+floor(log_4(k-1))),
    max|V_ij|<=sqrt(k-1),E(V_k)=k+1.

Every P_k is an irreducible degree-four Salem polynomial.
Its trace roots have one in(-2,0) and one greater than2, with

    u_+=(k-3+sqrt((k-1)^2+4))/2,
    m(P_k)=arcosh(u_+/2).

These measures grow approximately log k and do not form a near-one family.
The nonnegative B gives V_k=V_kminus, so the exact absolute cover has total measure2m(P_k), with extra cost m(P_k) and no optimality assertion.

At k=4, B has rows(1,1),(0,1),(0,1),(0,1).
The matrix V_4 has rank6,height1,energy5 and full polynomial Phi2^2 P4, where P4=t^4-t^3-t^2-t+1 is the original fixed quartic Salem input.
Its entire literal cover has rank12,height1,energy10, polynomial Phi2^4 P4^2 and measure2log beta4, beta4>1 the expanding root of P4.
Every entry/factor/cost is retained in the explicit mechanism below.
At k=5, B has rows(1,1),(0,2), yielding a rank4 realization of the irreducible quartic itself without a neutral multiplier.

A separate signed control takes

    A=[[4,-1,-1],[-1,4,-1],[-1,-1,4]]=5I_3-J_3,
    A#=[[4,1,1],[1,4,1],[1,1,4]]=3I_3+J_3.

The three difference rows e_i-e_j and two copies of e_i for each i give r=9,g=3, rank V=12, height1 and energy12.
The spectra are(2,5,5) and(6,3,3), so the complete polynomials and costs are

    p_V=Phi2^6(t^2+1)(t^2-3t+1)^2,
    p_(Vminus)=Phi2^6(t^2-4t+1)(t^2-t+1)^2,
    m(p_V)=2arcosh(3/2),
    m(p_(Vminus))=arcosh2<2arcosh(3/2).

Both original and extra costs are positive, and the whole cover costs their sum.
This proves that equality or extra-cost>=original-cost is not a general law, while preserving the positive-cover necessity.
The degree-six target here is reducible and supplies no irreducible comparison by itself.
No optimum, uniform ratio, general reciprocal coverage, near-one cover estimate or unrestricted Mahler gap is asserted.

## Current assessment

[Selected decision](#decision-retained-registration)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T21:18 |
| status | open |
| reason | Retain the complete explicit integer Gram/absolute Gram construction and costs, full block determinant and all spectral measures, irreducible quartic family and exact k4 full-cover comparison, and signed unit-entry cost control with every sufficient-subclass/source/contribution/coverage limitation. Complete actual current whole self-check and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire Gram construction and full cost theorem](#statement) | Entire original D60 necessary reuse/Sections1--4/equations(1)--(16), original Section5 contribution/listed checks and all remaining limits retained separately, plus explicit already consumed k4 full-cover costs: every symmetric integer diagonally dominant g>=1 matrix/nonnegative residual/base-four signed row and zero case/padding/r0-r-M-N/trace-height costs, exact constructed absolute Gram A# and both PSD guards, full block polynomial identity at0/-1/monic reciprocal degree2g/Phi2 exponent/rank/energy/height, complete eigenvalue measures including0/4 and every absolute-cover factor, actual real-trace obstruction without universal reciprocal coverage, every k>=4 quartic trace/real-field irreducibility/Salem classification/explicit measure/row costs and k4/k5 examples, k4 rank6-height1-E5 Phi2^2 P4 and entire rank12-height1-E10 Phi2^4 P4^2 cover, signed r9/g3 rank12 unit-entry control with full original/absolute spectra/factors and strict positive cost comparison. No optimum, near-one family, general Gram integrality/diagonal dominance from small measure, uniform ratio/gap or new source/native/Task execution is asserted. |
| argument | [All necessary original mathematical proofs](#argument) | Entire original D60 necessary reuse/Sections1--4/equations(1)--(16), original Section5 contribution/listed checks and all remaining limits retained separately, plus explicit already consumed k4 full-cover costs: every symmetric integer diagonally dominant g>=1 matrix/nonnegative residual/base-four signed row and zero case/padding/r0-r-M-N/trace-height costs, exact constructed absolute Gram A# and both PSD guards, full block polynomial identity at0/-1/monic reciprocal degree2g/Phi2 exponent/rank/energy/height, complete eigenvalue measures including0/4 and every absolute-cover factor, actual real-trace obstruction without universal reciprocal coverage, every k>=4 quartic trace/real-field irreducibility/Salem classification/explicit measure/row costs and k4/k5 examples, k4 rank6-height1-E5 Phi2^2 P4 and entire rank12-height1-E10 Phi2^4 P4^2 cover, signed r9/g3 rank12 unit-entry control with full original/absolute spectra/factors and strict positive cost comparison. No optimum, near-one family, general Gram integrality/diagonal dominance from small measure, uniform ratio/gap or new source/native/Task execution is asserted. |
| dependency | [Complete rectangular-block trace restriction](Yin_C_G0412_v1.md#sparse-trinomial-auxiliary) | Only arbitrary real rectangular B block-bipartite determinant with every real trace>=-2, and the exact irreducible degree-ten W/nonreal-trace obstruction. No canonical graph or arbitrary Seifert exclusion, pilot decimal or source premise is imported. |
| dependency | [Complete literal signed-cover mechanism](Yin_C_G0002_v1.md#signed-cover-identity) | Integral upper-unitriangular determinant and equal/opposite sheets, full original/absolute product and unnormalized additive measure; every nonzero strict entry has exactly two equal-magnitude copies, retaining rank/height/doubled-energy for the explicit k4 control. |
| dependency | [Complete prior base-four stabilization and its limits](Yin_C_G0455_v1.md#compressed-weighted-arm-realization) | Only already explicit base-four square encoding/row-size and growing-measure weighted construction, with no general higher-degree realization implication. The changed signed Gram factorization is fully proved locally. |
| dependency | [Complete positive absolute-cover necessity](Yin_C_G0440_v2.md#positive-absolute-cover-cost) | Strictly positive added cost when original measure is positive; no extra-cost>=original-cost, uniform upper ratio or optimized representation is presumed. |
| support | [Original complete fixed quartic input](Yin_C_G0396_v1.md#quartic-infinite-core-theorem) | Only the same irreducible Salem polynomial P4 and its fixed input identity. Its orbit/core/native certificates are unrelated to this direct Gram construction and are not rerun. |

## Complete retained argument

<a id="argument"></a>
<a id="retained-integral-gram-realization-proof"></a>
<a id="integral-gram-realization-fixed-scope"></a>

### Reuse and exact scope

The [complete stabilization theorem](Yin_C_G0455_v1.md#cyclotomic-stabilization-fixed-scope) handles endpoint costs and a quadratic family.
Its endpoint repair is not a general sufficiency theorem.
The [complete block-bipartite calculation](Yin_C_G0412_v1.md#sparse-trinomial-auxiliary), in its subsection on the Pisot obstruction, already computes the determinant for arbitrary real rectangular B and proves its real-trace restriction.
The [complete signed-cover identity](Yin_C_G0002_v1.md#signed-cover-identity) and [complete positive-cover cost theorem](Yin_C_G0440_v2.md#positive-absolute-cover-cost) retain their full factors and exact scopes.

The changed input here is an explicit integer Gram construction: a testable class of trace matrices is factored by integer rows with controlled row count and coefficients.
This gives actual integral upper-unitriangular realizations of reciprocal polynomials of arbitrary even degree, using only a stated power of Phi2 as neutral multiplier.
The absolute-cover polynomial is also computed in full.
An irreducible degree-four family and a separate signed degree-six cost control make the distinction concrete.

The sufficient hypothesis is symmetric integral diagonal dominance with nonnegative residual diagonal.
It is not assumed for every reciprocal target, and no change of integral basis establishing it in general is supplied.
In particular the positive-semidefinite, real-trace restriction retained in C412 remains in force even under arbitrary cyclotomic multiplication.
This round does not recycle that restriction as a new theorem or claim unrestricted coverage.

<a id="constructive-integral-gram-completion"></a>
### 1. Explicit integer Gram factorization with row and height costs

Let A=(a_ij) be a symmetric integral g by g matrix, g>=1, satisfying

    a_ii >= sum_(j!=i)|a_ij| for each i.                         (1)

Put c_ij=|a_ij| for i<j and delta_i=a_ii-sum_(j!=i)|a_ij|, so every delta_i is a nonnegative integer.
For a nonnegative integer N let s4(N) be the sum of its base-four digits, with s4(0)=0.
Define

    r0=sum_(i<j)s4(c_ij)+sum_i s4(delta_i),
    r=max(g,r0).                                                (2)

There is an explicitly constructed integer r by g matrix B with

    B^T B=A,
    sum_(u,i) B_ui^2=tr A.                                      (3)

For each positive c_ij write c_ij=sum_k d_k 4^k, 0<=d_k<=3.
Insert d_k copies of the row2^k(e_i+epsilon_ij e_j), where epsilon_ij=sign(a_ij) and e_i denotes the ith coordinate row.
For each positive delta_i, similarly insert the base-four rows2^k e_i with the appropriate multiplicities.
There are exactly r0 rows.
If r0<g append g-r0 zero rows.

Each pair row contributes its square to both relevant diagonal entries and epsilon_ij times that square to the two symmetric off-diagonal entries.
Summing its digits yields c_ij, and the residual rows complete the diagonal to a_ii.
This proves B^T B=A directly, including zeros and negative off-diagonal entries.
Taking traces proves the second equality in(3).
In particular A is positive semidefinite; no converse for arbitrary positive-semidefinite integer matrices is assumed.

For a nonzero A, let M be the largest positive number among the c_ij and delta_i, and let N be the number of positive numbers in that list.
Then

    N<=g(g+1)/2,
    r0<=3N[1+floor(log_4 M)],
    max|B_ui|<=sqrt M.                                         (4)

Indeed each positive component has at most1+floor(log_4 M) digits, each at most three, and every inserted weight2^k has square at most its component.
This is an explicit logarithmic coefficient-size cost at fixed g, while the squared-entry cost remains exactly tr A.
The zero case is separate: if A=0, take r=g and B=0; no logarithm of zero is used.

Define A# by retaining the diagonal of A and replacing every off-diagonal entry by its absolute value.
For the specifically constructed B above, taking entrywise absolute values gives

    |B|^T |B|=A#.                                               (5)

This exact identity holds because each nonzero row has at most two nonzero coordinates, supported on one prescribed pair or one coordinate.
There is no cancellation between different pairs.
It is not asserted for an arbitrary integer factorization of the same A.
Thus A# is also positive semidefinite and its precise spectrum will determine the extra cover cost.

<a id="higher-degree-phi2-realization"></a>
### 2. Full determinant and absolute-cover formulas

From the constructed B form the integral upper-unitriangular matrix

    V=[[I_r,-B],[0,I_g]].                                       (6)

All diagonal entries are one.
Let s=t+1 and u=t+t^(-1).
The full polynomial is

    p_V(t)=det(tV+V^T)
          =(t+1)^(r-g) P_A(t),
    P_A(t)=t^g det((u+2)I_g-A).                                 (7)

To verify(7), the block determinant over Q(t) is

    det([[s I_r,-t B],[-B^T,s I_g]])
      =s^(r-g) det(s^2 I_g-t B^T B)
      =s^(r-g) t^g det((u+2)I_g-A).

Since r>=g, the displayed multiplier has nonnegative exponent.
Clearing the rational block calculation gives a polynomial identity at every t, including t=0 and t=-1.
The expression P_A is a monic reciprocal integer polynomial of degree2g and constant term one: t^g times a monic degree-g polynomial in u+2 has integral coefficients, exponents from zero through2g and both endpoint coefficients one.
Thus the only added factor in(7) is the explicitly given cyclotomic Phi2^(r-g), of degree r-g.
No scalar normalization, deleted factor or rational matrix is substituted for the required realization.

The dimension and energy are exactly

    dim V=r+g,
    sum_(i<j)V_ij^2=tr A,
    max|V_ij|<=max(1,sqrt M) for A nonzero.                      (8)

These account for zero-row padding as well as all nonzero rows.
They need not be minimal.
In particular appending zeros changes only the permitted Phi2 factor.

The all-negative absolute presentation V^- has off-diagonal block -|B|.
Therefore, by(5),

    p_(V^-)(t)=(t+1)^(r-g) P_(A#)(t).                           (9)

For a nonnegative real lambda define

    F(lambda)=0 if 0<=lambda<=4;
    F(lambda)=arcosh((lambda-2)/2) if lambda>4.

If lambda_1,...,lambda_g are the eigenvalues of A, counting multiplicity, and mu_1,...,mu_g those of A#, then

    m(p_V)=sum_i F(lambda_i),
    m(p_(V^-))=sum_i F(mu_i).                                  (10)

Indeed the associated quadratic is t^2+(2-lambda)t+1.
For lambda in[0,4] both roots have modulus one, including the repeated roots at lambda=0 or4.
For lambda>4 it has positive reciprocal roots, with the expanding logarithm exactly F(lambda).
Both matrices are positive semidefinite by their displayed Gram decompositions, so no negative eigenvalue case has been omitted.
The Phi2 factors contribute zero measure.
C2's complete signed cover W then has exactly p_W=p_V p_(V^-) and total logarithmic measure equal to the sum of the two values in(10).
This is the full absolute-cover cost, not just its Perron root or a lower bound.

Consequently a given reciprocal polynomial P has a sufficient realization certificate whenever its trace polynomial can be written as det((u+2)I-A) for an integer A satisfying(1).
The general task of finding such an A, or proving a target admits one, is not resolved by defining P_A.
Every root trace in this subclass is real and at least-2.
The C412 nonreal-trace target remains excluded, regardless of adding cyclotomic factors, because its original roots remain roots of the product.

<a id="irreducible-quartic-gram-family"></a>
### 3. An irreducible higher-degree family, including the fixed quartic input

For each integer k>=4 take

    A_k=[[1,1],[1,k]].

This satisfies(1), with one pair component c_12=1 and the only nonzero residual delta_2=k-1.
Its complete reciprocal polynomial is

    P_k(t)=t^4+(3-k)(t^3+t^2+t)+1,
    P_k(t)=t^2 Q_k(t+t^(-1)),
    Q_k(u)=u^2+(3-k)u+(1-k).                                  (11)

This follows either by the two by two determinant in(7), or by tr A=k+1 and det A=k-1.
Let h=s4(k-1).
The construction has r0=r=1+h>=2, so it gives

    p_(V_k)=(t+1)^(h-1) P_k,
    dim V_k=3+h<=3+3[1+floor(log_4(k-1))],
    max|V_ij|<=sqrt(k-1),
    sum_(i<j)V_ij^2=k+1.                                      (12)

More concretely B consists of the row(1,1) and the base-four rows(0,2^j) encoding k-1.
All its entries are nonnegative.
Hence V_k already equals V_k^- and the extra absolute-cover measure is exactly m(P_k), with total cover measure2m(P_k).
There is no minimization claim.

Every P_k in(11) is an irreducible Salem polynomial of degree four.
To check this without numerical root inference, the discriminant of Q_k is

    (k-1)^2+4,

which lies strictly between(k-1)^2 and k^2 for k>=4, and is not a square.
Thus Q_k is irreducible quadratic.
Its values at-2,0,2 are respectively k-1,1-k,11-3k.
One trace root u_- is therefore strictly between-2 and0, and the other u_+ is greater than two.
The quadratic trace field is totally real.
The element u^2-4 is negative at its u_- embedding and cannot be a square in that field.
Therefore t^2-u t+1 is irreducible over the trace field, and any root t has degree four over Q, since u=t+t^(-1) lies in Q(t).
This proves irreducibility of P_k.
Its roots comprise one positive expanding reciprocal pair and a nonreal conjugate pair on the unit circle, as required.

The full measure is explicitly

    m(P_k)=arcosh(u_+/2),
    u_+=[k-3+sqrt((k-1)^2+4)]/2.                               (13)

It grows approximately log k; this is not a near-one family.
At k=4, P_k=t^4-t^3-t^2-t+1 is the previously fixed [complete fixed quartic input](Yin_C_G0396_v1.md#quartic-infinite-core-theorem).
Here h=3, B has rows(1,1),(0,1),(0,1),(0,1), and an exact six by six upper-unitriangular V realizes (t+1)^2 P_k.
<a id="quartic-six-to-twelve-cover-costs"></a>
The k=4 matrix just displayed has g=2,r=4, diagonal-one rank6, maximum entry magnitude1, strict-upper squared energy5 and full determinant Phi2^2 P4.
Every strict upper entry is nonpositive.
In C2's vertex-then-sheet cover every nonzero entry is therefore replaced by its scalar times I_2.
There are exactly two equal copies of each strict entry, so the complete cover has rank12, height1 and energy10.
Permuting to sheet-then-vertex order exhibits two copies of the same rank6 matrix.
Consequently its entire polynomial is Phi2^4 P4^2 and its full logarithmic measure is2m(P4)=2log beta4, where beta4>1 is the expanding Salem root of P4.
This is the achieved comparison used by later fixed proofs, with no claim of minimal rank, height, energy or cover measure.

At k=5, h=1 and B has rows(1,1),(0,2), so a four by four V realizes the irreducible quartic itself with no additional factor.
These instances are consequences of the all-parameter construction, not a new finite scan or a claim that the polynomials were previously unknown.

<a id="signed-gram-cover-cost-control"></a>
### 4. A signed higher-degree control where extra measure is smaller than original measure

Equality of added and original measure in the preceding nonnegative-B family and C455 is a feature of those presentations, not a general lower-cost law.
A small signed instance of the same construction makes this distinction exact.

Let A be twice the identity plus the ordinary three-vertex complete-graph Laplacian:

    A=[[4,-1,-1],[-1,4,-1],[-1,-1,4]]=5 I_3-J_3,
    A#=[[4,1,1],[1,4,1],[1,1,4]]=3 I_3+J_3.                  (14)

Both satisfy(1).
Use one row e_i-e_j for each of the three pairs, and two rows e_i for each i.
This is the construction of Section1 with r=9,g=3 and entries in{0,1,-1}; its squared-entry sum is12.
Thus V in(6) has dimension12 and only unit nonzero strict upper entries.

The spectra of A and A# are respectively(2,5,5) and(6,3,3), obtained directly from the eigenvalues3,0,0 of J_3.
Equations(7) and(9) give the entire two polynomials:

    p_V=(t+1)^6 (t^2+1)(t^2-3t+1)^2,
    p_(V^-)=(t+1)^6 (t^2-4t+1)(t^2-t+1)^2.                   (15)

All factors and multiplicities are retained.
Hence

    m(p_V)=2 arcosh(3/2),
    m(p_(V^-))=arcosh(2)<2 arcosh(3/2).                      (16)

For the strict inequality, if v=arcosh(3/2)>0 then cosh(2v)=7/2>2, and cosh is strictly increasing on the nonnegative real axis.
The original measure and the added cost are both positive, consistently with C440v2.
The total signed-cover measure is their sum.
This example proves no optimum and no uniform cost ratio.
Its degree-six reciprocal target is reducible, with one cyclotomic quadratic and a repeated noncyclotomic quadratic factor; the separate family in Section3 supplies irreducible higher-degree targets.

## Exact original contribution, checking and remaining boundary

The structural author supplied the new signed sparse rows, integer trace subclass, exact A# transfer, quartic family and signed cost example.
The underlying rectangular-block real-trace restriction, literal double-cover identity, positive added-cost result and base-four device are reused with their complete scopes.
They are not repackaged as a new source theorem or a universal realization result.
The exact original578-character listed author-check account and entire R90 whole written account remain at their original day precision.
Generic shared context without retained actual initial target contents leaves that original whole independent-review obligation UNKNOWN.
Current authored checking cannot close it or invent an additional original whole author-review event.

This is a sufficient construction on a specified real-trace subclass, not a general realization theorem.
The missing coverage problem is whether the relevant small-measure reciprocal targets admit an appropriate integral trace realization, perhaps after explicitly controlled neutral stabilization or a different matrix class.
Diagonal dominance, Gram integrality and spectral restrictions cannot be silently inferred from small Mahler measure.
Outside the current class, further construction must preserve every diagonal one and full determinant while paying for its actual factors.
Inside it, the exact A# formula makes optimized cost a concrete spectral question, but no near-one cost estimate follows from the examples.

The original historical research wording remains in L191, without selecting or resuming a Task.
No new source/PDF proof inspection, numerical scan, mathematical producer/native run or J is supplied.
