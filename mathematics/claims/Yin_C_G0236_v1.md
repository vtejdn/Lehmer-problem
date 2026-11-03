---
author: Yin
---

# Complete integral adjoint quotient, torsion indices and invariant-subgroup boundary

This retains both complete original 2026-10-07 arguments of [L61](../ledger/Yin_L_G0061_v1.md) and [L62](../ledger/Yin_L_G0062_v1.md), with their original local equation numbering.
The actual quotient lattice, exact trace/torsion sequence, entropy comparisons, finite-sublevel proof, reciprocal subgroup and elementary torus-return proof are physically retained.
The fixed-input full periodic limit remains an accepted external input at its original War05/Baker depth; no new source proof or research calculation is performed.

## Statement

Let alpha be any nonzero nontorsion algebraic unit of degree d>=2, with monic irreducible polynomial P, conjugates alpha_i, original companion A in GL_d(Z), m=logM(P)>0 and Delta=abs(discP).
A. On E=M_d(Z) the centralizer C(A)=Z[A] is a saturated direct summand, with the explicit integral retraction r(B)=sum_i(Be_0)_i A^i.
The literal quotient L=E/C is free of rankD=d(d-1), and conjugation induces an actual invertible integral actionT represented by pi(ABA^(-1)) on first-column-zero representatives.
Its characteristic polynomial is

    R(t)=product_(i!=j)(t-alpha_i/alpha_j),

monic integral reciprocal of constant1, with repeated ratios and factors allowed.
The separate integral companion ofR has the same characteristic polynomial and total entropy, without claiming integral conjugacy of the two models.
Writing x_i=logabs(alpha_i), sum_i x_i=0 and m=(1/2)sum_i abs(x_i), both algebraic entropy on the lattice and the dual toral topological entropy equal

    h_ad=m(R)=sum_(i<j)abs(x_i-x_j),
    d m<=h_ad<=2(d-1)m.

The lower equality has exactly two distinct logarithmic moduli, one positive and one negative; the upper equality has exactly one x_i=m, exactly one x_j=-m and all remaining x-values zero.
Every quadratic unit attains both, while Salem/sign-twisted Salem inputs attain the upper equality.
Ifz is the count of zero log-moduli andV_+,V_- are the two within-sign sums, then h_ad=(d+z)m+V_++V_-.
These entropy comparisons do not require power-degree preservation.

B. Now impose deg(alpha^n)=d for every positive integern, equivalently no off-diagonal ratio alpha_i/alpha_j is a root of unity.
The reduced action may still have non-root-of-unity eigenvalues on the unit circle; it need not be expansive.
The centralizer ofA^n remainsC(A), even when Z[A^n] has nontrivial indexI_n inC.
For every n, both reduced integral models have the exact finite dual toral fixed-point cardinality

    F_n=abs(det(T^n-I))=abs(discP^[n])=Delta I_n^2,
    I_n=[Z[alpha]:Z[alpha^n]].

For the literal quotientL, with the unimodular matrix-trace pairing and C^perp its annihilator,

    [A,E]=C^perp,
    Tau_n=C^perp/[A^n,E]=tors(E/[A^n,E]),
    D_C=C^*/rho(C), card(D_C)=Delta,
    0->Tau_n->L/(T^n-I)L->D_C->0,
    card(Tau_n)=I_n^2.

No canonical splitting of this sequence is claimed, and it is not assigned to the separate companion model merely from equality of characteristic polynomials.
At n=1, Tau_1=0 and the middle group is exactlyD_C.
The discrete torsion-free lattice has only the zero fixed point; finite counts above concern its dual torus.
The full unreduced adjoint action has d eigenvalues1 and zero periodic determinant, so it is not the source of those finite counts.
F_n/F_1 andF_b/F_a whena dividesb are integer squares.
The accepted full fixed-input War05 limit and the independently direct elementary limsup in PartII have their exact distinct proof scopes:

    lim logF_n/n=h_ad,
    lim logI_n/n=h_ad/2,
    lim log(card(Tau_n))/n=h_ad.

