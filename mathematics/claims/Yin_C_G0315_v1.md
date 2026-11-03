---
author: Yin
---

# Fixed-input attainment and finite support for the relaxed trace amplitude

This retains the complete original 2026-10-07 [L114 argument](../ledger/Yin_L_G0114_v1.md).
The original ms25_source agent assembled this argument for Yin; the coordinator supplied the cluster mechanism and displayed quantitative split.
Original proof attribution and every actual old review retain their exact input/date scopes.
No current Task/E execution, source acquisition or mathematical program run is selected by this maintenance.

## Statement

Fix a hyperbolic algebraic unit alpha with monic irreducible polynomial P and M(P)>1.
For every nonzero finite integer forcing z whose response e=P(S)^(-1)z satisfies norm(e)_infinity<1/2, define Q(e)=product_j cos(pi e_j), and let A_free(P) be the supremum of this nonempty class.
It satisfies 0<A_free(P)<=exp(-pi^2/(2M(P)^2))<1 and A_free(P)^2<=c_opt(P)<=A_free(P).
For every certified 0<eta<A_free(P), the exact constants B,K,C,rho,delta,T,J_rho,kappa,G in (3)--(9) are finite and bound all candidates with Q(e)>=eta.
Every such candidate is dominated by a member of the finite strict-cube integer family with coefficients bounded by floor sqrt(B) and support in {0,...,(K-1)G} after translation.
Thus A_free(P)=max_{z in F}Q(P(S)^(-1)z), every maximizing forcing has every consecutive gap less than G, and there are finitely many maximizers modulo translation.
No exact comparison algorithm for infinite-product equality, uniqueness, c_opt attainment, degree-uniform amplitude floor, unit-circle extension or uniform Mahler gap is asserted.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T09:01 |
| status | open |
| reason | Retain the complete exact original theorem and argument; current whole checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Full original (1)--(10): threshold and integer coefficient/energy bounds, shifted Green constants, both half-lines and strict cube, mixed derivative rectangle and correlation constants, exact gap ceiling, strict improvement and finite termination, every maximizing translation and product-comparison/uniformity/residue limits. |
| argument | [Complete argument](#argument) | Full original (1)--(10): threshold and integer coefficient/energy bounds, shifted Green constants, both half-lines and strict cube, mixed derivative rectangle and correlation constants, exact gap ceiling, strict improvement and finite termination, every maximizing translation and product-comparison/uniformity/residue limits. |
| dependency | [Exact retained input](Yin_C_G0307_v1.md#relaxed-residue-amplitude-equivalence) | Nonemptiness, exponential tails, nonzero relaxed residue, square-cost comparison with the prescribed integral-multiplier class and explicit lower threshold. |
| dependency | [Exact retained input](Yin_C_G0308_v1.md#forcing-numerator-and-rounding-boundary) | Every nonzero integer forcing has energy at least M(P)^(-2), giving the strict amplitude cap used in cluster improvement. |
| dependency | [Exact retained input](Yin_C_G0304_v1.md#rounded-defect-residue-class) | Exact integer Laurent residue kernel, inverse shift convention and zero-class exclusion in the open cube. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T09:04 |
| status | proved |
| reason | Adopt the exact complete original theorem and retained argument after actual whole self-review with resolved used inputs, preserving all fixed-input, hypothesis and uniformity boundaries. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Full original (1)--(10): threshold and integer coefficient/energy bounds, shifted Green constants, both half-lines and strict cube, mixed derivative rectangle and correlation constants, exact gap ceiling, strict improvement and finite termination, every maximizing translation and product-comparison/uniformity/residue limits. |
| argument | [Complete argument](#argument) | Full original (1)--(10): threshold and integer coefficient/energy bounds, shifted Green constants, both half-lines and strict cube, mixed derivative rectangle and correlation constants, exact gap ceiling, strict improvement and finite termination, every maximizing translation and product-comparison/uniformity/residue limits. |
| dependency | [Exact retained input](Yin_C_G0307_v1.md#relaxed-residue-amplitude-equivalence) | Nonemptiness, exponential tails, nonzero relaxed residue, square-cost comparison with the prescribed integral-multiplier class and explicit lower threshold. |
| dependency | [Exact retained input](Yin_C_G0308_v1.md#forcing-numerator-and-rounding-boundary) | Every nonzero integer forcing has energy at least M(P)^(-2), giving the strict amplitude cap used in cluster improvement. |
| dependency | [Exact retained input](Yin_C_G0304_v1.md#rounded-defect-residue-class) | Exact integer Laurent residue kernel, inverse shift convention and zero-class exclusion in the open cube. |
| review | [Actual current whole self-review](../audits/reviews/Yin_R_G0549_v1.md#current-attainment-finding) | Exact current statement, complete original proof and directly used interfaces; self-reviewed, with every old checking relationship and exact original input retained separately. |

## Complete retained argument

<a id="argument"></a>
Let P be the monic irreducible polynomial of a hyperbolic algebraic unit alpha, with M=M(P)>1.
On bilateral sequences put (Sx)_j=x_(j+1).
For every nonzero finitely supported integer z for which e=P(S)^(-1)z satisfies ||e||_infinity<1/2, write

    Q(e)=product_(j in Z) cos(pi e_j),
    A=A_free(P)=sup Q(e).                               (1)

These are the relaxed forcings of [L G0110](Yin_C_G0307_v1.md#relaxed-residue-amplitude-equivalence).
The product is positive because every such inverse has exponential tails.
That record proves nonemptiness and A^2<=c_opt(P)<=A.
The integer-forcing Jensen bound of [L G0111](Yin_C_G0308_v1.md#forcing-numerator-and-rounding-boundary) applies to this entire relaxed class, so

    Q(e)<=u:=exp[-pi^2/(2M^2)]<1.                       (2)

Indeed ||e||_2^2>=M^(-2), and log cos(pi x)<=-pi^2 x^2/2.
In particular 0<A<=u<1, without assuming attainment.

<a id="amplitude-threshold-integer-support"></a>
### A product threshold bounds the integer data

Fix any certified number eta with 0<eta<A.
Such a number is available from the explicit positive lower bound in L G0110, for example half that bound.
Only candidates with Q(e)>=eta need to be considered.
Set

    r=arccos(eta)/pi,       delta=1/2-r>0,
    E_eta=-2log(eta)/pi^2,
    Q_P=max_(|t|=1)|P(t)|,
    B=Q_P^2 E_eta,          K=floor B.                  (3)

Since every cosine factor is at most one, Q(e)>=eta forces each factor to be at least eta; hence ||e||_infinity<=r.
The logarithmic bound used in (2) also gives ||e||_2^2<=E_eta.
Fourier isometry yields

    ||z||_2^2<=B,   ||z||_1<=||z||_2^2<=B,
    #supp(z)<=K,   |z_j|<=floor sqrt(B).                (4)

The l1 inequality uses integer coefficients.
Because there is a nonzero candidate above eta, K>=1.
This controls the number and sizes of coefficients, but does not yet control gaps in their locations.

Choose constants C>0 and 0<rho<1 such that the inverse kernel h=P(S)^(-1)delta_0 satisfies

    |h_j|<=C rho^|j|.                                  (5)

These constants may be chosen explicitly.
With

    rho=max(max_(|beta|<1)|beta|,
            max_(|beta|>1)|beta|^(-1)),
    C=rho^(-1) sum_beta |P'(beta)|^(-1),

the Green formula of L G0110 gives (5), because h_j=w_(j-1).
The factor rho^(-1) accounts for the impulse-index shift; all roots of the unit are nonzero.

<a id="quantitative-gap-splitting"></a>
### A sufficiently large gap permits strict improvement

Suppose consecutive support locations p<q of z have gap q-p>=G.
Split z=z_L+z_R at this gap, with both parts nonzero, and set e_L=P(S)^(-1)z_L and e_R=P(S)^(-1)z_R.
Then e=e_L+e_R.

On the half-line j<=floor((p+q)/2), the right response has absolute value at most BC rho^(G/2).
On the other half-line the same bound holds for the left response.
This follows from (4)--(5), since all forcing sites of the opposite part have distance at least G/2.
If

    BC rho^(G/2)<=delta/2,                             (6)

then both full responses satisfy

    ||e_L||_infinity, ||e_R||_infinity
                  <=t:=r+delta/2=1/2-delta/2<1/2.

On its own half-line use e_L=e-e_R, or e_R=e-e_L; on the opposite half-line use the small tail directly.
Thus both subforcings really belong to the relaxed class.
Their products Q_L and Q_R are positive and at most u by (2).

For L(x)=log cos(pi x), put

    T=pi^2 sec^2(pi t),
    J_rho=(1+sqrt(rho))/(1-sqrt(rho)).

At each coordinate the four numbers 0,e_L,e_R,e_L+e_R lie in [-t,t].
Every point x e_L+y e_R with 0<=x,y<=1 is in their convex hull.
The double integral of L'' therefore proves

    |L(e_L+e_R)-L(e_L)-L(e_R)|<=T |e_L e_R|.           (7)

For two forcing locations a,b with b-a>=G, the kernel correlation is bounded by

    sum_j |h_(j-a) h_(j-b)|
      <=C^2 rho^(|a-b|/2)
                  sum_j rho^((|j-a|+|j-b|)/2)
      <=C^2 J_rho rho^(G/2).

For the first inequality split the exponent in half and use |j-a|+|j-b|>=|a-b|.
For the second discard |j-b| from the remaining nonnegative exponent and sum the bilateral geometric series.
Summing over the coefficient pairs and using (4) now gives

    |log Q(e)-log Q_L-log Q_R|
                <=T B^2 C^2 J_rho rho^(G/2).           (8)

All sums are absolutely convergent by the exponential kernel and finite forcing.
No independence of the two responses or probability interpretation is used.

Write kappa=-log u=pi^2/(2M^2)>0.
Choose an integer G>=1 so that (6) holds and the right side of (8) is at most kappa/2.
This is an explicit finite choice: with

    R=min(1,delta/(2BC),
                 kappa/(2T B^2 C^2 J_rho)),
    G=max(1,ceil[2log(1/R)/log(1/rho)]),                (9)

both requirements hold.
Consequently

    Q(e)<=exp(kappa/2)Q_L Q_R
          <=exp(-kappa/2)max(Q_L,Q_R),

so the better subforcing has amplitude at least exp(kappa/2)Q(e)>Q(e).
It remains above eta and has strictly fewer nonzero forcing coefficients.

<a id="relaxed-amplitude-finite-attainment"></a>
### An explicit finite family contains every maximizer

Starting from any candidate with Q(e)>=eta, repeatedly keep the better subforcing whenever a consecutive support gap is at least G.
Every step is a strict improvement and preserves the threshold; the number of nonzero integer coefficients strictly decreases.
The process therefore stops after at most K-1 steps.
At its end all consecutive gaps are smaller than G.
After a common integer shift the support is contained in

    {0,...,(K-1)G},

and it still obeys (4).
Let F be the finite set of nonzero integer forcings in that interval satisfying the coefficient bounds in (4) and the strict inverse cube condition.
The preceding reduction proves

    boxed: A_free(P)=max_(z in F) Q(P(S)^(-1)z).        (10)

To justify the global assertion, A>eta supplies an above-threshold candidate, so F is nonempty.
Every candidate above eta is dominated by one in F, and candidates below eta cannot reach the maximum already present in F.
The reverse inequality is immediate because F is a subset of the original class.

In particular the relaxed supremum is attained by a nonzero finite integer forcing.
Every maximizing forcing already has all gaps smaller than G, since otherwise (9) would strictly improve it.
Thus there are only finitely many maximizers modulo common integer translation.
Neither uniqueness modulo translation nor uniqueness up to sign is asserted.

The open cube also automatically rules out zero residue: if Phi(z)=0, the L G0107 kernel identity would give z=P(S)q with finite integer q; invertibility then gives e=q, and ||e||_infinity<1/2 forces q=0.
This observation is consistent with the relaxed definition, which drops the prescribed nonzero integral-multiplier class rather than allowing a hidden zero-class maximizer.

### Meaning and limits of the finite reduction

Formula (10) is a finite candidate theorem with explicit input-dependent support, coefficient and gap bounds.
It is not a claim that an exact optimizer comparison program terminates on every transcendental equality between infinite cosine products.
No such program has been run or supplied here.
The products are well-defined limits, and the finite maximum exists regardless of a comparison algorithm.

The theorem fixes P throughout.
The constants eta, C, rho, Q_P and hence K and G may deteriorate along an unbounded-degree, small-Mahler sequence.
It does not supply a degree-independent lower amplitude.
Nor does it prove attainment of c_opt(P): the prescribed residue condition need not survive discarding one cluster.
L G0110 still gives only A_free(P)^2<=c_opt(P)<=A_free(P).

The changed arithmetic target is a finite bounded forcing problem for each fixed polynomial, with the remaining task being uniform control of its costs over the intended core.
There is no Lehmer-gap claim and no unit-circle extension.
