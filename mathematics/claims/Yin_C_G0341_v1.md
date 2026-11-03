---
author: Yin
---

# Explicit finite-energy coercivity with complete cluster collars and coefficient-only constants

This retains the complete original 2026-10-08 [L135 mathematical argument](../ledger/Yin_L_G0135_v1.md).
The entropy_status agent supplied cluster closure, algebraic-norm exclusion and coefficient constants; the coordinator checked the mechanism and supplied boundary telescoping, disjoint-block normalization and spectral constants.
No current Task/E execution, source acquisition, mathematical program run or algorithm implementation is selected by this maintenance.

## Statement

Fix the monic irreducible unit polynomial P of degree d, with positive logarithmic Mahler measure and a unit-circle root, and exactly the original finite closed-cube energy E_R with integer P(S)x and nonzero origin defect.
For every rational B>0, the full constants (2)--(3) and K=floor(W^2 B) iterations (4) yield an explicit R_crit(P,B) such that every integer R>=R_crit satisfies E_R>B, including K=0 and empty feasible sets.
The proof retains both disjoint-block families, all boundary and recurrence indices, exact Laurent signs, norm factors, monic integral quotient/support, two-ended spectral control with full Gamma cost and the final s_K collar step.
The coefficient-only rational replacement (17)--(18) retains the Cauchy, Vandermonde-minor, integral discriminant and Mahler coefficient bounds and gives a valid larger radius without root isolation.
All P,B dependence and K-fold iterated cost remain explicit; there is no numerical run, practical complexity, logarithmic lower growth, product lower bound or contradiction for a varying near-one family.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T10:12 |
| status | open |
| reason | Retain the complete exact original theorem and argument; actual current whole checking and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original (1)--(18) and all cost/scope consequences: exact original domain and finite energy, Young/support/K0 case, both collars and boundary states, Laurent signs, algebraic norm, integral quotient/support, two-ended recurrence constants, final s_K step/strict compactness, rational coefficient-only radius and all limits. |
| argument | [Complete argument](#argument) | Entire original (1)--(18) and all cost/scope consequences: exact original domain and finite energy, Young/support/K0 case, both collars and boundary states, Laurent signs, algebraic norm, integral quotient/support, two-ended recurrence constants, final s_K step/strict compactness, rational coefficient-only radius and all limits. |
| dependency | [Exact retained input](Yin_C_G0335_v1.md#finite-rational-energy-coercivity) | Exactly the unchanged finite rational closed-cube problem and positive-Mahler irreducible-unit/central-root domain. |
| dependency | [Exact retained input](Yin_C_G0337_v1.md#tunable-salem-finite-energy-envelope) | Application only to the actual enlarged-product upper test, retaining every fixed-input cost; no transition lower bound. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T10:16 |
| status | proved |
| reason | Adopt the complete exact original theorem and retained argument after actual current whole self-review, retaining all quantifiers, source depths, original checking inputs, explicit costs and unexecuted/nonuniform limits. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire original (1)--(18) and all cost/scope consequences: exact original domain and finite energy, Young/support/K0 case, both collars and boundary states, Laurent signs, algebraic norm, integral quotient/support, two-ended recurrence constants, final s_K step/strict compactness, rational coefficient-only radius and all limits. |
| argument | [Complete argument](#argument) | Entire original (1)--(18) and all cost/scope consequences: exact original domain and finite energy, Young/support/K0 case, both collars and boundary states, Laurent signs, algebraic norm, integral quotient/support, two-ended recurrence constants, final s_K step/strict compactness, rational coefficient-only radius and all limits. |
| dependency | [Exact retained input](Yin_C_G0335_v1.md#finite-rational-energy-coercivity) | Exactly the unchanged finite rational closed-cube problem and positive-Mahler irreducible-unit/central-root domain. |
| dependency | [Exact retained input](Yin_C_G0337_v1.md#tunable-salem-finite-energy-envelope) | Application only to the actual enlarged-product upper test, retaining every fixed-input cost; no transition lower bound. |
| review | [Actual current whole self-check](../audits/reviews/Yin_R_G0560_v1.md#current-explicit-coercivity-finding) | Complete current statement and retained proof with every directly used interface; self-reviewed. Old findings retain their exact actual dates, inspected inputs, corrections and relationships. |

## Complete retained argument

<a id="argument"></a>
Use the domain of [L G0130](Yin_C_G0335_v1.md#finite-rational-energy-coercivity): P(t)=sum_(i=0)^d p_i t^i is the monic irreducible minimal polynomial of an algebraic unit with positive logarithmic Mahler measure and at least one unit-circle conjugate.
All roots are distinct and nonzero.
Write

    W=sum_i |p_i|,  Z=floor(W/2),  M=M(P)>1,
    C_1=sum_i i |p_i|.

In particular W>=2 and Z>=1.
This result concerns exactly the finite problem of L G0130:

    I_R={-R,...,R+d},
    K_R={x in [-1/2,1/2]^(I_R):
         z_j=sum_i p_i x_(j+i) is an integer for -R<=j<=R,
         z_0 !=0},
    E_R=min_(x in K_R) sum_(j in I_R) x_j^2,              (1)

with E_R=infinity if the set is empty.
No optimizer is computed here.
We give a finite explicit radius after which E_R exceeds a prescribed rational energy threshold.
This strengthens the earlier qualitative divergence by a very large quantitative bound; it is not an efficient rate or a uniform near-one estimate with suppressed parameters.

<a id="explicit-finite-energy-coercivity-radius"></a>
### Constants and the coercivity statement

List the roots beta_1,...,beta_d of P, and let

    V=(beta_i^j)_(0<=j<=d-1,1<=i<=d),
    Gamma=sum_(i,j) |(V^(-1))_(i,j)|.                   (2)

These constants are finite.
Let B>0 be rational and put

    K=floor(W^2 B).

For every integer ell>=0 define the positive integers

    A(ell)=Z(ell+1),
    T(ell)=1+ceil[4 C_1^2 B A(ell)^(2(d-1)) M^(2ell)
                    +16 Gamma^2 B],
    L(ell)=d T(ell).                                  (3)

Certified upper bounds for C_1, Gamma and M may replace them in (3).
In particular a completely rational coefficient-only choice will be supplied below.
L is nondecreasing in ell.
Define integers

    s_0=0,
    s_(j+1)=s_j+L(s_j),       0<=j<K,
    R_crit(P,B)=s_K.                                  (4)

Then the explicit lower statement is

    R>=R_crit(P,B)  implies  E_R>B.                    (5)

When K=0, R_crit=0 and (5) follows immediately from the integer defect count proved next.
For K>=1, the argument uses at most K successive enlargements of a defect cluster.
The formulas retain the dependence on B, degree, coefficients, root separation through Gamma, and Mahler measure.
There is no hidden compactness choice.

### Energy bounds the number and size of integer defects

Suppose x is feasible in (1) and has energy at most B.
Extend x by zero outside I_R only for this estimate.
Young's finite-convolution inequality gives

    sum_(j=-R)^R z_j^2 <= W^2 sum_(j in I_R) x_j^2
                         <=W^2 B.                     (6)

Indeed the full squared norm of sum_i p_i x_(j+i) is at most W^2 ||x||_2^2, and discarding its exterior indices cannot increase it.
Every nonzero integer defect contributes at least one, so there are at most K such defects in [-R,R].
Also the cube gives

    |z_j|<=W/2,  hence |z_j|<=Z.                       (7)

Since z_0 is nonzero, K>=1 is necessary for such an x.
This is an actual support-count consequence of the assumed energy bound, not an assumption on defect positions or a relaxation of the cube.

### A finite cluster cannot have two sufficiently long empty collars

Let [a,b] be an integer interval containing zero and at least the nonzero defect at zero.
Put ell=b-a and L=L(ell).
Suppose its two collars stay inside the constrained defect interval and are empty:

    [a-L,b+L] subset [-R,R],
    z_j=0 for a-L<=j<a and for b<j<=b+L.                (8)

There may be zero defects inside [a,b]; they cause no problem.
We will derive a contradiction to energy at most B.

Write T=T(ell), so L=dT.
The left collar contains the following T disjoint blocks of d consecutive x-coordinates:

    [a-hd,a-(h-1)d-1],             1<=h<=T.

The right collar contains the T disjoint blocks

    [b+1+(h-1)d,b+hd],            1<=h<=T.

All these coordinates belong to I_R.
On each side the sum of block energies is at most B.
Thus there are starting indices l and r for one left and one right block such that, with X_j=(x_j,...,x_(j+d-1)),

    ||X_l||_2<=sqrt(B/T),  ||X_r||_2<=sqrt(B/T),
    a-L<=l<=a-d,  b+1<=r<=b+L-d+1.                    (9)

In particular the whole defect cluster lies between l and r-1.

Fix any unit-circle root beta of P.
Define the nonzero integer cluster polynomial

    Z_c(t)=sum_(j=a)^b z_j t^(b-j),
    deg Z_c<=ell,  ||Z_c||_1<=A(ell).                  (10)

The subscript distinguishes this polynomial from the integer coefficient bound Z.
It is nonzero because z_0!=0.
The empty collars and P(beta)=0 give the exact boundary identity

    beta^(-b-1) Z_c(beta)
      =sum_(j=l)^(r-1) z_j beta^(-j-1)
      =sum_(i=0)^d p_i beta^(i-1)
         [sum_(u=r)^(r+i-1) x_u beta^(-u)
             -sum_(u=l)^(l+i-1) x_u beta^(-u)].         (11)

For i=0 both inner sums are empty.
To derive it, substitute the definition of z, reindex u=j+i, and subtract the common sum on [l,r-1], whose coefficient is beta^(-1)P(beta)=0.
Every boundary coordinate in (11) lies in one of the two complete states in (9).
Since |beta|=1, the identity yields

    |Z_c(beta)|<=C_1(||X_l||_infinity+||X_r||_infinity)
                  <=2 C_1 sqrt(B/T).                  (12)

No inverse Vandermonde or separation of different central roots is needed for this scattering estimate.

If Z_c(beta)!=0, irreducibility makes its algebraic norm a nonzero integer.
For any conjugate beta_i,

    |Z_c(beta_i)|<=A(ell) max(1,|beta_i|)^ell.

Multiplying this estimate at all conjugates other than beta gives

    |Z_c(beta)|>=A(ell)^(-(d-1)) M^(-ell).              (13)

The omitted central conjugate has modulus one and contributes no Mahler factor.
There is no claim that all conjugates are central.
By (3), T>4 C_1^2 B A(ell)^(2(d-1)) M^(2ell), so (12) is strictly smaller than the right side of (13).
Therefore Z_c(beta)=0.
Irreducibility implies P divides Z_c in Q[t]; monic polynomial division then gives

    Z_c=P Q_c,  Q_c in Z[t],  Q_c!=0.                  (14)

If deg Z_c<d, divisibility is already impossible.
Otherwise write Q_c(t)=sum_j w_j t^(b-j), extending w by zero outside its finite support.
Since deg Q_c<=ell-d and its order at zero is nonnegative,

    supp(w) subset [a+d,b],
    w is a nonzero integer sequence,
    P(S)w equals z on [a,b] and zero elsewhere.         (15)

The last identity follows by taking coefficients of t^(b-j) in P(t)Q_c(t)=Z_c(t).
It does not require a guessed sign or an omitted Laurent shift.
If the extreme cluster coefficients vanish, the support inclusion only becomes smaller.

Let v=x-w on the available coordinates between l and r+d-1.
On every recurrence index l<=j<r, (8) and (15) give P(S)v_j=0.
Both states X_l and X_r of w are zero: the left block ends at a-1 and the right starts after b.
Thus v has the same boundary states as x in (9).

For completeness, the homogeneous companion recurrence has state eigenvectors (1,beta_i,...,beta_i^(d-1)), the columns of V.
At an interior index j in [a,b], express a mode using its coefficient from the left state when |beta_i|<=1 and from the right state when |beta_i|>1.
The respective propagation factors are beta_i^(j-l) and beta_i^(j-r), both of modulus at most one.
Applying V^(-1) to those boundary states and summing absolute values therefore gives

    |v_j|<=2 Gamma sqrt(B/T)<1/2,      a<=j<=b.         (16)

The factor two is a harmless upper bound for the two groups of modes; retaining the actual disjoint row sums is slightly sharper.
The strict final inequality follows from T>16 Gamma^2 B.
This two-sided estimate is uniform in ell; it does not propagate an expanding mode from the wrong endpoint or accumulate an uncharged factor depending on the length of the core.

Some w_j in [a+d,b] is a nonzero integer.
But |x_j|<=1/2 and (16) imply |w_j|=|x_j-v_j|<1, a contradiction.
This proves that no interval satisfying (8) can occur for a feasible vector of energy at most B.

### Closing the cluster with all finite indices retained

Suppose now R>=s_K and such an x exists.
Start with [a_0,b_0]=[0,0].
After j enlargements, maintain a cluster interval containing zero and at least j+1 distinct nonzero defects, with span at most s_j.
Its endpoints have absolute values at most its span, because it contains zero.
Since L is nondecreasing, the two collars of its current length L(b_j-a_j) lie inside

    [-s_j-L(s_j),s_j+L(s_j)]=[-s_(j+1),s_(j+1)].

For j<K these collars lie inside [-R,R].
The preceding result says they cannot both be empty.
Choose one nonzero defect from either collar and enlarge the interval just enough to include that point.
It was outside the former interval and is a new defect.
The span increases by at most L(b_j-a_j), hence the new span is at most s_(j+1).
This proves the induction step.

At j=K-1 the same step would give K+1 distinct nonzero defects in [-R,R], contradicting (6).
Thus no feasible x has energy at most B.
Compactness of each K_R ensures that its minimum, if finite, is attained.
It follows that E_R>B, proving (5), including its strict comparison and the closed cube.

<a id="coefficient-only-coercivity-radius"></a>
### An explicit coefficient-only version

The radius can be evaluated using rational arithmetic alone, without root isolation.
Set

    H=1+W,
    D_0=(d-1)! H^((d-1)^2).

Cauchy's root bound gives |beta_i|<=H.
Each entry of V has modulus at most H^(d-1).
A Leibniz expansion bounds every (d-1)-minor by D_0.
Since P is monic and separable, det(V)^2 is its nonzero integer discriminant up to the usual sign; thus |det(V)|>=1.
Cramer's rule therefore gives

    Gamma<=d^2 D_0,
    C_1<=dW,
    M(P)<=W.                                            (17)

The last inequality follows from the Mahler integral bound by the coefficient l1 norm.
Consequently replace (3) by

    T_bar(ell)=1+ceil[4d^2 W^2 B [Z(ell+1)]^(2(d-1))
                                    W^(2ell)
                          +16d^4 D_0^2 B],
    L_bar(ell)=d T_bar(ell),                             (18)

and iterate (4) with L_bar.
Every quantity in (18) is rational or integer for rational B, and all comparisons and ceilings are exact.
The resulting R_bar(P,B) is a valid possibly larger coercivity radius.
It depends explicitly only on d,W,B.
Formula (17) retains the potentially large root-separation cost through this coefficient bound rather than treating the Vandermonde inverse as uniformly bounded.

For a concrete integer R one therefore has the quantitative lower certificates E_R>B for every positive rational B whose computed radius is at most R.
For any supplied P and B this is an explicit finite bound on how far an energy-exclusion search ever needs to go; it is not merely the earlier assertion that such a radius exists.

### Cost and mathematical scope

For M>1, one application of L(ell) is bounded by an explicit polynomial in ell times an exponential in ell, with the displayed P and B parameters.
The construction iterates that operation K=floor(W^2 B) times.
The coefficient-only version can be much larger still.
These are very large iterated bounds; no claim of practical computation, a logarithmic lower growth rate, or useful near-one uniformity follows.

The earlier logarithmic feasible upper witnesses are compatible with this much weaker explicit lower growth.
The present proof does not alter those witnesses or the exact finite-energy problem.
It uses the integer defect support bound, long zero-defect collars, an integer algebraic norm, and the closed-cube obstruction at a finite integer response; it does not replace the cube by an unconstrained least-squares problem.

Applied to the [actual-product upper test of L G0132](Yin_C_G0337_v1.md#tunable-salem-finite-energy-envelope), this theorem can supply an explicit finite energy threshold or a termination radius while retaining every P-dependent cost.
It supplies no transition-product lower bound and no contradiction for a whole varying near-one family.
No assumption that such a family exists is made, and G0001 remains unresolved.