The full limit retains its Baker input on algebraic unit-circle eigenvalues; no uniform convergence time or arithmetic rate is supplied.
The finite ratio-spectrum certificate is dominated by the ordinary powered Vandermonde estimate

    Delta I_n^2<=d^d M(P)^(2n(d-1)),

with dlogd no larger than the discarded d(d-1)log2 cost.

C. Over all monic irreducible nontorsion unit polynomials, every realH gives a finite set with h_ad<=H, and the positive minimum of h_ad is attained.
This uses the exact accepted asymptotic Dobrowolski bound and coefficient finiteness at their original source scope.
Any hypothetical sequence m(P_j)->0 has degree tending to infinity and h_ad(P_j)->infinity.
The normalized quantitya(P)=h_ad/d satisfies m<=a<=2(1-1/d)m, so its positive gap, vanishing sequences and convergence of positive series are equivalent to those ofm on the same class.
The divisor is the original degreed, not rankD; normalization byD instead has the stated height-scale comparison and is not automatically a new integral flow's ordinary entropy.
The complete C231 norm descent supplies all-power endpoints only for counterexample-existence reductions.

D. IfP is reciprocal, the field involution sigma(alpha)=alpha^(-1) preservesO=Z[alpha].
The actual subgroup W={m_z sigma:z inO} in End_Z(O) intersectsC trivially and embeds invariantly into the literal reduced adjoint quotient, with

    Ad_A(m_z sigma)=m_(alpha^2 z)sigma,
    h_alg(W)=2m.

