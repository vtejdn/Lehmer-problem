---
author: Yin
---

# Constructive integral trace realizations and full absolute-cover costs

The current complete [C458v2 theorem](../claims/Yin_C_G0458_v2.md#statement) is adopted with its [whole corrected-chain independent finding](../audits/reviews/Yin_R_G0669_v1.md#integral-gram-whole-independent-finding).
The original sufficient construction and day-precision adoption below retain their historical inputs and scope.

Date: 2026-10-10.
The coordinating AI for Yin adopts the complete separately reviewed D G0060 proof at the exact scope below.
The assigned orbit_research AI supplied its mathematics; the coordinator supplied the full noncontributor review.
No source proof or program is newly adopted.

<a id="integral-gram-realization-fixed-scope"></a>
## Adopted scope

Every symmetric integer trace matrix A with nonnegative diagonal-dominance residual has the explicit integer Gram construction retained below.
It realizes P_A=t^g det((t+t^(-1)+2)I-A) by an integral upper-unitriangular determinant with exactly a stated Phi2 power.
Rank, coefficient size, energy and every absolute-cover factor are controlled explicitly.
The constructed factorization transfers its absolute polynomial exactly to A#, so its whole logarithmic measure is the stated spectral sum.

The irreducible quartic Salem family and the signed unit-entry cost comparison are adopted with their complete factors.
This is a sufficient real-trace subclass, not universal reciprocal coverage.
Its quartic measures grow with the parameter; the signed example is reducible and asserts no optimum.
Neither an unrestricted small-measure realization nor a G0001 gap is proved.
Historical pending-review wording remains chronology; this adoption and the complete finding determine present status.
Only heading depth and relative navigation are transformed in the retained body.

<a id="retained-integral-gram-realization-proof"></a>
## Integral Gram completion, higher-degree reciprocal realizations and exact cover cost

Date: 2026-10-10.
Responsible orbit_research proof for Yin.
The coordinator assigned a higher-degree construction or stabilization invariant beyond L190; this agent developed the argument below.
It is a new self-checked proof, not yet separately reviewed or fixed.
No remote operation, numerical search or new external theorem is used.

### Reuse and exact scope

The [fixed L190 stabilization theorem](Yin_L_G0190_v1.md#cyclotomic-stabilization-fixed-scope) handles endpoint costs and a quadratic family.
Its endpoint repair is not a general sufficiency theorem.
The [block-bipartite calculation in L175](Yin_L_G0175_v1.md#sparse-trinomial-auxiliary), in its subsection on the Pisot obstruction, already computes the determinant for arbitrary real rectangular B and proves its real-trace restriction.
The [D9 signed-cover identity](../claims/Yin_C_G0002_v1.md#signed-cover-identity) and [L185 positive-cover cost theorem](Yin_L_G0185_v1.md#positive-absolute-cover-cost) retain their full factors and exact scopes.

The changed input here is an explicit integer Gram construction: a testable class of trace matrices is factored by integer rows with controlled row count and coefficients.
This gives actual integral upper-unitriangular realizations of reciprocal polynomials of arbitrary even degree, using only a stated power of Phi2 as neutral multiplier.
The absolute-cover polynomial is also computed in full.
An irreducible degree-four family and a separate signed degree-six cost control make the distinction concrete.

The sufficient hypothesis is symmetric integral diagonal dominance with nonnegative residual diagonal.
It is not assumed for every reciprocal target, and no change of integral basis establishing it in general is supplied.
In particular the positive-semidefinite, real-trace restriction from L175 remains in force even under arbitrary cyclotomic multiplication.
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
D9's signed cover W then has exactly p_W=p_V p_(V^-) and total logarithmic measure equal to the sum of the two values in(10).
This is the full absolute-cover cost, not just its Perron root or a lower bound.

Consequently a given reciprocal polynomial P has a sufficient realization certificate whenever its trace polynomial can be written as det((u+2)I-A) for an integer A satisfying(1).
The general task of finding such an A, or proving a target admits one, is not resolved by defining P_A.
Every root trace in this subclass is real and at least-2.
The L175 nonreal-trace target remains excluded, regardless of adding cyclotomic factors, because its original roots remain roots of the product.

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
At k=4, P_k=t^4-t^3-t^2-t+1 is the previously fixed [L169 quartic input](Yin_L_G0169_v1.md#quartic-infinite-core-theorem).
Here h=3, B has rows(1,1),(0,1),(0,1),(0,1), and an exact six by six upper-unitriangular V realizes (t+1)^2 P_k.
At k=5, h=1 and B has rows(1,1),(0,2), so a four by four V realizes the irreducible quartic itself with no additional factor.
These instances are consequences of the all-parameter construction, not a new finite scan or a claim that the polynomials were previously unknown.

<a id="signed-gram-cover-cost-control"></a>
### 4. A signed higher-degree control where extra measure is smaller than original measure

Equality of added and original measure in the preceding nonnegative-B family and L190 is a feature of those presentations, not a general lower-cost law.
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
The original measure and the added cost are both positive, consistently with L185.
The total signed-cover measure is their sum.
This example proves no optimum and no uniform cost ratio.
Its degree-six reciprocal target is reducible, with one cyclotomic quadratic and a repeated noncyclotomic quadratic factor; the separate family in Section3 supplies irreducible higher-degree targets.

### 5. Contribution, checks and continuation boundary

The new content is the explicit sufficient integer trace-matrix class, its sparse signed row construction and logarithmic coefficient encoding, its exact absolute-matrix transfer A to A#, the irreducible quartic realization family, and the signed cost comparison.
The underlying real block determinant and its spectral restriction are fixed L175 reuse, while the signed double-cover factorization and positive-cost necessity are fixed D9/L185 reuse.
The base-four device is reused from L190 in a changed matrix factorization; neither that device nor these assembled facts are presented as external-literature novelty.
The coordinator assigned the broader question but supplied none of these derivations.

The author checked every row contribution and padding case, nonnegative residual and PSD hypotheses, the full block determinant at exceptional t by polynomial identity, all multiplicities and logarithmic-measure contributions, row/height/energy costs, quartic trace signs and irreducibility via the real field embedding, and the exact signed triangle spectra and strict cost inequality.
No floating approximations, computational samples or continuing program are needed for these written identities; no J is introduced.
A complete separate noncontributor review remains pending.

This is a sufficient construction on a specified real-trace subclass, not a general realization theorem.
The missing coverage problem is whether the relevant small-measure reciprocal targets admit an appropriate integral trace realization, perhaps after explicitly controlled neutral stabilization or a different matrix class.
Diagonal dominance, Gram integrality and spectral restrictions cannot be silently inferred from small Mahler measure.
Outside the current class, further construction must preserve every diagonal one and full determinant while paying for its actual factors.
Inside it, the exact A# formula makes optimized cost a concrete spectral question, but no near-one cost estimate follows from the examples.
G0001 remains active and unresolved.



The original whole review, dated 2026-10-10 at day precision, and its adoption above remain past facts, with their exact inspected scope, UNKNOWN arrangement and contribution/source/nonexecution limits retained in [R669's later historical comparison](../audits/reviews/Yin_R_G0669_v1.md#l191-r90-and-r812).
That later review was not an input to the original adoption.

## Retention and review bindings

The original complete noncontributor review checked the entire [retained proof](#retained-integral-gram-realization-proof), including every integer row, exceptional determinant value, measure contribution, irreducibility argument and scope boundary.
[R669's historical comparison](../audits/reviews/Yin_R_G0669_v1.md#l191-r90-and-r812) preserves that whole original scope and its UNKNOWN initial arrangement.
The reviewer assigned the question but supplied none of the derivations.
No numerical or external-source verification is claimed.

The complete D G0060 proof remains here, with its original noncontributor review's necessary facts retained at the historical comparison above.
