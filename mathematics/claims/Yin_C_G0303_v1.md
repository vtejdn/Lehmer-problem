---
author: Yin
---

# Exact homoclinic coding entropy through block prediction and two endpoint carries

This retains the complete original2026-10-07 [L106 proof](../ledger/Yin_L_G0106_v1.md).
The assembling review_matrix_completion agent derived the upper comparison; assess_shortness_route supplied the finite-carry lower comparison.
The complete original actual checks remain at their sufficient [R30 home](../audits/reviews/Yin_R_G0030_v1.md#contribution-and-actual-review).
No source, computation or Task is newly executed.

## Statement

Let alpha be an algebraic unit with irreducible polynomial P,no unit-circle conjugate and m=log M(P)>0.
Let R be any full order in K=Q(alpha) containing Z[alpha],Lambda=R^vee,X=K_infty/Lambda and T multiplication by alpha.
Use the actual uniformly convergent two-sided homoclinic fair-sign coding with
r_j=A^j e_s1 for j>=0 and r_j=-A^j e_u1 for j<0.
Let nu be its coding law and
H_N=H(sum_(j=0)^(N-1)xi_j alpha^j),h1=lim H_N/N.
Then

    h_nu(T)=h1

for every fixed full order R,without maximal order,injective coding or full support.
Fair-sign and fair-bit finite sums have the same entropy by the exact affine bijection.

The proof retains two finite comparisons.
For any finite q-atom Borel partition Q with null boundaries,q>=2,and sufficiently long fixed boundary buffer B,

    H_nu(join_(t=0)^(N-1)T^(-t)Q)
       <=H_N+2B log q+N[h_bin(p_B)+p_B log(q-1)], N>=2B+1,

where the actual geometric two-tail error epsilon_B tends to0 and
p_B is the nu mass of the epsilon_B-neighborhood of the partition boundaries.
First fix B and take N to infinity,then B to infinity.
Compact-core/null-boundary-grid approximation extends the upper comparison to every finite measurable partition,including completed-measure atoms modulo null sets.

For a sufficiently small quotient-diameter partition Q,choose epsilon with
2epsilon<lambda1 and epsilon(1+norm(A^(-1)))<lambda1.
The fixed compact set D of actual coding lifts and finite carry set
F=Lambda intersect(D-D+closed epsilon ball)
give

    H_N<=H_nu(join_(k=0)^N T^k Q)+2log|F|.

The exact seam equality S_N=x(xi)-A^N x(sigma^(-N)xi) and coherent small backward lifts leave at most|F|² possible exact sums in each N+1-term name class.
Both infinite tails and the N+1 normalization are retained.

The same proof works for every fixed finitely supported integer iid digit law,using its own compact lift and largest absolute digit.
Thus the kth convolution of the actual coding has the entropy rate of its changed per-time sum-of-k-signs law,without identifying that rate with the original h1.
All costs may depend on the fixed input,norm,order and partition.
No uniform onset,entropy equality with m,weak-limit entropy continuity,rational-flow identity or unit-circle/Salem extension is asserted.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:24 |
| status | open |
| reason | Complete original block-prediction upper proof, two-endpoint finite-carry lower proof and fixed finite-integer iid extension retained; current complete checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full statement](#statement) | Entire fixed-full-order hyperbolic coding/algebraic-sum entropy equality, exact finite prediction/Fano and two-carry comparisons and every finite integer iid extension, preserving nonuniform, changed-digit and unit-circle limits. |
| argument | [Complete argument](#argument) | Full original1–12: exact negative block and tail indices, null-boundary/Fano/order-of-limits and arbitrary-partition proof, full-space seam identity, unique coherent backward lifts, compact finite carries, conditional cardinality and N+1 entropy normalization. |
| dependency | [Actual full-order toral coding](Yin_C_G0299_v1.md#argument) | Exact trace-dual lattice, complex signs, uniformly convergent homoclinic representatives, seam and invariant measure on each full-order quotient; no automatic entropy equality is imported. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T08:31 |
| status | proved |
| reason | Adopt the complete original fixed-full-order homoclinic/algebraic-sum entropy equality after actual whole self-review, with the complete upper prediction/Fano and lower two-carry proofs, finite integer iid extension and all input-dependent/nonunit-circle boundaries preserved. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire fixed-full-order hyperbolic coding/algebraic-sum entropy equality, exact finite prediction/Fano and two-carry comparisons and every finite integer iid extension, preserving nonuniform, changed-digit and unit-circle limits. |
| argument | [Argument](#argument) | Full original1–12: exact negative block and tail indices, null-boundary/Fano/order-of-limits and arbitrary-partition proof, full-space seam identity, unique coherent backward lifts, compact finite carries, conditional cardinality and N+1 entropy normalization. |
| dependency | [Dependency](Yin_C_G0299_v1.md#argument) | Exact trace-dual lattice, complex signs, uniformly convergent homoclinic representatives, seam and invariant measure on each full-order quotient; no automatic entropy equality is imported. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0543_v1.md#current-coding-entropy-finding) | Exact full current statement, complete retained original argument and every selected interface, self-reviewed; old findings keep only their actual original inputs and precise relationships. |

## Complete retained argument

<a id="argument"></a>
Throughout, alpha is an algebraic unit with irreducible polynomial P and no unit-circle conjugate, with m=log M(P)>0.
Let R be any full order in K=Q(alpha) containing Z[alpha], and let Lambda=R^vee be its trace dual.
Put X=K_infty/Lambda and let T be multiplication by alpha.
These are precisely the order, real trace pairing and complex-coordinate conventions of [C G0300](Yin_C_G0299_v1.md#trace-torus-dual-normalization).
In particular the character lattice is R, not automatically O_K.

Let A be multiplication by alpha on K_infty, and e_s,e_u its stable and expanding coordinate projections.
Use the actual Euclidean representatives

    r_j=A^j e_s1       (j>=0),
    r_j=-A^j e_u1      (j<0).

They satisfy sum_j ||r_j||<infinity and A r_-1-r_0=-1.
For two-sided independent fair signs xi_j, set

    x(xi)=sum_(j in Z) xi_j r_j,
    kappa(xi)=[x(xi)],   nu=kappa_*Bernoulli,
    (sigma xi)_j=xi_(j-1).

Then kappa sigma=T kappa, and D={x(xi):xi in {-1,1}^Z} is a compact subset of K_infty, by uniform convergence.
We distinguish this compact set of actual lifts from its torus image.

Define the exact algebraic sums and their discrete entropies by

    S_N=sum_(j=0)^(N-1) xi_j alpha^j,
    H_N=H(S_N),   h_1=lim_(N->infinity) H_N/N.          (1)

The limit exists because H_(N+M)<=H_N+H_M: split the independent blocks and multiply the second by the injective map alpha^N.
The sign convention has the same H_N as fair digits {0,1}, since the two algebraic sums differ by an injective affine map.
All logarithms are natural.

<a id="homoclinic-entropy-equality"></a>
### Exact conclusion

For this actual measure and toral automorphism,

    h_nu(T)=h_1.                                       (2)

This holds for every fixed full order R above.
No maximal-order assumption, assumption of injective coding, or assertion that the support is the whole torus is needed.
The proof controls infinite tails on both sides; it does not identify a finite algebraic sum with a torus point injectively.

<a id="algebraic-block-upper-entropy"></a>
### Upper bound: an exact block sum predicts the middle orbit names

Fix a finite Borel partition Q of X with q>=2 atoms and nu-null boundaries.
A one-atom partition is trivial.
Let U_delta be the closed delta-neighborhood of the union of its boundaries.
Since this is a finite union of closed null sets in a compact torus,

    p_delta=nu(U_delta)->0 as delta->0.

Such partitions may be chosen to be finite coordinate grids.
The same argument applies whenever the displayed boundary property holds.

For a block of length N take the digits indexed -N+1,...,0, and set

    Z_N=sum_(j=-N+1)^0 xi_j alpha^j,
    y_N=[e_s Z_N]=sum_(j=-N+1)^0 xi_j [r_j].           (3)

The second equality follows because [r_j]=[A^j e_s1]; for negative j their difference is alpha^j in R, hence in Lambda.
The torus point y_N is therefore a deterministic function of the exact algebraic value Z_N.
Multiplying by alpha^(N-1) and reversing the independent digits proves H(Z_N)=H_N.

For every t=0,...,N-1, the omitted part of T^t kappa(xi) has representatives sum_(j outside [-N+1,0]) xi_j r_(j+t).
Indeed T^t[r_j]=[r_(j+t)], and the absolutely convergent series can be shifted and passed to the quotient.
Consequently, if B<=t<=N-1-B,

    dist(T^t kappa(xi),T^t y_N)<=epsilon_B,
    epsilon_B=sum_(k>=B+1)||r_k||
                    +sum_(k<=-B-1)||r_k|| ->0,         (4)

uniformly over every sign sequence and N.
This is the boundary estimate; no convergence of a finite-prefix distribution to nu is being assumed.

Given Z_N, predict the atom Q(T^t kappa(xi)) by Q(T^t y_N).
For an interior time in (4), a mistake requires T^t kappa(xi) to lie in U_(epsilon_B).
Invariance of nu bounds its probability by p_B:=p_(epsilon_B).
For sufficiently large B, p_B<=1/2, and elementary Fano conditioning gives

    H(Q(T^t kappa(xi)) | Z_N)
       <= f_q(p_B):=h_bin(p_B)+p_B log(q-1).             (5)

Here the usual error expression is increasing on [0,1/2] for q>=2; one obtains it by conditioning on whether the predicted label was wrong.
The at most 2B remaining times cost at most log q each.
Conditional subadditivity therefore gives, for N>=2B+1,

    H_nu(join_(t=0)^(N-1) T^(-t)Q)
       <=H_N+2B log q+N f_q(p_B).                      (6)

First let N tend to infinity with B fixed, and then let B tend to infinity.
It follows that h_nu(T,Q)<=h_1.

These partitions suffice to bound the measure entropy over all finite measurable partitions.
To see this without assuming a generating-partition theorem, take an arbitrary finite partition P.
By regularity choose disjoint compact cores of its atoms whose union has mass at least 1-delta.
A sufficiently fine finite coordinate grid has cells too small to meet two different compact cores.
Choose its finitely many coordinate boundaries to have zero nu mass; this is possible since each coordinate marginal has at most countably many atoms.
Predicting P from that grid makes an error at most delta, so H(P|Q)<=f_q(delta), where q is now the number of P atoms.
The entropy chain rule gives

    h_nu(T,P)<=h_nu(T,Q)+H(P|Q)<=h_1+f_q(delta).

Let delta tend to zero and take the supremum over P.
Thus

    h_nu(T)<=h_1.                                      (7)

The compact-core argument also applies to partitions in the completed measure space after changing atoms on null sets.

<a id="two-endpoint-carry-lower-entropy"></a>
### Lower bound: a small orbit name leaves only finitely many endpoint carries

Fix a Euclidean norm on K_infty and let lambda_1>0 be the length of a shortest nonzero vector of Lambda.
Choose epsilon>0 such that

    2epsilon<lambda_1,
    epsilon(1+||A^(-1)||)<lambda_1.                     (8)

Take a finite Borel partition Q of X with every atom of quotient diameter strictly less than epsilon.
Null boundaries are not needed for this lower bound.
For any pair of points in the same atom, their difference has a unique lift of norm less than epsilon: existence follows from the quotient metric, and uniqueness from 2epsilon<lambda_1.

The seam identity gives the following exact equality in K_infty:

    S_N=x(xi)-A^N x(sigma^(-N)xi).                     (9)

Indeed, in the coefficient of xi_j the difference r_j-A^N r_(j-N) vanishes unless 0<=j<N.
On that interval it equals A^j(e_s+e_u)1=A^j1.
Hyperbolicity enters here through e_s+e_u=I.

Suppose two sign sequences xi and xi' produce the same backwards Q-name at times 0,...,N, namely the same atoms containing T^(-k)kappa(xi) and T^(-k)kappa(xi') for every such k.
Let delta_k be the unique difference lift of norm less than epsilon.
Then

    delta_(k+1)-A^(-1)delta_k in Lambda,
    ||delta_(k+1)-A^(-1)delta_k||
                           <epsilon(1+||A^(-1)||).

By (8) this lattice vector is zero.
Hence

    delta_k=A^(-k)delta_0.                             (10)

Since all actual coding lifts lie in D, there exist endpoint carries lambda_0,lambda_N in the fixed finite set

    F=Lambda intersect (D-D+closed ball of radius epsilon)

such that

    x(xi)-x(xi')=delta_0+lambda_0,
    x(sigma^(-N)xi)-x(sigma^(-N)xi')=delta_N+lambda_N.

The set is finite because D is compact and Lambda is a lattice; it contains zero.
Subtracting (9) for the two sequences and using (10) cancels the real displacement and leaves

    S_N(xi)-S_N(xi')=lambda_0-A^N lambda_N.            (11)

Fix one reference sequence for any nonempty name class.
Equation (11) proves that within that entire class the exact algebraic variable S_N takes at most |F|^2 values, regardless of N.
This statement concerns both infinite tails, not merely two finite words.
Conditional entropy is thus at most 2log|F|, and

    H_N<=H_nu(join_(k=0)^N T^k Q)+2log|F|.             (12)

The join has N+1 backwards times.
By invariance and invertibility its entropy equals that of an N+1-term forward join of Q.
Divide (12) by N and pass to the limit to get h_1<=h_nu(T,Q)<=h_nu(T).
Together with (7), this proves (2).

<a id="coding-entropy-scope-and-costs"></a>
### What this bridge changes and what it leaves open

The finite estimates (6) and (12) are the substantive comparison.
The upper loss is a vanishing per-time partition-prediction error after fixing a long boundary buffer.
The lower loss is the constant 2log|F| from two endpoint carries.
Both costs depend on the fixed input, norm, order and partition.
They are not asserted uniform in degree or as m tends to zero.

In particular, the exact measure used by the trace Fourier witness has entropy h_1, so a genuine entropy estimate for this specific invariant measure can be read as an estimate for the algebraic fair-binary entropy rate.
This improves the earlier factor bound h_nu(T)<=log2.
It supplies no new lower bound on h_1 and no automatic equality h_1=m.
Nor does it identify the entropy of a changed digit law, such as a convolution power, with the original h_1.

The same proof applies to any fixed, finitely supported integer digit law with independent identically distributed digits.
Replace H_N by the entropy of its exact algebraic sum, use its compact coding-lift set D, and multiply epsilon_B in (4) by the largest absolute digit.
The seam discrepancies remain in Lambda because the digits are integers; (9)--(12) are unchanged, and multiplying and reversing an iid block still proves the entropy identity used in (3).
Thus its toral coding entropy equals its own algebraic-sum entropy rate.
In particular, the measure nu^(star k) from L G0104 corresponds to the law of a sum of k independent fair signs at each time, and its entropy equals that changed law's rate.
No convergence of these entropies to m is inferred from the Fourier convergence of the measures towards Haar.

Changing R changes the quotient lattice and can change the measure as a toral factor, but the argument proves that these particular codings all have the same entropy h_1.
The statement remains about the integral-order torus; it does not identify this compact group with the dual of the original rational additive flow.
No unit-circle or Salem extension is asserted: the geometric tail estimate and the exact full-space identity (9) both use hyperbolicity.