The full degree-d powered polynomialP^[2], including possible multiplicities, dividesR inZ[t]; it is irreducible of degree d when the all-power guard holds.
No primitiveness or integral splitting ofW is asserted.
The positive minimum and finite sublevels for the whole adjoint family therefore supply no entropy-gap conclusion for its invariant-subgroup closure.
There is no unconditional subgroup counterexample, no all-compact-abelian periodic theorem, uniform arithmetic growth or resolution of the original Mahler gap.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:21 |
| status | open |
| reason | Register both complete retained adjoint arguments with exact integral models, trace/torsion sequence, entropy/periodic guards and subgroup/normalization boundaries; actual current whole inspection and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact complete statement](#statement) | Every general-unit entropy/lattice/subgroup claim, separately imposed all-power periodic/torsion guard, exact equality and degree/rank conventions, finite-sublevel and normalized-equivalence limits. |
| argument | [Both complete original arguments](#argument) | Entire original L61 and L62 mathematics, including retraction/inverse, full companion-column saturation proof, exact trace sequence, all equality cases, finite-cost comparison, coefficient finiteness, actual subgroup and complete elementary limsup proof. |
| dependency | [Complete powered-order identity](Yin_C_G0231_v1.md#powered-order-index) | Full original powered polynomial and exact monogenic-order index/discriminant formula, with all-power guard retained for every finite count. |
| dependency | [All-positive-power existence descent](Yin_C_G0231_v1.md#all-positive-power-existence-descent) | Only no-larger-positive-measure endpoint and counterexample-existence access, without pointwise strengthening of an original input or preservation of its flow. |
| dependency | [Rational entropy formula](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) | Exact finite-dimensional rational total algebraic entropy with multiplicities; the local denominator-clearing argument transports it to the integral lattice. |
| dependency | [Toral entropy normalization](../audits/literature/Smy08/Yin_U004.md#smy08-u004) | Classical toral GL_D(Z) entropy formula only, retaining algebraic multiplicities and no dimension divisor; no new original proof audit. |
| dependency | [Dobrowolski and elementary finite-height facts](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Only the accepted c,d0 asymptotic nonzero-nontorsion integral bound, coefficient finiteness and measure-one convention; no new explicit best constant or original proof. |
| dependency | [Exact toral periodic growth](../audits/literature/War05/Yin_U001.md#war05-u001) | Accepted fixed-input no-root-of-unity toral limit at original pp1--2/equations2,4 reading, with Baker and nonexpansive scope explicit; not every compact abelian group or a uniform rate. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:28 |
| status | proved |
| reason | Adopt both complete retained adjoint arguments after actual whole current self-review of every integral model, trace/torsion map, entropy/equality/sublevel/subgroup and source-qualified periodic interface. Exact general versus all-power domains, original degree versus rank and whole-flow versus subgroup boundaries remain; no new source proof, uniform arithmetic rate or independent-review claim is made. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Every general-unit entropy/lattice/subgroup claim, separately imposed all-power periodic/torsion guard, exact equality and degree/rank conventions, finite-sublevel and normalized-equivalence limits. |
| argument | [Argument](#argument) | Entire original L61 and L62 mathematics, including retraction/inverse, full companion-column saturation proof, exact trace sequence, all equality cases, finite-cost comparison, coefficient finiteness, actual subgroup and complete elementary limsup proof. |
| dependency | [Dependency](Yin_C_G0231_v1.md#powered-order-index) | Full original powered polynomial and exact monogenic-order index/discriminant formula, with all-power guard retained for every finite count. |
| dependency | [Dependency](Yin_C_G0231_v1.md#all-positive-power-existence-descent) | Only no-larger-positive-measure endpoint and counterexample-existence access, without pointwise strengthening of an original input or preservation of its flow. |
| dependency | [Dependency](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) | Exact finite-dimensional rational total algebraic entropy with multiplicities; the local denominator-clearing argument transports it to the integral lattice. |
| dependency | [Dependency](../audits/literature/Smy08/Yin_U004.md#smy08-u004) | Classical toral GL_D(Z) entropy formula only, retaining algebraic multiplicities and no dimension divisor; no new original proof audit. |
| dependency | [Dependency](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Only the accepted c,d0 asymptotic nonzero-nontorsion integral bound, coefficient finiteness and measure-one convention; no new explicit best constant or original proof. |
| dependency | [Dependency](../audits/literature/War05/Yin_U001.md#war05-u001) | Accepted fixed-input no-root-of-unity toral limit at original pp1--2/equations2,4 reading, with Baker and nonexpansive scope explicit; not every compact abelian group or a uniform rate. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0517_v1.md#current-integral-adjoint-finding) | Entire exact current statement, all complete retained proof parts and each selected interface; self-reviewed, with original dated scopes and relationships kept separate. |

## Complete retained arguments

<a id="argument"></a>

Both parts retain their original 2026-10-07 mathematics and local formula numbering.
The two original ratio-spectrum sections have distinct local anchors here so each fixed proof remains uniquely addressable.

## PartI: complete integral quotient, exact torsion and entropy costs

<a id="integral-adjoint-quotient"></a>
### The saturated centralizer and an explicit free quotient

Let alpha be a nonzero nontorsion algebraic unit with monic minimal polynomial P in Z[t], degree d>=2, and assume

    deg(alpha^n)=d       for every n>=1.                 (1)

The all-positive-power norm descent in [L G0059](Yin_C_G0231_v1.md#all-positive-power-existence-descent) legitimizes this restriction for gap or nonattainment existence questions.
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
### Characteristic polynomial and the no-root-of-unity condition

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
### Exact finite toral periodic counts

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
### The squared index is actual commutator torsion

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
### Exact entropy and sharp comparison to the original flow

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
### Periodic growth and its exact source boundary

For this integral toral automorphism, all eigenvalues are algebraic and none is a root of unity.
The retained [War05-U001 periodic-growth interface](../audits/literature/War05/Yin_U001.md#war05-u001), at its original statement and applicability scope, therefore applies:

    lim_(n->infinity) log F_n/n=h_ad.

Its treatment of algebraic eigenvalues on the unit circle uses the accepted Baker input; that proof is not reproduced or strengthened here.
No expansiveness assumption is inserted.
Together with (5) and (11), this gives

    lim log I_n/n=h_ad/2,
    lim log|Tau_n|/n=h_ad.                             (17)

These are pointwise limits for each fixed input.
They provide no uniform convergence time or degree-independent lower growth rate.
Nor are they assertions about periodic points on arbitrary compact abelian groups or on the discrete lattice itself.
The elementary simultaneous-torus-return argument in [L G0062](#adjoint-periodic-index-boundary) proves the corresponding limsup without the additional Diophantine input.
Its other conclusions about whole-family entropy and the reciprocal invariant subgroup have their separate stated scopes.

<a id="adjoint-normalized-target-boundary"></a>
### What the construction does and does not improve

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

## PartII: complete sublevel, normalization, subgroup and elementary periodic boundary

### Inputs and source boundary

Let alpha be a nontorsion algebraic unit of degree d>=2, with monic irreducible polynomial P and distinct conjugates alpha_1,...,alpha_d.
Write m=log M(P)>0 and Delta=|disc P|.
Where periodic counts or the all-power class are used, assume deg(alpha^n)=d for every n>=1.
The existence reduction to such endpoints is [L G0059](Yin_C_G0231_v1.md#all-positive-power-existence-descent).
It does not say that each original input already has this property.

The only analytic arithmetic bound used is the accepted external Dobrowolski statement recorded in [Smy08-U001](../audits/literature/Smy08/Yin_U001.md): there are absolute c>0 and d_0>=3 such that every nonzero nontorsion algebraic integer of degree d>=d_0 satisfies

    m >= c (log log d / log d)^3.                       (1)

No explicit choice of c or d_0, Voutier refinement, or proof of the original theorem is adopted here.
The source audit also supplies the elementary coefficient bound |a_j|<=binom(d,j) M(P) and Kronecker's measure-one characterization.
The entropy/Mahler identification uses the accepted rational formula of [GBV15-U001](../audits/literature/GBV15/Yin_U001.md#gbv15-u001) and the rationalization interface of [DGB16-U001](../audits/literature/DGB16/Yin_U001.md#dgb16-u001).
The finite-index identity below is the proved [powered-order formula](Yin_C_G0231_v1.md#powered-order-index).

<a id="adjoint-companion-ratio-spectrum"></a>
### An integral reduced adjoint flow

Set D=d(d-1) and

    R(t)=product_(i!=j)(t-alpha_i/alpha_j).

Each ratio is an algebraic integer because alpha_j is a unit.
The multiset is Galois invariant, so R is monic in Z[t]; paired inverse ratios give constant term 1.
Its degree is D.
Thus its companion matrix is unimodular and defines a free integral flow of rank D.

There is also a literal adjoint realization.
On O=Z[alpha], let A be multiplication by alpha.
Conjugation T -> A T A^(-1) acts invertibly on End_Z(O), with eigenvalues alpha_i/alpha_j for all i,j.
Its fixed lattice C is saturated, being the kernel of an integral homomorphism.
It has rank d: over Q, a commuting operator is determined by its value on the cyclic vector 1, so the centralizer consists of multiplications by elements of Q(alpha).
The quotient End_Z(O)/C is free of rank D, is invariant in both time directions, and its characteristic polynomial is R.
In particular it has the same algebraic entropy as the companion flow.
Denote this entropy by h_ad.

The full adjoint action has d eigenvalues 1.
Its periodic determinant is always zero.
All nonzero periodic determinants below belong to the reduced quotient or to the companion of R, not the full adjoint action.

Finally, R has a root of unity exactly when some distinct alpha_i, alpha_j have equal positive powers.
By the embedding-fiber identity in L G0059, this is equivalent to deg(alpha^n)<d for some n>=1.
Thus the all-power hypothesis is precisely what excludes cyclotomic roots from this reduced ratio polynomial; R can still be reducible and have repeated noncyclotomic roots.

<a id="adjoint-degree-amplification"></a>
### Exact entropy comparison and finite sublevel sets

Put x_i=log|alpha_i|.
Since alpha is a unit, sum_i x_i=0, and m=(1/2)sum_i |x_i|.
The ratio spectrum gives

    h_ad = sum_(i<j) |x_i-x_j|,
    d m <= h_ad <= 2(d-1)m.                            (2)

For the lower inequality, the triangle inequality gives

    2h_ad=sum_(i,j)|x_i-x_j|
          >=sum_i |sum_j(x_i-x_j)|
          =d sum_i|x_i|=2dm.

For the upper inequality, each |x_i| appears in d-1 unordered pairs.
These comparisons require neither reciprocity nor power-degree preservation.
The upper constant is attained when the log-moduli are x,-x,0,...,0, as for a Salem input.

For every real H, only finitely many monic irreducible nontorsion unit polynomials P have h_ad<=H.
Indeed, (1)--(2) imply for large d that

    h_ad >= c d (log log d / log d)^3 -> infinity.      (3)

Thus d is bounded on such a sublevel set.
Then M(P)<=exp(H/d), and the integer coefficient bound gives only finitely many P.
In particular the unnormalized adjoint family has an attained positive minimum.
To see attainment without any compactness assertion, choose one input and minimize over its finite, nonempty entropy sublevel set; all other inputs have larger entropy.

Any hypothetical sequence m(P_j)->0 has d_j->infinity: a bounded degree and, eventually, M(P_j)<=2 would give finitely many polynomials with positive measure.
Equation (3) therefore yields h_ad(P_j)-> infinity.
More generally, an infinite sequence of distinct such minimal polynomials eventually leaves every bounded adjoint-entropy sublevel set.
This conclusion is unconditional and does not decide whether the original sequence with m(P_j)->0 exists.

<a id="normalized-adjoint-equivalence"></a>
### The normalization that restores the original problem

For a(P)=h_ad(P)/d, (2) becomes

    m(P) <= a(P) <= 2(1-1/d)m(P) < 2m(P).             (4)

On any chosen class of these inputs, a uniform positive lower bound for a is equivalent to one for m: a>=epsilon implies m>=epsilon/2, and m>=epsilon implies a>=epsilon.
Vanishing sequences and convergence of positive series of these quantities are equivalent by the same comparison.
On all-power-stable units this is an equivalent gap question, not a new uniform bound.
By the existence descent in L G0059, the infimum of positive m is unchanged on passing from all nontorsion units to this endpoint class.

The division in (4) is by the original degree d, not the rank D of the reduced flow.
Normalizing by that rank instead gives

    m/(d-1) <= h_ad/D <= 2m/d,

which is comparable to the absolute logarithmic height m/d.
Neither normalization is automatically the ordinary algebraic entropy of a new integral flow; it must be stated explicitly.

<a id="reciprocal-adjoint-subgroup"></a>
### The reciprocal core reappears as an actual invariant subgroup

Suppose in addition P is reciprocal.
The map sigma:alpha->alpha^(-1) is an involutive field automorphism of K=Q(alpha).
It preserves O: alpha^(-1) belongs to O because alpha is a unit, and applying sigma again gives equality sigma(O)=O.
For z in O let m_z be multiplication by z and define

    W={m_z sigma:z in O} subset End_Z(O).

This is a free rank-d subgroup, and direct composition gives

    Ad_A(m_z sigma)=m_(alpha^2 z) sigma.                (5)

Moreover W intersects C trivially.
Commuting m_z sigma with m_alpha would give z(alpha-alpha^(-1))=0; nontorsion excludes alpha=alpha^(-1), so z=0.
Hence W embeds in the reduced adjoint quotient as an actual invariant subgroup isomorphic to multiplication by alpha^2 on O.
Its entropy is exactly 2m: the full degree-d powered polynomial has roots alpha_i^2 and its logarithmic measure is 2m, including any powering multiplicities.
Under the all-power assumption this powered polynomial P^[2] is itself irreducible of degree d.

Equivalently, the ordered pair (alpha_i,alpha_i^(-1)) contributes alpha_i^2 to R, so P^[2] divides R in Z[t].
This also confirms the entropy contribution directly.
No assertion that the image of W is primitive, or that the integral flow splits as a direct sum, is made.

Consequently the positive gap and finite sublevels for whole adjoint flows supply no logical inference of the corresponding properties for their invariant-subgroup closure.
This is not an unconditional counterexample to a subgroup entropy gap.
If small original reciprocal entropies existed, (5) would give small subgroup entropies 2m inside whole adjoint flows whose entropy tends to infinity.
Using an entropy addition theorem must preserve this distinction; monotonicity only bounds the subgroup entropy above by the whole.

<a id="adjoint-periodic-index-boundary"></a>
### Finite periodic counts retain an arithmetic question

Assume all positive powers preserve degree and let B be either reduced-adjoint matrix above.
For n>=1, the finite number of fixed points of its dual toral automorphism is

    F_n=|det(B^n-I)|
       =product_(i!=j)|(alpha_i/alpha_j)^n-1|
       =|disc P^[n]|=Delta I_n^2,                     (6)

where I_n=[Z[alpha]:Z[alpha^n]].
The toral fixed-point formula follows from the lattice index of the nonsingular integer map B^n-I.
In the product, the denominator has absolute value |Norm(alpha)|^(n(d-1))=1, and the numerator pairs into the powered discriminant.
This proves (6) without an entropy limit theorem.

The elementary bound |z^n-1|<=2 max(1,|z|)^n gives, for every n,

    log Delta+2log I_n <= n h_ad+D log 2,
    m >= [log Delta+2log I_n-D log 2]/[2n(d-1)].       (7)

Thus an adequately strong lower estimate for the actual indices could provide a finite Mahler certificate.
Integer positivity F_n>=1 or I_n>=1 alone does not supply such an estimate; (7) retains both its quadratic degree cost D log2 and the factor n(d-1).
In fact the ordinary d by d powered Vandermonde estimate already replaces D log2 in (7) by d log d, which is no larger.
The direct proof and full integral quotient/torsion structure are retained in [L G0061](#adjoint-normalized-target-boundary).
Thus forming the ratio-spectrum flow does not improve this finite certificate for the same index input.

There is an elementary asymptotic identity at limsup scope:

    limsup_(n->infinity) (log F_n)/n=h_ad,
    limsup_(n->infinity) (log Delta+2log I_n)/(nd)=a(P). (8)

The upper bound follows from (7).
For the lower bound, collect the finitely many unit-circle eigenvalues into a vector z in a torus.
None is 1.
There are integers q_j->infinity with z^(q_j)->1: compactness supplies powers with arbitrarily small positive return, and if their exponents stayed bounded some fixed positive power would be exactly 1; in that finite-order case its multiples also give unbounded returns.
Thus z^(q_j+1)->z, where every coordinate differs from 1.
Along n_j=q_j+1 all the unit-circle logarithmic factors stay bounded.
Each remaining eigenvalue rho satisfies log|rho^n-1|/n->log^+|rho|.
Summing proves the lower limsup.
If there are no unit-circle eigenvalues, the ordinary limit follows directly.

For algebraic unit-circle eigenvalues, this elementary argument establishes only the limsup.
The complete fixed-input limit is available at the accepted War05/Baker scope reused in [L G0061](#adjoint-index-growth); its additional Diophantine input is not reproduced here.
Both versions are pointwise in P and supply no convergence rate uniform in d or P.
Their degree-normalized value is already the equivalent quantity (4).
Equations (6)--(7) leave actual finite order-index growth as a possible arithmetic input, but entropy amplification, integrality and a fixed-flow asymptotic alone do not provide the missing uniform estimate.
