---
author: Yin
---

# Exact Haar induction, mixed moments and full radical extensions

Date: 2026-10-07.
Direct bounded derivation by the assigned AI assess_shortness_route for Yin, within G0001.
This note reuses the full cyclic-module decomposition of L G0003 and the exact Haar conventions of L G0085--L G0086.
It adds an exact product formula for moment generating functions, preservation of their best uniform constant, and the precise field-extension boundary.
No source acquisition, computation or novelty claim is involved.

<a id="radical-haar-product"></a>
## Full cyclic induction gives independent Haar coordinates

Let alpha be a nontorsion algebraic unit with monic irreducible polynomial P of degree d, and write O=Z[alpha].
For k>=1 let

    R_k=Z[t]/(P(t^k)),     tau=t mod P(t^k).

This is the entire quotient, whether or not P(t^k) is irreducible.
It is a free abelian group of rank kd, and multiplication by tau is an automorphism.
The coefficient-class decomposition in [L G0003](Yin_L_G0003_v1.md#g0001-cyclic-induction) gives

    R_k=direct-sum_(j=0)^(k-1) tau^j O,
    tau^(kh+j)=tau^j alpha^h.                             (1)

Here O embeds by alpha=tau^k.
Divisibility by P(t^k) can be checked separately in every exponent class modulo k, so (1) is an integral module identity, not an assumption about roots.
Its dual Haar measure is the product Haar measure on k copies of the torus dual to O.

For y in that base torus put

    Z_n(y)=sum_(h=0)^(n-1) chi_y(alpha^h),    Z_0=0,
    M_n(t,theta)=integral exp(t Re(exp(-i theta)Z_n(y)))dy,
    M_0=1,                                               (2)

where t and theta are real.
For n=kq+s, 0<=s<k, define n_j=q+1 for j<s and n_j=q for j>=s.
Formula (1) then proves the exact identities

    Z_n^(k)(y_0,...,y_(k-1))=sum_j Z_(n_j)(y_j),
    M_n^(k)(t,theta)=product_j M_(n_j)(t,theta)
                   =M_(q+1)(t,theta)^s M_q(t,theta)^(k-s).
                                                               (3)

Independence is across the full integral coordinate blocks.
No independence of different powers inside a block is asserted.
In particular the passage from (3) to a bound needs no Holder loss proportional to the number k of residue classes.

<a id="radical-mixed-moment-series"></a>
## The exact all-order identity uses mixed moments

For p,q>=0 put

    C_n(p,q)=integral Z_n^p conjugate(Z_n)^q,
    F_n(z,w)=integral exp(z Z_n+w conjugate(Z_n))
             =sum_(p,q>=0) C_n(p,q) z^p w^q/(p!q!).        (4)

Each C_n(p,q) counts equalities between a labelled p-term list and a labelled q-term list of powers.
It is a nonnegative integer, with the empty list allowed.
The series is entire in the two complex variables: |Z_n|<=n gives absolute convergence on every compact set.
The raw additive energy is A_(n,r)=C_n(r,r).
Equation (3) has the exact two-variable version

    F_n^(k)(z,w)=product_j F_(n_j)(z,w),
    A_(n,r)^(k)
      =(r!)^2 sum_(sum p_j=sum q_j=r)
                    product_j C_(n_j)(p_j,q_j)/(p_j!q_j!).       (5)

The two constraints in this sum do not require p_j=q_j in each block.
Consequently the balanced generating function sum_r A_(n,r)u^r/(r!)^2 does not in general multiply under induction.
Independent coordinate sums do not create independent uniform rotations of their complex values.

For a concrete check, take alpha=phi=(1+sqrt(5))/2 and n_j=3.
The identity 1+phi=phi^2 gives C_3(2,1)>=2 and C_3(1,2)>=2, by the two orderings of the two-term side.
In the two-block, r=3 formula (5), allocations (2,1),(1,2) and their exchange therefore contribute at least

    2 (3!)^2 [2/(2!1!)] [2/(1!2!)]=72

additional tuples beyond all allocations with p_j=q_j.
Every other coefficient is nonnegative.
This is an actual failure of the putative balanced-series product, not just an issue of unavailable independence notation.

<a id="exact-subgaussian-induction-constant"></a>
## The best uniform Haar MGF constant is preserved exactly

Call sigma>=0 admissible for the base if, for every n>=1 and all real t,theta,

    M_n(t,theta)<=exp(sigma n t^2/2).                      (6)

The admissible sets for the base and its full k-fold induction are identical.
The forward implication follows from (3) and sum_j n_j=n.
Conversely, setting n=kq in (3) gives M_(kq)^(k)=M_q^k; taking the positive kth root of (6) recovers the base bound.
Therefore their infima satisfy exactly

    sigma_*(R_k,tau)=sigma_*(O,alpha).                    (7)

This includes a potentially infinite infimum.
On the current unit domain it is finite: the proof in [L G0086](Yin_L_G0086_v1.md#elementary-house-moment-bound) gives the admissible constant a=ceil(log2/log rho) for any conjugate modulus rho>1.
Both modules also have nonzero second moments, so no zero constant is admissible.

For any admissible sigma>0, angular averaging of (6), with the nonnegative series from L G0086, gives

    t^(2r) A_(n,r)/(4^r(r!)^2)<=exp(sigma n t^2/2).

Choosing t^2=2r/(sigma n) proves, simultaneously for every k,n,r,

    A_(n,r)^(k)<=(2e sigma n/r)^r (r!)^2
                  <=(2e sigma r n)^r.                    (8)

Thus a common base MGF bound gives a common all-order moment constant throughout all full cyclic inductions, independently of k and of their diminishing house.

An all-order moment hypothesis on the base also suffices with an absolute loss independent of k.
Suppose

    A_(n,r)<=(C r n)^r  for every n,r>=1.                  (9)

For X=Re(exp(-i theta)Z_n) one has E X=0, since every alpha^h is a nonzero element of the torsion-free group O.
If X' is an independent copy, Jensen gives E exp(tX)<=E exp(t(X-X')).
The difference is symmetric, and

    E(X-X')^(2r)<=4^r E|X|^(2r)<=(4C r n)^r.

Since (2r)!>=r! r^r, its even power series gives

    M_n(t,theta)<=sum_(r>=0) (4C n t^2)^r/r!
                    =exp(4C n t^2).                     (10)

All variables here are bounded, so the series manipulations are justified for every real t.
Combining (7), (8) and (10) proves A_(n,r)^(k)<=(16e C r n)^r for all k,n,r.
This uses all moment orders in (9), not just every fixed-order asymptotic or the slowly growing windows of [L G0085](Yin_L_G0085_v1.md#uniform-fixed-moment-energy).
No converse from those limited windows has been assumed.

<a id="full-degree-radical-guard"></a>
## Exactly when the complete decomposition is a field decomposition

Let beta^k=alpha, K=Q(alpha), L=Q(beta), and ell=[L:K]<=k.
The following are equivalent:

1. P(t^k) is irreducible over Q.
2. [L:K]=k, or equivalently [L:Q]=kd.
3. 1,beta,...,beta^(k-1) are linearly independent over K.
4. The evaluation R_k -> Z[beta] is an isomorphism and
   Z[beta]=direct-sum_(j<k) beta^j Z[alpha].

The first three follow from the degree of t^k-alpha and the tower formula.
Under (3), the exponent-class expansion proves (4), including injectivity over Z.
Conversely (4) forces the rank kd and hence (2).
Since beta is a root of P(t^k), this also proves (2) implies (1) without a separate irreducibility criterion.
Beta is an algebraic unit: both beta and beta^-1 satisfy monic equations over algebraic integers.

When ell<k, evaluation is a proper quotient of free integral modules.
On dual tori, its Haar measure lies on a proper subtorus of the k-coordinate torus; the coordinate variables need not be independent.
All equalities in the full quotient remain equalities after evaluation, so

    A_(n,r)(beta)>=A_(n,r)^(k),                           (11)

which gives no transfer of an upper bound in the desired direction.
The total-Mahler accounting from L G0003 is

    m(beta)=(ell/k)m(alpha),
    m(P(t^k))=m(P),    house(P(t^k))=house(P)^(1/k).        (12)

The full-module measure and its MGF bound must therefore not be assigned to a selected factor when ell<k.

There is an explicit numerical-constant failure of such an assignment, using only exact elementary inequalities.
Take alpha=phi^2, whose minimal polynomial is u^2-3u+1.
Its house is phi^2>2, so L G0086 makes sigma=1 admissible for the base and, by (7), its full k=2 induction.
But

    P(t^2)=t^4-3t^2+1=(t^2-t-1)(t^2+t-1),

and choosing beta=phi loses the full degree.

For any nontorsion algebraic unit gamma, the small-body proof of L G0086 also gives the necessary bound

    sigma_*(gamma)>=1/(2m(gamma)).                        (13)

Indeed, for t>0 and 0<delta<1/4, its body of volume c_gamma delta^d exp(-nm) has Re Z_n>=n cos(2pi delta).
Thus (6) implies sigma t^2/2>=t cos(2pi delta)-m after division by n and passage to the limit.
Let delta decrease to zero and optimize at t=1/sigma.
This proves (13) for every admissible sigma and hence for their infimum.

Here phi^2=(3+sqrt(5))/2<8/3<e, so log phi<1/2 and sigma_*(phi)>1.
Therefore the admissible sigma=1 of the complete induction actually fails on this selected factor.
This example has selected measure phi, above the plastic constant; it is not a small-core obstruction or a Lehmer counterexample.
It isolates the false transfer itself.

<a id="irreducible-radical-house-control"></a>
## An irreducible unit family with house tending to one

This is the retained radical control of [C212 radical control](../claims/Yin_C_G0212_v1.md#radical-collision-control), now used to test the MGF cost.
Its elementary degree proof is recalled so that the full-extension hypothesis remains explicit.

Take beta_h=phi^(1/2^h)>0 for h>=0.
We prove inductively that

    P_h(t)=t^(2^(h+1))-t^(2^h)-1

is its irreducible minimal polynomial.
The base h=0 is the quadratic polynomial of phi.
If the statement holds at h, then the degree is even and Norm_(Q(beta_h)/Q)(beta_h)=-1.
Consequently beta_h is not a square in Q(beta_h), since the rational norm of a square is a rational square.
The polynomial x^2-beta_h is therefore irreducible over that field.
Adjoining the positive square root doubles the degree, and P_(h+1) has exactly that degree and vanishes there.
This proves the induction, without a general radical irreducibility theorem.

The family therefore satisfies

    degree(beta_h)=2^(h+1),
    M(beta_h)=phi,
    house(beta_h)=phi^(1/2^h) -> 1,
    sigma_*(beta_h)=sigma_*(phi)<=2,
    A_(n,r)(beta_h)<=(4e r n)^r  for every h,n,r.           (14)

The upper constant 2 follows from phi<2<phi^2.
In contrast, the direct house/Hölder prescription on beta_h would use ceil(2^h log2/log phi), which tends to infinity.
Thus that particular house cost is not an intrinsic necessity for all algebraic-unit families with house approaching one.

The limits are precise.
Their Mahler measures remain at the fixed number phi, above the plastic constant.
For h>=1, beta_h^(2^h)=phi has strictly smaller degree.
More generally, every nontrivial full k-fold extension in this note loses degree under its kth power.
Hence this construction does not belong to the all-positive-power-degree-preserving core used after the retained existence descent.
It does not provide common MGF or moment constants on that remaining core.

Likewise, varying the seed alpha without controlling its constant does not create a uniform estimate by induction.
Formula (7) preserves the exact seed cost rather than reducing it; (13) explains why that cost still has to respect its positive Mahler measure.
This is a real improvement over a house-only test on complete induced families, not a new uniform entropy gap or a replacement for the missing arithmetic estimate on the degree-stable small reciprocal units.

## Current proof and retained checking scope

The complete current statement and every original mathematical argument are retained in [C278](../claims/Yin_C_G0278_v1.md#argument), with its actual selected assessment.
The [current entire finding](../audits/reviews/Yin_R_G0534_v1.md#current-haar-induction-finding) is self-reviewed.
The [complete original checking account and exact findings](../audits/reviews/Yin_R_G0534_v1.md#historical-haar-author-finding) retain their original2026-10-07 inputs, mathematical contributions, actual scopes and limitations.
Original independent or collaborator wording does not supply unrecorded initial context or transfer an old finding to this new C.
