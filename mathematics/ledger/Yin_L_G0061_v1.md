---
author: Yin
---

# G0001: an integral adjoint quotient and its powered-discriminant periodic counts

Date: 2026-10-07.

The complete mathematical proof is now retained in [C236](../claims/Yin_C_G0236_v1.md#integral-adjoint-quotient).
This original dated input remains available with its full mathematics; formal review accounts are retained in [R517](../audits/reviews/Yin_R_G0517_v1.md#historical-adjoint-author-finding).
Bounded construction by assigned AI review_matrix_completion for Yin, with the coordinator's proposed commutator-torsion interpretation checked directly below.
This continues the order-index identities of [L G0059](Yin_L_G0059_v1.md#powered-order-index).
No new source or computation is used.
The entropy and periodic-growth inputs retain their already accepted source scopes.

The outcome is an actual free integral quotient flow whose toral periodic counts are the powered polynomial discriminants, together with a precise torsion interpretation of the squared order indices.
Its entropy is between d and 2(d-1) times the original Mahler logarithm.
A uniform gap after dividing this new entropy by d is therefore an equivalent target, not a consequence of the construction.
The finite-cost comparison below makes that boundary explicit.

<a id="integral-adjoint-quotient"></a>
## The saturated centralizer and an explicit free quotient

Let alpha be a nonzero nontorsion algebraic unit with monic minimal polynomial P in Z[t], degree d>=2, and assume

    deg(alpha^n)=d       for every n>=1.                 (1)

The all-positive-power norm descent in [L G0059](Yin_L_G0059_v1.md#all-positive-power-existence-descent) legitimizes this restriction for gap or nonattainment existence questions.
It does not assert (1) for an arbitrary original input.

Write alpha_1,...,alpha_d for the conjugates, set

    m=m(P),       Delta=|disc P|,
    I_n=[Z[alpha]:Z[alpha^n]],

and let A in GL_d(Z) be the companion matrix in the power basis e_0,...,e_(d-1), so A^j e_0=e_j for 0<=j<d.
On

    E=End_Z(Z^d)=M_d(Z)

consider the integral automorphism

    Ad_A(B)=A B A^(-1).

Its integral centralizer is exactly

    C=C(A)={B:AB=BA}=Z[A],

with basis I,A,...,A^(d-1).
Indeed a commuting B is determined by v=B e_0, because B e_j=A^j v.
If v=sum_i v_i e_i, this is exactly the action of sum_i v_i A^i.
Conversely every such polynomial commutes with A.

Evaluation at e_0 restricts to an isomorphism C -> Z^d.
In particular the map

    r(B)=sum_i (B e_0)_i A^i

is an integral retraction E -> C.
Therefore C is a saturated direct summand, and

    L=E/C is free of rank D_ad=d(d-1).                  (2)

It can be represented explicitly by matrices with first column zero, using pi(B)=B-r(B).
Ad_A fixes C pointwise, so it induces an integral automorphism T of L.
In the preceding representative lattice it is

    T(B)=pi(A B A^(-1)),
    T^(-1)(B)=pi(A^(-1) B A).

This describes an actual GL_(D_ad)(Z) action; it does not replace an integral lattice by a rational vector space or silently discard torsion.

<a id="adjoint-ratio-spectrum"></a>
## Characteristic polynomial and the no-root-of-unity condition

Over C the matrix A is diagonalizable, since P is separable.
On the corresponding matrix units, Ad_A has eigenvalues alpha_i/alpha_j.
The centralizer becomes the d-dimensional diagonal subspace.
Consequently

    R(t)=chi_T(t)=product_(i!=j)(t-alpha_i/alpha_j).      (3)

This polynomial is monic integral because it is the characteristic polynomial of the integral quotient automorphism.
Its roots occur with their inverses, its degree d(d-1) is even, and their product is one.
Thus R has constant coefficient one and is reciprocal.
Repeated ratios and repeated irreducible factors are allowed; no squarefree or irreducibility assertion about R is needed.

Condition (1) says exactly that no ratio alpha_i/alpha_j with i!=j is a root of unity: a root-of-unity ratio is equivalent to equality of two conjugate powers at some positive exponent.
Therefore R has no root-of-unity root, and T^n-I is nonsingular for every n>=1.
This does not exclude other unit-circle eigenvalues.
In particular Salem inputs do not make this an expansive toral system.

Also Q[A^n]=Q[A] for every n by (1), so the integral centralizer of A^n is the same saturated C.
It need not equal Z[A^n]: that order has index I_n in C.
This distinction is essential in the torsion calculation below.

<a id="adjoint-periodic-discriminant"></a>
## Exact finite toral periodic counts

Let X=Hom(L,R/Z), the compact dual torus of dimension D_ad, with dual automorphism T_hat.
For each n the finite group of fixed points is dual to L/(T^n-I)L, and therefore

    F_n:=|Fix(T_hat^n)|
        =|L/(T^n-I)L|
        =|det(T^n-I)|.                                (4)

One can check the cardinality directly by a basis and Smith normal form of the nonsingular integer matrix T^n-I.
This is a toral periodic count: on the discrete torsion-free group L itself, T^n-I is injective and its only fixed point is zero.

Put beta_i=alpha_i^n.
Formula (3) gives

    |det(T^n-I)|
      =|product_(i!=j)(beta_i-beta_j)
             /product_j beta_j^(d-1)|
      =|disc P^[n]|,

because the denominator has absolute value one for a unit.
The order-index identity in L G0059 now yields the exact formula

    F_n=|disc P^[n]|=Delta I_n^2.                       (5)

In particular F_1=Delta and F_n/F_1 is an integer square.
If a divides b, the order-index cocycle makes F_b/F_a an integer square as well.
These are exact restrictions on this class of periodic counts.
They do not by themselves give a uniform exponential rate.

<a id="commutator-torsion-index"></a>
## The squared index is actual commutator torsion

The matrix trace pairing

    <B,D>=tr(BD)

is a unimodular integral pairing on E: the matrix-unit basis is paired by E_(ij) with E_(ji).
Write C^perp for the annihilator of C under this pairing.
Since C is primitive, restriction gives a surjective map

    rho:E -> C^*=Hom_Z(C,Z),
    rho(B)(c)=tr(Bc),       ker rho=C^perp.              (6)

Surjectivity follows by extending an integral functional on the direct summand C to E and then using the unimodular pairing.

For the companion A, the image of the commutator map is saturated:

    [A,E]=C^perp.                                      (7)

Here is a direct integral proof of the required saturation.
Write P(t)=t^d+sum_(j=0)^(d-1) p_j t^j.
If the columns of B and [A,B] are b_j and c_j, respectively, the first d-1 equations are

    b_(j+1)=A b_j-c_j,       0<=j<d-1.

After these substitutions, the last equation becomes Phi(c)=0, where

    Phi(c)=c_(d-1)+sum_(r=0)^(d-2)
       [A^(d-1-r)+sum_(j=r+1)^(d-1) p_j A^(j-1-r)] c_r.

The dependence on b_0 vanishes because P(A)=0.
Conversely, if this relation holds, start with b_0=0 and the recursion solves every column equation.
Phi:E -> Z^d is surjective because its last-column coefficient is I.
Thus [A,E]=ker Phi and its cokernel is free of rank d.
Trace cyclicity gives [A,E] subset C^perp; both are saturated lattices of rank d(d-1) with the same rational span, so they are equal.
This proof does not presume (5) or infer saturation from an equality of determinants.

For any n, multiplication by A^(-n) is an integral automorphism of E and

    (Ad_A^n-I)(B)=[A^n,B A^(-n)].

Hence im(Ad_A^n-I)=[A^n,E] exactly.
Its rational kernel is C_Q by (1), and its image is contained in C^perp with full rank there.
It follows that

    Tau_n:=C^perp/[A^n,E]
         =torsion subgroup of E/[A^n,E].              (8)

This finite group need not be trivial when n>1.
The centralizer stays C while the generated order Z[A^n] can have nontrivial index.

The trace pairing on C is nondegenerate over Q: it is the field trace pairing on Q(alpha).
In its power basis the Gram determinant is disc P, since the Gram matrix is the product of a Vandermonde matrix with its transpose.
In particular C intersection C^perp=0, and

    D_C:=C^*/rho(C)       has order Delta.              (9)

Combining (6) with the quotient L=E/C gives the exact sequence

    0 -> Tau_n -> L/(T^n-I)L -> D_C -> 0.              (10)

To check exactness directly, the middle group is E/(C+[A^n,E]).
Its map to C^*/rho(C) is induced by rho and is onto.
Its kernel is (C+C^perp)/(C+[A^n,E]), which is C^perp/[A^n,E] because C intersection C^perp=0.
Equations (5) and (9) now give

    |Tau_n|=I_n^2.                                    (11)

Thus the squared monogenic-order index is the order of a concrete torsion subgroup in a commutator cokernel.
There is no claim of a canonical direct splitting of (10).
At n=1, (7) gives Tau_1=0, and the middle group is exactly the trace-discriminant group D_C.

<a id="adjoint-entropy-comparison"></a>
## Exact entropy and sharp comparison to the original flow

The rational Algebraic Yuzvinski Formula is reused at its accepted scope in [GBV15-U001](../audits/literature/GBV15/Yin_U001.md#gbv15-u001).
It applies to T on L tensor Q and gives m(R), since R is already monic integral.
The entropy on L agrees: any finite subset of the rational space can be multiplied by one integer into L; scaling commutes with T and preserves every finite trajectory cardinality.
Thus taking the supremum over finite sets gives equality, without adding a new rationalization theorem.

Let

    x_i=log|alpha_i|,
    sum_i x_i=0,       m=sum_i max(x_i,0),
    h_ad=h_alg(T on L).

The zero sum uses the unit hypothesis.
From (3),

    h_ad=m(R)
        =sum_(i<j)|x_i-x_j|.                          (12)

The retained toral formula in [Smy08-U004](../audits/literature/Smy08/Yin_U004.md#smy08-toral-entropy) also identifies this with h_top(T_hat), with no dimension divisor.
These external entropy formulas retain their stated inspection boundaries; their original proofs are not newly audited here.

The sharp comparison is

    d m <= h_ad <= 2(d-1)m.                            (13)

For the lower bound, for each i the triangle inequality gives

    sum_j |x_i-x_j| >= |sum_j(x_i-x_j)|=d|x_i|.

Sum in i and use sum_i|x_i|=2m.
Equality holds precisely when every x_i is either the minimum or the maximum of the list; since m>0, this means exactly two distinct logarithmic moduli.
Their values must have opposite signs.
For the upper bound sum |x_i-x_j|<=|x_i|+|x_j| over unordered pairs.
Equality holds precisely when no two x_i are positive and no two are negative.
Since their sum is zero and m>0, the exact pattern is

    one x_i=m,       one x_j=-m,
    all remaining x's zero.                           (14)

For a Salem polynomial this is its usual root-modulus pattern, so

    h_ad=2(d-1)m       in the Salem case.               (15)

The same holds for a sign-twisted Salem polynomial.
Every quadratic unit has equality in both bounds.
More generally (14), rather than an assumed Salem-only reduction of the original problem, is the precise equality condition.
In the reciprocal core the lower-bound equality means d/2 conjugates at each of two reciprocal nonunit moduli, with no unit-circle conjugates.

There is also an exact way to display the contribution of neutral conjugates.
If z is the number of zero x_i and V_+,V_- are the sums |x_i-x_j| within the positive and negative lists respectively, then

    h_ad=(d+z)m+V_++V_-.                               (16)

The cross-sign pairs contribute (d-z)m and the pairs with zeros contribute 2zm.
This verifies the comparison and Salem value without discarding neutral conjugates or dividing the original algebraic entropy by degree.

<a id="adjoint-index-growth"></a>
## Periodic growth and its exact source boundary

For this integral toral automorphism, all eigenvalues are algebraic and none is a root of unity.
The retained War05 periodic-growth interface, recorded at [S G0004](../strategies/Yin_S_G0004.md#periodic-resultant-interface) and its source locator, therefore applies:

    lim_(n->infinity) log F_n/n=h_ad.

Its treatment of algebraic eigenvalues on the unit circle uses the accepted Baker input; that proof is not reproduced or strengthened here.
No expansiveness assumption is inserted.
Together with (5) and (11), this gives

    lim log I_n/n=h_ad/2,
    lim log|Tau_n|/n=h_ad.                             (17)

These are pointwise limits for each fixed input.
They provide no uniform convergence time or degree-independent lower growth rate.
Nor are they assertions about periodic points on arbitrary compact abelian groups or on the discrete lattice itself.
The elementary simultaneous-torus-return argument in [L G0062](Yin_L_G0062_v1.md#adjoint-periodic-index-boundary) proves the corresponding limsup without the additional Diophantine input.
Its other conclusions about whole-family entropy and the reciprocal invariant subgroup have their separate stated scopes.

<a id="adjoint-normalized-target-boundary"></a>
## What the construction does and does not improve

The arithmetic output is the integral quotient, the exact sequence (10), and the identification of powered order indices with its torsion and periodic counts.
These structures retain information beyond a bare nonzero integer determinant.
The growth normalization still has to be paid for.

Indeed (13) says

    m <= h_ad/d <= 2(1-1/d)m.                          (18)

Thus a positive absolute lower bound on h_ad/d throughout these all-power-stable unit inputs is equivalent, up to these explicit constants and the L G0059 existence reduction, to the original positive Mahler gap on units.
It is a target reformulation, not a theorem supplied by the construction.
A bound only on the ordinary entropy h_ad>=c would imply merely m>=c/[2(d-1)].
The divisor d in (18) is the original field degree, not the new lattice rank d(d-1).

There is a direct finite-cost diagnostic too.
From the individual ratio factors,

    F_n<=2^(d(d-1)) exp(n h_ad).

Using (13) would give the valid sufficient lower estimate

    m >= [log Delta+2log I_n-d(d-1)log 2]
             /[2n(d-1)].                              (19)

But ordinary Vandermonde and Hadamard at the d roots of P^[n] already give

    Delta I_n^2 <= d^d M(P)^(2n(d-1)),
    m >= [log Delta+2log I_n-d log d]/[2n(d-1)].        (20)

Since 2^(d-1)>=d for d>=2, (20) is at least as strong as (19).
Thus the generic norm estimate on the new ratio-spectrum flow does not improve the old powered-discriminant finite certificate.
The ordinary integrality of I_n, the fixed square class of F_n and the pointwise limit (17) likewise do not establish the missing uniform rate.
A further argument would need a quantitative restriction on these actual lattices or torsion groups that survives the d and time costs, rather than renaming (18) as a gap.

<a id="integral-adjoint-review"></a>
## Actual review and scope

Original drafting, coordinator, assigned-whole and commutator/whole accounts are retained in [R517](../audits/reviews/Yin_R_G0517_v1.md#historical-adjoint-author-finding).
The original 2026-10-07 date, actual contributions and full check scopes remain there, with current finding-specific relationships.
No new source, computation, uniform arithmetic estimate or resolution of G0001 is asserted.
