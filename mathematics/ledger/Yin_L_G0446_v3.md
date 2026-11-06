---
author: Yin
---
# Arithmetic random matrices: companion-minor propagation and paid dyadic gain

<a id="scope-and-strategic-assessment"></a>
## Scope and strategic assessment

This bounded 2026-11-05 continuation concerns the unchanged [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract) and [S6's integral-minor question](../strategies/Yin_S_G0006.md#integral-minor-proliferation-2026-11-05).
The fixed inputs are [C209's original orbit/kernel identity and finite certificate](../claims/Yin_C_G0209_v1.md#statement) and [L446v2's first-witness and volume-sampling comparison](Yin_L_G0446_v2.md#integer-minors-and-the-volume-sampling-probability-law).
The earlier prime, graph and volume-sampling comparisons remain at their exact scope in v2.
L446v2 already explains why a single nonunit minor and its translates do not give a positive uniform rate.
The question is whether a local witness can be multiplied inside the same original window, or whether integral saturation and positivity force another actual gain.
The calculations below are author-checked exploration, not independently reviewed Claims or an adopted uniform-gap result.
The paid dyadic identity supplies no additional arithmetic lower bound beyond its stated integer estimate.

## Exact original objects

Let P be monic and squarefree in Z[t], of degree d>=1, with P(0)=1 or -1.
Let C be multiplication by t on Z[t]/(P), in the ordered power basis, and let e be the first coordinate vector.
For L>=0 write v_j=C^j e, V_L=[v_0,...,v_(L-1)] and W_L=V_L V_L^T; for L>=d put G_L=det W_L.
Then v_0,...,v_(d-1) are the standard basis, det C=1 or -1 and G_L is a positive integer.
Put Delta=|disc P| and

    F_L=log Delta+log G_L-d log L.

The exact C209 certificate is F_L<=2(L-1)m(P).
A useful gain must be assessed in F_L at the actual original L and d.

Let A_N have the full coefficient columns P,tP,...,t^(N-1)P, with rows indexed by 0,...,N+d-1.
C209 gives det(A_N^T A_N)=G_(N+d), and complementary maximal minors agree in absolute value with the d-column minors of V_(N+d).
These facts keep the original integer lattice and every finite-window row.

<a id="deletion-budget"></a>
## Why independent local blocks do not concatenate for free

An N-row maximal minor of A_N selects rows

    0<=r_0<r_1<...<r_(N-1)<=N+d-1.

Set b_i=r_i-i.
Then

    0<=b_0<=b_1<=...<=b_(N-1)<=d,
    b_(i+1)-b_i=r_(i+1)-r_i-1.

The first inequality follows from the order of the selected rows and the d omitted rows.
The last identity counts exactly the omitted rows strictly between successive selected rows.
Including the omitted initial and terminal rows gives exactly d omitted rows in total.

Consequently a recipe that builds each independent local block by introducing fresh omitted rows can use those deletions at most d times.
It cannot repeat an interior block and then reset the omission state at no cost.
This concerns that literal block-concatenation mechanism, not the growth of every minor.
Long stretches with constant b_i remain possible and can themselves have growing determinants.

## The exact exterior state, and what its positivity means

For 0<=k<=d, let H_k be the kth real exterior power of R^d, in its standard exterior basis.
Put A_k=Lambda^k C and let E_k:H_(k-1)->H_k be w |-> e wedge w for k>=1.
For L>=0 define the positive semidefinite matrix

    X_(k,L)=sum_(0<=j_1<...<j_k<L) w_J w_J^T,
    w_J=v_(j_1) wedge ... wedge v_(j_k).

The empty exterior power is H_0=R and X_(0,L)=1.
For k>0 the sum is zero when L<k.
Cauchy--Binet gives X_(k,L)=Lambda^k W_L, and X_(d,L)=G_L for L>=d.

Partition the subsets of {0,...,L} according to whether they contain 0.
Those omitting 0 are obtained by applying C to each vector of a subset of {0,...,L-1}.
For those containing 0, put e first and apply C to the other k-1 vectors.
This proves the exact recurrence

    X_(k,L+1)
      =A_k X_(k,L) A_k^T
       +E_k A_(k-1) X_(k-1,L) A_(k-1)^T E_k^T,       (EX1)

for 1<=k<=d, with X_(0,L+1)=X_(0,L).
It is an integral positive linear evolution on the direct sum of symmetric-matrix spaces.

Each path through these graded blocks can raise its exterior degree at most d times.
The same-degree evolution is conjugation by one compound A_k; there is no independent second branch or downward reset at that degree.
This is the exact state-space version of the preceding deletion budget.

The diagonal conjugation block X |-> A_k X A_k^T has spectral radius rho(A_k)^2.
For an upper bound, its complexified eigenvalues are products of eigenvalues of A_k.
For the reverse bound, choose an eigenvector z of A_k at an eigenvalue of maximum modulus.
The nonzero real symmetric matrix Re(z z*) is positive semidefinite and is an eigenmatrix with eigenvalue rho(A_k)^2.
The full block evolution is triangular in k, so its spectral radius is the largest of these diagonal radii.

The eigenvalues of A_k are the products of k roots of P.
Maximizing their moduli over k includes exactly the roots outside the unit circle and therefore gives

    rho(EX1)=M(P)^2.                                  (EX2)

Thus the exact integral positive recursion keeps the desired information, but its spectral radius is the original Mahler quantity.
A generic Perron assertion for EX1 supplies no new gap without further arithmetic information.
The map is not irreducible on its whole positive cone: the states supported only at degree d form a nonzero invariant face.
On that face the map is the identity, since A_d=det C.

<a id="paid-dyadic-gain"></a>
## An exact positive local gain after the entire window boundary

For L>=d, split the original orbit into two adjacent L-windows:

    W_(2L)=W_L+C^L W_L (C^L)^T.

Put B_L=W_L^(-1/2) C^L W_L^(1/2), and let sigma_1,...,sigma_d be its positive singular values.
Their product is one, since |det C|=1.
Taking determinants and using 1+sigma^2=2 sigma cosh(log sigma) gives

    F_(2L)-F_L
      =log[G_(2L)/(2^d G_L)]
      =sum_(i=1..d) log cosh(log sigma_i)
      =:Q_L>=0.                                      (DY1)

The d log 2 increase in the full C209 boundary has been subtracted exactly.
The discriminant is the same original Delta at both scales and has not been replaced or omitted.
Equality holds exactly when B_L is orthogonal, equivalently

    C^L W_L (C^L)^T=W_L.                             (DY2)

If m(P)>0, a root of this monic unit polynomial has modulus greater than one.
Then DY2 is impossible: C^L would be similar to an orthogonal matrix and would have all eigenvalues of modulus one.
Thus Q_L>0 for every L>=d whenever m(P)>0, and integer determinants give

    Q_L>=log(1+1/(2^d G_L)).                          (DY3)

Indeed G_(2L) and 2^d G_L are integers, and strict inequality separates them by at least one.
This bound retains its complete potentially large denominator.

The exact iterated comparison is

    F_(2^s L)=F_L+sum_(j=0..s-1) Q_(2^j L).           (DY4)

At L=d one has W_d=I and hence F_d=log Delta-d log d.
Thus DY4 exposes both the initial discriminant deficit and the gain accumulated at each original scale.
Strict gain at every scale is insufficient by itself: the known integer lower bound DY3 need not grow proportionally to the final window.
No degree-uniform positive estimate for the normalized right-hand side of DY4 has been obtained.

<a id="saturation-and-cone-test"></a>
## The low-order saturation and positive-cone test

The tested additional information was integral saturation of low-order orbit wedges, or the fact that their covariance becomes positive definite after a bounded number of steps.
Here both properties are automatic and do not distinguish the required inputs.

For every 1<=k<=d, the wedges of k distinct columns among v_0,...,v_(d-1) are precisely the standard basis of Lambda^k Z^d.
Thus the integer module generated by all kth-order orbit wedges is already the full exterior lattice at L=d.
Its index is one at that point and remains one thereafter.
Likewise

    X_(k,d)=I_(binom(d,k)),

so every degree block is already positive definite on the original input after d steps.
Every consecutive d-column orbit basis is also unimodular, because it is C^j times the initial basis.

These statements hold without noncyclotomicity.
For the degree-unbounded irreducible control P=t^d+1, with d a power of two, C is a signed permutation and

    C^d=-I, W_(kd)=k I, G_(kd)=k^d, Delta=d^d.

The Gram formula follows by decomposing kd consecutive orbit vectors into k signed copies of the standard basis.
The discriminant formula is also the retained L446v2 calibration.
It follows that F_(kd)=0 and Q_(kd)=0 for every integer k>=1.
The full lower-order lattice saturation and positive definiteness coexist with exact cancellation of the entire original certificate.
This refutes a positive-gain inference from those properties alone, not an estimate using further noncyclotomic arithmetic.

Adding the existence of one nonunit minor also leaves every one of these saturated lattices unchanged.
That witness changes a coordinate of an already saturated module, not its index.
A lattice-index argument using only these modules cannot amplify the witness.
A useful lattice replacement would have to identify a different nontrivial quotient or a quantitative restriction on the relative metrics in DY1.

## Current outcome and continuation boundary

The literal independent-block multiplication fails because its deletion state cannot reset.
The exact positive exterior recursion has only finitely many degree-raising steps, and its same-degree spectral growth is exactly the original Mahler growth.
The attempted added source of information, low-order integral saturation and positivity at time d, is automatic even in the irreducible zero-measure calibration.
It does not produce a new uniform arithmetic gain.

DY1 is a paid finite local mechanism: relative distortion of the actual original metric produces an additive gain in the complete C209 numerator.
DY3 is the integer rigidity currently obtained, and it does not supply a uniform rate.
The unresolved improvement is a non-tautological arithmetic constraint forcing substantial relative distortion with its actual delay and initial discriminant deficit paid.
No such constraint is presently supplied, and uniform minor proliferation has not been established.

This outcome does not justify a larger search over local maximal-minor witnesses, a repeated lower-order saturation calculation, or a generic positive-matrix theorem applied to EX1.
A further assignment through this interface should begin with a concrete new quotient, inequality or original-input restriction capable of strengthening DY3, rather than another reformulation of EX2.
No computation or new external theorem was used in these deductions.
