---
author: Yin
---
# Actual Salem wreath realizations with prescribed binary ramification

Human author Yin.
Root proposed the arithmetic realization, its optional binary ramification parameter and the direct height consequence.
The loglog_cyclic_review author develops the global cyclic and symmetric fields, trace-unit motion, exact Salem root action and their complete assembly.
The entropy_attainment_bridge author supplies the explicit binary local field, strong-Hensel primitive preservation, real-place compatibility and ramification-cost calculation.
All three are proof contributors and cannot independently review this account.
The source-only helper located standard interfaces and supplied no new construction proof.
No native mathematical computation, polynomial search, prime scan or numerical approximation is performed.

## Responsible question, source boundaries and assembly

This combines the actual unramified construction with its explicit totally ramified local replacement into one family.
The case r=1 preserves the unramified conclusions; r=2^a allows an exact prescribed binary ramification index.
It realizes the regular block action T=C_M times S_j and a central odd-order residue-Frobenius lift by genuine Salem units, with two orbital targets per root even when the global Frobenius class is very large.
It is a positive-measure control family and does not assert near-one realizability or novelty over every existing Salem construction.

The accepted [L162 even-degree Salem kernel](../ledger/Yin_L_G0162_v1.md#salem-kernel-class-population), under its [R61 acceptance](../audits/reviews/Yin_R_G0061_v1.md#complete-independent-written-review-and-adoption), supplies the full inversion kernel; its actual argument is reproduced below at the precise even trace degree.
The accepted [Con26 full unit lattice](../audits/literature/Con26/Yin_U001.md#con26-u001) and [L388 strict unit cone](../ledger/Yin_L_G0388_v1.md#actual-order-units-in-every-log-cone) provide the totally positive Pisot-unit direction.
The [The26b local interface](../audits/literature/The26b/Yin_U001.md#the26b-u001) supplies actual decomposition groups, inertia and residue-Frobenius lifts at the indicated number-field primes.
The [Con26e strong Hensel interface](../audits/literature/Con26e/Yin_U001.md#con26e-u001) applies in the actual finite complete extension, with a possibly nonunit derivative, and later to the simple reciprocal quadratics.

The accepted [Hun74 PID unit](../audits/literature/Hun74/Yin_U005.md#hun74-u005), specifically IV.6.7 and IV.6.9 at coefficient PID Z, supplies the prime-primary cyclic decomposition of a finite abelian group.
The separate [Hun74 finite-field unit](../audits/literature/Hun74/Yin_U006.md#hun74-u006) supplies the exact finite-field existence, irreducible-degree and cyclic Frobenius interfaces from V.5.7--V.5.10.
It is accepted at statement/applicability scope, without a new proof audit of Chapter V.
The monic rational-factor property in [Con26d-U001 v2](../audits/literature/Con26d/Yin_U001.md#con26d-u001) justifies irreducibility over Q from the chosen irreducible reduction.
That source also identifies the familiar global Eisenstein pattern of q_r, but no uninspected local Eisenstein theorem is invoked: its local degree and ramification are proved by valuations below.
The finite Chinese remainder theorem, elementary separable norm tower and ordinary field/Galois foundations are used at their stated algebraic scope.
All inherited source-proof inspection limits remain unchanged.

The initially proposed split odd prime and discriminant squareclass witnesses are unnecessary because the trace degree is even.
No Schur, Chebotarev, Kummer independence, Krasner or local class-field theorem is used.
The required cyclotomic groups and local degrees are established directly rather than inferred from an uninspected cyclotomic-field formula.
The accepted [C162 orbital criterion](Yin_C_G0162_v1.md#statement) under its [whole-review decision](Yin_C_G0162_v1.md#decision-whole-reviewed-2026-10-18) supplies comparison context only.
The direct height proof below uses the credited [extra-depth norm mechanism](Yin_C_G0146_v1.md#bounded-class-nonnormal-argument) and [actual ratio-fiber interface](../ledger/Yin_L_G0397_v1.md#full-ratio-orbits), with every needed step retained in this construction.
No conclusion of C162 or C163 is a premise.

## Statement

For every odd prime ell, every integer a>=0 and r=2^a, and every integer j>=max{5,r}, there exists an integer b>=1 and M=ell^b such that infinitely many genuine Salem units alpha have original degree

    t=M j!, d=2t,

and normal closure L with the ACTUAL root permutation group

    G=(C2)^T semidirect T, T=C_M times S_j,

on T times {0,1}, with T acting regularly on its blocks.
The actual trace field Q(alpha+alpha^(-1)) is totally real Galois with group T.
At every prime of L above 2 the ramification index is exactly r and the residue degree is exactly ell.
At a suitable such prime there is a selected arithmetic residue-Frobenius lift sigma of order ell, acting as a pure translation by a central z in C_M of order ell, with

    s=2, gamma=1,
    kappa=|class_G(sigma)|=2^(t-t/ell).                  (1)

Here s is the number of targets per source in the G-orbit of (alpha,sigma(alpha)), and gamma is the fraction of original Frobenius edges (beta,sigma(beta)) belonging to that orbit.
Every sigma-cycle on the original 2t roots has length ell.
For each integer f with 1<=f<ell, sigma^f has the same conjugacy-class size.
At r>1 the assertion selects this actual lift; it does not assign the same order to every residue-Frobenius lift.

For every abelian subgroup A0 of G and every finite abelian extension B0/Q,

    [G:A0]>=j!/3^(j/3),
    [B0(alpha):B0]>=j!.                                (2)

The original field has exactly the inverse automorphism: N_G(G_alpha)/G_alpha is isomorphic to C2.
Every constructed member satisfies

    h_abs(alpha)>log2/(24r),
    m(P_alpha)>d log2/(24r),                            (3)

where h_abs is the absolute logarithmic height and m(P_alpha)=d h_abs(alpha) is the original TOTAL logarithmic Mahler measure.
For every fixed ell,j,r the constructed measures tend to infinity along the family.
For r=1 the entire L is unramified at 2 and (3) becomes h_abs(alpha)>log2/24.
Even when r grows, j>=r makes d/r=2M j!/r large; the construction provides no sequence of total measures tending to zero.

<a id="argument"></a>
## Complete argument

### 1. The odd cyclic field and its Frobenius order

Fix the odd prime ell and put N=2^ell-1.
Let zeta be a primitive N-th root of unity and Q0=Q(zeta).
This is a finite Galois field, as the splitting field of X^N-1, and its Galois group embeds into the abelian group (Z/NZ)^* by its action on zeta.
No surjectivity onto that whole group is required.

At any prime over 2, all N-th roots of unity have distinct reductions.
Indeed, if eta is an N-th root of unity, eta!=1 and eta=1 modulo that prime, the equality 1+eta+...+eta^(N-1)=0 reduces to N=0 in characteristic 2, contradicting N odd.
Thus inertia fixes each N-th root and is trivial, so 2 is unramified in Q0.
An actual residue-Frobenius lift exists by The26b-U001 and takes zeta to zeta^2, since these roots have distinct reductions.
Its order is ell: the order divides ell, ell is prime, and 2 is not 1 modulo N.

Complex conjugation has order 2 and its fixed field is C=Q(zeta+zeta^(-1)); the quadratic equation for zeta proves this fixed-field identity.
C is totally real and Galois over Q because Gal(Q0/Q) is abelian.
The square Frobenius has order ell also in Gal(C/Q), since an odd-order cyclic subgroup intersects the order-two complex-conjugation subgroup trivially.

Decompose the finite abelian group Gal(C/Q) into its prime-primary cyclic factors using Hun74-U005.
The order-ell Frobenius has a nonzero coordinate in at least one cyclic ell-primary factor C_M, where M=ell^b for some b>=1.
Projection onto that factor preserves the exact order ell of this coordinate.
Let A be the fixed field of its kernel.
Then A is totally real cyclic of degree M, 2 is unramified, and its Frobenius z has exact order ell.
Every completion of A above 2 consequently has residue degree ell.
The conductor N need not be prime and 2 need not be inert in A.

<a id="binary-cyclic-local-field"></a>
### 2. The explicit binary cyclic local field

Fix an integer a>=0 and put r=2^a.
In an algebraic closure of Q_2 choose a root zeta of X^(2r)+1.
Its order is exactly 4r, since 4r is a power of 2 and zeta^(2r)=-1.
Set

    C=Q_2(zeta), eta=zeta-1,
    theta=zeta+zeta^(-1)-2=eta^2/zeta,
    B=Q_2(theta).

Normalize the valuation by v(2)=1.
The root zeta is an integral unit, and its residue is 1 because in characteristic 2 the equation X^(4r)=1 has only the root 1.
Thus v(eta)>0.
The equation (1+eta)^(2r)+1=0 has constant term 2, leading term eta^(2r), and every intermediate binomial coefficient divisible by 2.
Every intermediate term consequently has valuation greater than 1.
The least valuation in a zero sum cannot occur uniquely, so

    v(eta)=1/(2r).

The 2r powers 1,eta,...,eta^(2r-1) are linearly independent over Q_2: their valuations have distinct fractional parts modulo Z, so a nontrivial rational linear combination has a unique term of least valuation.
Since eta satisfies a polynomial of degree 2r, it follows that [C:Q_2]=2r.
The same basis shows that the value group is (1/(2r))Z and the residue field is F_2.
Indeed a linear combination of valuation zero has its unique least term in the zeroth basis coordinate, with a Q_2-unit coefficient and hence residue in F_2.
Thus C is totally ramified.

All roots zeta^u with u odd modulo 4r belong to C, and there are 2r of them.
The extension C/Q_2 is Galois, and its automorphisms are exactly zeta maps to zeta^u for those odd classes.
Inversion is a nontrivial order-two automorphism.
It fixes theta, and zeta satisfies X^2-(theta+2)X+1 over B, so [C:B]=2.
Consequently [B:Q_2]=r and B is the fixed field of inversion.

The quotient (Z/4rZ)^*/{1,-1} is cyclic of order r.
For a>=1, the elementary induction

    v_2(5^(2^k)-1)=k+2

shows that 5 has order 2^a modulo 2^(a+2)=4r.
Its powers comprise all units congruent 1 modulo 4; their negatives give the other odd classes.
For a=0 the quotient is trivial, as required.
Therefore Gal(B/Q_2) is cyclic of order r.
Also v(theta)=1/r, and the r powers of theta have distinct valuation fractions as above.
They show directly that B has ramification index r and residue field F_2.
No unproved assumption that a real global subfield has the desired local degree is used.

For a monic integral polynomial defining theta, use

    C_0(X)=2, C_1(X)=X,
    C_(n+1)(X)=X C_n(X)-C_(n-1)(X),
    q_r(X)=C_r(X+2).

The identity C_n(zeta+zeta^(-1))=zeta^n+zeta^(-n) gives q_r(theta)=0 because zeta^r has order 4.
The polynomial q_r is monic of degree r and is therefore the minimal polynomial of theta over Q_2.
It has all r distinct roots in B, since B/Q_2 is Galois.
The relation C_(2n)=C_n^2-2 gives q_r(X)=X^r modulo 2 and q_r(0)=2.
Over R its roots are the distinct numbers 2cos((2k+1)pi/(2r))-2, with one representative from each inverse pair.
In particular q_r is a specific polynomial in Z[X] and its root set is disjoint from every positive integer.
For r=1 it is X+2 and B=Q_2.

<a id="strong-hensel-primitive-preservation"></a>
### 3. Exact local splitting under coefficient perturbation

For the stated j>=max{5,r}, put

    g(X)=q_r(X) product_(i=1)^(j-r)(X-i).

Write its j distinct roots in B as theta_1,...,theta_j, choosing theta_1=theta.
They are all integral.
Let

    t_i=v(g'(theta_i)),
    t_max=max_i t_i,
    R_sep=max_(i!=k)v(theta_i-theta_k).

These are finite nonnegative rational numbers.
Choose any integer K>2t_max+R_sep.
For every monic degree-j f in Z[X] congruent coefficientwise to g modulo 2^K, integrality of the centers gives

    v(f(theta_i))>=K,
    v(f'(theta_i)-g'(theta_i))>=K,
    v(f'(theta_i))=t_i.

Thus v(f(theta_i))>2t_i, and Con26e supplies a simple root beta_i in B with

    v(beta_i-theta_i)>=K-t_i>R_sep.                  (4)

If a center is already a root, the valuation of its displacement is infinite.
The balls in (4) are disjoint by the ultrametric inequality, so the beta_i are j distinct roots and exhaust all roots of f.
For each of the j-r rational centers i, the same Hensel theorem applied in Q_2 gives a root there; its uniqueness in the B-neighborhood identifies it with beta_i.
Thus these j-r roots are in Q_2.

The root beta_1 still generates B.
If a nontrivial tau in Gal(B/Q_2) fixed beta_1, then beta_1 would be within valuation greater than R_sep of both theta_1 and tau(theta_1).
Those centers are distinct because theta_1 is primitive, contradicting their separation.
Here tau preserves the valuation: for odd u the quotient (zeta^u-1)/(zeta-1) is a unit, so every conjugate of theta has valuation 1/r and the same unique-minimum formula in its power basis holds.
The Galois stabilizer of beta_1 is therefore trivial, so Q_2(beta_1)=B.

Consequently the splitting field of EVERY such f over Q_2 is exactly B, not merely a subfield of B.
The cyclic local Galois group acts regularly on the r roots in the q_r cluster and fixes the other j-r roots.
No Krasner theorem, continuity of roots without a radius, or hidden irreducibility-preservation assumption is used.
In the unramified case one may alternatively start with any j distinct integer centers b_i and g=product_i(X-b_i).
Writing s_i=v_2(g'(b_i)) and s_max=max_i s_i, the weaker sufficient integer precision L0>2s_max already gives root distances at least L0-s_i>s_max.
Since every pairwise center valuation is at most s_max, this recovers the original construction with j distinct Q_2 roots even when their reductions coincide modulo 2.

<a id="ramified-symmetric-real-crt"></a>
### 4. Simultaneous real roots and full symmetric group

Choose three distinct odd primes l_1,l_2,l_3 greater than j.
Over their residue fields choose monic squarefree degree-j polynomials with factor-degree patterns

    (j), (j-1,1), (2,1,...,1), respectively.

Finite-field irreducibles of each required degree are supplied by the accepted Hun74-U006 interface.
For the elementary existence mechanism, the q^n roots of X^(q^n)-X over F_q form a field.
Every proper intermediate field containing F_q has degree d dividing n, hence d<=floor(n/2), and at most one such subfield has cardinality q^d because its elements are the roots of X^(q^d)-X.
For n>=2 the union of those proper intermediate fields has size at most sum_(d=1)^floor(n/2) q^d<q^n.
An element outside that union has degree n over F_q; degree 1 is immediate.
The distinct linear factors exist because the chosen odd primes exceed j; the degree-at-least-two irreducible factors have no base-field roots.
All prescribed reductions are squarefree.

Combine these coefficient congruences with f=g modulo 2^K by CRT.
Write Q=2^K l_1 l_2 l_3 for their common modulus.
To retain all real roots, put G_R(X)=product_(i=1)^j(X-Ri) for an integer R>=2, and choose each lower coefficient of a monic f_R in its required Q-class nearest to the corresponding coefficient of G_R.
Each coefficient error has absolute value at most Q/2.

At X=R(i plus or minus 1/4), one has

    |G_R(X)|>=3^(j-1) R^j/4^j,
    |f_R(X)-G_R(X)|<=(Q/2) j [(j+1)R]^(j-1).

Choose an integer

    R>Q j 4^j (j+1)^(j-1)/(2*3^(j-1)).

Then the original opposite endpoint signs around every Ri are preserved.
The j disjoint intervals therefore each contain one real root of f_R.
These are all j roots and they are distinct.
No smallness condition at the real place is incompatible with the fixed 2-adic or odd-prime residue class; increasing R supplies the needed room.

The irreducible reduction at l_1 makes f_R irreducible over Q.
Let E be its splitting field.
It is totally real.
At each chosen odd prime the roots have distinct reductions because the polynomial reduction is squarefree.
An actual residue-Frobenius lift from The26b therefore permutes the roots with the prescribed factor-degree pattern.
The group is transitive and contains a (j-1)-cycle fixing one point; that point stabilizer is transitive on the remaining points, so the group is 2-transitive.
It also contains a transposition.
Conjugating it through the 2-transitive action gives every transposition, hence Gal(E/Q)=S_j.

At a chosen 2-prime the splitting field completion is B by Section 3.
Because E/Q is Galois, the other 2-primes have isomorphic completions.
Every such prime has ramification index r, residue degree 1, and a cyclic decomposition group C_r acting as an r-cycle with j-r fixed points.
For r=1 this is precisely complete splitting of 2 in E.
This constructs the required actual symmetric field before the later Pisot-unit step.

<a id="ramified-cyclic-compositum"></a>
### 5. The trace-field compositum and selected residue lift

Use the totally real cyclic A from Section 1, with odd degree M and residue-Frobenius z of order ell.
Every completion of A above 2 is an unramified cyclic extension U/Q_2 of degree ell.
The intersection A intersection E is Galois over Q and is a cyclic quotient field of the S_j extension.
Every abelian quotient of S_j has order at most 2: transpositions generate S_j, are conjugate and have order 2, so their images generate at most one group of order 2 in an abelian quotient.
Since [A:Q]=M is odd, the intersection is Q.
Thus

    F=AE, Gal(F/Q)=T=C_M times S_j,
    [F:Q]=t=M j!,

and F is totally real.
At a chosen prime w over 2 its completion is W=BU.
It has ramification index r and residue degree ell.
Indeed the valuation group of U is Z, so theta of valuation 1/r still has degree at least r over U by the distinct fractional valuations, and its defining polynomial gives degree at most r.
The r powers of theta form a basis over U with distinct valuation fractions; the same unique-minimum argument gives value group (1/r)Z and residue field equal to that of U.
Both B and U are Galois over Q_2, and restriction identifies

    Gal(W/Q_2)=C_r times C_ell,
    inertia=C_r times {1}.                              (5)

The element (1,z) is an actual residue-Frobenius lift of order ell.
It is identity on B and induces square Frobenius on the residue field of U.
In the global quotient T=C_M times S_j its image is (z,1), hence central.
Because F/Q is Galois the same ramification and residue degrees occur at every prime above 2.
The selection of (1,z) is essential at ramified primes; no uniqueness among all lifts is asserted.

At each w the residue field is F_(2^ell).
For every w choose a residue z_w in F_(2^ell)^* different from 1 and set c_w=z_w+z_w^(-1).
Then c_w!=0 in characteristic 2, and X^2-c_w X+1 has the two distinct roots z_w,z_w^(-1).
The integer-ring Chinese remainder theorem supplies a_0 in O_F with a_0=c_w modulo w for every w above 2.
Adding a sufficiently large even rational integer preserves these residues and makes every real embedding positive; call the resulting integral element a_star.
Choosing residue 1 in place of these actual trace residues would not justify the required quadratic splitting for odd ell.

### 6. The unit motion and actual Salem polynomial

Fix the distinguished real embedding of F.
The accepted Con26/L388 full-lattice argument supplies a unit epsilon in O_F^* with absolute value greater than 1 at that embedding and less than 1 at every other embedding.
Square it to make every embedding positive, and then raise it to a positive integer power so its residue is 1 in the finite group (O_F/2O_F)^*.
This finite unit group is available even when O_F/2O_F is nonreduced.
Since 2O_F is contained in every 2-prime, the congruence preserves all selected residues.
Call this totally positive unit u.
Its strict embedding inequalities remain unchanged.
These powers and unit sizes need not be uniformly bounded in ell,j,r.

For positive integers k put v_k=a_star u^k.
It is integral, preserves all the prescribed 2-prime residues, tends to positive infinity at the distinguished embedding and to zero through positive values at every other embedding.
For every sufficiently large k,

    v_k>2 at the distinguished embedding,
    0<g(v_k)<2 at every other embedding g.

The element v=v_k is primitive in F.
If it belonged to a proper subfield, its distinguished value would repeat [F:Q(v)]>1 times among the F-embeddings, contradicting the unique value greater than 2.
Thus Q(v)=F, and its conjugates form the regular T-orbit.

The polynomial X^2-vX+1 is irreducible over F because v^2-4 is negative at every other real embedding and cannot be a square in a totally real field.
Let alpha>1 be its larger real root at the distinguished embedding.
Then F=Q(alpha+alpha^(-1)) is contained in Q(alpha), so [Q(alpha):Q]=2t.
Its minimal polynomial is exactly

    P_alpha(X)=product_(g in T) [X^2-g(v)X+1] in Z[X].

It is monic, irreducible, reciprocal and has constant coefficient 1.
Its roots are alpha,alpha^(-1), and 2t-2 nonreal roots of modulus 1.
Thus alpha is a genuine Salem algebraic integer unit.
For fixed ell,j,r, m(P_alpha)=log alpha tends to infinity as k tends to infinity.

### 7. The full wreath group at even trace degree

Let L be the splitting field of P_alpha.
Its inverse pairs are indexed by the t conjugates g(v), so the trace-pair quotient is precisely T=Gal(F/Q), acting regularly.
The root action embeds Gal(L/Q) into (C2)^T semidirect T with surjective top projection.
Let V be its inversion kernel.

At the distinguished complex embedding, complex conjugation fixes the real pair and swaps every other inverse pair.
Its vector in V is 1+e_1.
Conjugating by the transitive top action supplies every 1+e_g.
Because t=M j! is even, their sum is 1, and hence e_g=(1+e_g)+1 belongs to V for every g.
Therefore V=(C2)^T, exactly as in the accepted even-degree part of L162.
The embedded root-action group has the full ambient wreath-group order and is therefore the entire wreath group.
This does not assume a splitting of a smaller unknown extension: the full kernel and the faithful root action establish equality with the full ambient group.

### 8. Actual local quadratic splitting and pure central shift

For every 2-prime w of F, the reciprocal quadratic of v has the two simple residue roots chosen above.
The complete-field Hensel theorem lifts them to two roots in F_w.
The same is true of each conjugate g(v), because its residue condition transports from g^(-1)w and finite-field isomorphisms preserve the split-simple property.
Thus every factor of P_alpha splits over F_w, so the completion L_W at a prime above w equals F_w.
Consequently the ENTIRE normal closure has exact ramification index r and residue degree ell at 2; the quadratic adjoining adds no local extension.
For r=1 the entire L is unramified.

The decomposition group of L at this prime is the actual Gal(W/Q_2) in (5).
Select its lift sigma=(1,z), which has order ell and projects to the central z in T.
In the wreath coordinates write sigma=(b_vec,z).
The equation sigma^ell=1 says that the sum of b_vec on each length-ell block cycle is zero.
On each cycle one can solve b_vec=c+zc by successively choosing one coordinate and determining the rest; the zero sum is exactly the consistency condition.
Hence conjugation by a base vector turns sigma into the pure translation (0,z).
The free initial choice on the distinguished cycle can make that base conjugator fix alpha, or equivalently one can orient the root pairs while keeping alpha's label fixed.
This identifies an actual prime/Frobenius and the original root, not merely a formal class in an abstract group.

### 9. Exact original-root orbital and group bounds

Label alpha by (1,0) in T times {0,1} and sigma alpha by (z,0).
Because z is central and nonidentity, the G-orbit O of this ordered pair consists precisely of the ordered pairs from block x to block xz with either source bit and either target bit.
It has 4t=2d elements and two possible targets per original root.
Every actual sigma-edge belongs to it, giving s=2 and gamma=1.

A base vector commutes with sigma exactly when it is constant on each of its t/ell cycles; every top element commutes with z.
Thus

    |C_G(sigma)|=2^(t/ell)t,
    |class_G(sigma)|=2^(t-t/ell).

All root cycles have length ell, and replacing sigma by sigma^f for 1<=f<ell gives the same cycles and centralizer size.
If H=G_alpha, then H is the subgroup of base vectors zero at the distinguished block.
All base vectors normalize H, and a regular top translation normalizes H only when it is the identity.
Consequently N_G(H)/H=C2, consistent with the actual inverse automorphism of the Salem field.

For an abelian subgroup A0 of G, its image in S_j has order at most 3^(j/3).
Indeed on each orbit an abelian transitive image is regular; faithfulness bounds its order by the product of orbit sizes, and n<=3^(n/3) for every positive integer n.
The image in T therefore has order at most M3^(j/3), and the base kernel has order at most 2^t.
Dividing by |G|=2^t M j! proves the first bound in (2).

The derived subgroup G' contains all even-weight base vectors, since commutators of a coordinate flip and regular translations give any pair of coordinate flips.
Its top image is {1} times A_j, whose regular block orbit has j!/2 elements.
Even-weight base vectors can flip the bit in any one of these blocks by also flipping a different block.
Hence every G'-orbit on the root set has size at least j!.
For an arbitrary finite abelian B0/Q, the intersection L intersection B0 is abelian over Q, so Gal(L/(L intersection B0)) contains G'.
Restriction identifies that group with Gal(LB0/B0), and its orbit on alpha has size [B0(alpha):B0], proving the second bound in (2).
The original field is not Galois, and the displayed abelian-index and abelian-base relative-degree parameters cannot remain uniformly bounded as j grows.
This does not exclude every classical height theorem.

<a id="ramified-height-cost"></a>
### 10. The strict ramification-dependent height floor

The selected lift sigma has finite order ell and actual orbital parameters s=2,gamma=1.
Let rho=alpha^2/sigma(alpha), E0=Q(rho) and D=[E0:Q].
The ratio is an integral unit and is nontorsion: if sigma(alpha)=alpha^2 times a root of unity, iteration through sigma's finite order would make alpha^(2^ell-1) a root of unity.
The G-equivariant map (x,y) maps to x^2/y from the ordered-pair orbit of size 2d onto the D distinct ratio conjugates has constant fiber size 2d/D.
Its d compatible Frobenius pairs therefore supply at least D/2 DISTINCT rho-conjugates congruent to 1 at the selected 2-prime.

Each positive normalized valuation is at least 1/r, since the entire completed normal closure has value group (1/r)Z.
For a unit x congruent to 1, the identity x^2-1=2(x-1)+(x-1)^2 gives

    v(x^2-1)>=min(1+v(x-1),2v(x-1)).

Starting at 1/r and using r=2^a, after a squarings the lower depth is 1; after two more it is 3.
All other conjugates remain integral.
Thus at the SAME exponent n=4r,

    log abs Norm_(E0/Q)(rho^n-1)/D >=(3/2)log2.          (6)

The original pair marginals are uniform, so the actual absolute-height bound is h_abs(rho)<=3h_abs(alpha).
For each nonzero nontorsion conjugate rho_i and integer n>=1,

    |rho_i^n-1|<2 max(1,|rho_i|^n).

Off the unit circle strictness follows from 1+R<2max(1,R); on the circle equality would require rho_i^n=-1 and hence rho torsion.
The full archimedean bound is therefore strict:

    log abs Norm_(E0/Q)(rho^n-1)/D
      <log2+n h_abs(rho)<=log2+12r h_abs(alpha).         (7)

Combining (6) and (7) proves the strict bound (3), including its total-measure normalization.
For r=1, more generally A-1 squarings give depth at least A and exponent 2^(A-1), yielding

    (A/2)log2<log2+3*2^(A-1)h_abs(alpha).

Either A=3 or A=4 gives h_abs(alpha)>log2/24, retaining the original unramified specialization.
At fixed ell,j,r the Pisot motion has already shown m(P_alpha)=log alpha tends to infinity.
When the binary ramification varies, j>=r still prevents this family from yielding small total measures through the weakened height floor.
The construction tests the general ramified scope with actual arithmetic fields, but supplies neither automatic near-one coverage nor an effective least-prime or optimized-height statement.


## Author check and present boundary

The complete assembly retains the odd-conductor reduction/inertia argument, exact order through the real and cyclic quotients, explicit binary cyclotomic degree/group/value-group proof, quantitative Hensel separation and primitive preservation, finite-field patterns, simultaneous real/odd-prime/2-adic conditions and full symmetric Galois group.
It also retains the odd cyclic disjointness, exact ramification and residue degrees in the local compositum, the selected finite-order lift, positive unit cone and congruence, primitive trace, irreducible reciprocal polynomial and every original conjugate.
The full even-degree kernel, root-coordinate coboundary, exact orbital/class counts, abelian-subgroup and every-abelian-base lower bounds, all own-ratio fibers and the strict norm-height calculation are included.
This complete author argument awaits a separate whole noncontributor review; author checking and source statement acceptance do not establish independent review or G0001 completion.

## Current assessment
[Selected decision](#decision-current-complete-pair-orbit-home)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T11:39 |
| status | open |
| reason | Register the complete unified actual Salem realization with every binary ramification index r=2^a, exact local degree and selected odd-order residue lift, full regular wreath group, orbital and abelian-base bounds, strict height cost and all unramified specializations. Root and both construction agents contributed; a whole noncontributor review is still required. No near-one family, automatic unrestricted coverage or novelty classification is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete actual-realization statement](#statement) | Every odd prime ell, r=2^a>=1 and j>=max{5,r}; existence and infinitude, original degree and trace field, exact e and residue degree, selected lift and orbital/class counts, every abelian subgroup/base, strict absolute-height and original total-measure bounds. |
| argument | [Complete arithmetic construction](#argument) | Sections1--10 and author boundary, including explicit local field and primitive Hensel neighborhood, simultaneous real/odd-prime constraints, actual local completions, positive unit motion, full Salem kernel, selected pure-shift Frobenius, all group counts and strict own-ratio norm estimate. |
| dependency | [Finite abelian primary factors](../audits/literature/Hun74/Yin_U005.md#hun74-u005) | IV.6.7 and IV.6.9 at PID Z; cyclic ell-primary quotient preserving the order-ell Frobenius. Earlier source inspection scope unchanged. |
| dependency | [Finite-field existence and irreducible degrees](../audits/literature/Hun74/Yin_U006.md#hun74-u006) | Actual V.5.7--V.5.10 statements, monic normalization and finite residue Frobenius; selected statement/applicability acceptance only, not a new Chapter V proof audit. |
| dependency | [Strong complete-field Hensel lifting](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Derivative-sensitive lifting in the actual B/Q2 and F_w, quantitative root separation and later simple reciprocal quadratics; original source-proof limits unchanged. |
| dependency | [Monic rational-factor interface](../audits/literature/Con26d/Yin_U001.md#con26d-u001) | Irreducibility over Q from a monic irreducible reduction; recognized global Eisenstein pattern attribution for q_r, while local degree/ramification are proved directly. |
| dependency | [Actual local decomposition and residue lifts](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Inertia, decomposition groups and arithmetic residue-Frobenius lifts at actual number-field primes; selected finite-order lift distinguished from all possible lifts. Source inspection scope unchanged. |
| dependency | [Full unit lattice](../audits/literature/Con26/Yin_U001.md#con26-u001) | Dirichlet logarithmic lattice of the totally real integer-ring unit group; inherited foundational source-proof limits. |
| dependency | [Strict unit cone consequence](../ledger/Yin_L_G0388_v1.md#actual-order-units-in-every-log-cone) | Actual unit with one expanding embedding and all other embeddings contracting; squaring and a finite congruence power retain this cone. |
| dependency | [Accepted even-trace Salem kernel](../ledger/Yin_L_G0162_v1.md#salem-kernel-class-population) | Even t=M j! complex-conjugation vectors span the complete inversion kernel; full group follows from actual faithful root action and regular trace quotient. Original classical attribution retained. |
| support | [Extra-depth norm antecedent](Yin_C_G0146_v1.md#bounded-class-nonnormal-argument) | Credited prime-power amplification and strict complete norm architecture, fully retained here at exact local e=r and exponent4r. |
| support | [Actual ratio-fiber antecedent](../ledger/Yin_L_G0397_v1.md#full-ratio-orbits) | Credited equal pair-to-ratio fibers and original marginal heights, with the complete actual 2d orbit and own-ratio degree D reconstructed in Section10. |
| support | [Accepted orbital comparison](Yin_C_G0162_v1.md#statement) | This supplies actual arithmetic instances of its s=2,gamma=1 input; C162 is not used as a premise of the realization or the direct height proof. |

### Decision whole-reviewed-2026-10-18

| Field | Value |
| --- | --- |
| date | 2026-10-18T11:48 |
| status | proved |
| reason | Adopt the complete actual Salem construction after R389 whole noncontributor review, including every binary ramification index, precise local completions and selected lift, full regular wreath action, subgroup/base bounds and strict height cost. The later AM16-U003 comparison already covers the qualitative total gap of this entire normal-trace class; this result is an explicit arithmetic control and local quantitative refinement, not new total-gap coverage or a near-one family. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete actual-realization statement](#statement) | Every odd prime ell, r=2^a>=1 and j>=max{5,r}; existence and infinitude, original degree and trace field, exact e and residue degree, selected lift and orbital/class counts, every abelian subgroup/base, strict absolute-height and original total-measure bounds. |
| argument | [Complete arithmetic construction](#argument) | Sections1--10 and author boundary, including explicit local field and primitive Hensel neighborhood, simultaneous real/odd-prime constraints, actual local completions, positive unit motion, full Salem kernel, selected pure-shift Frobenius, all group counts and strict own-ratio norm estimate. |
| dependency | [Finite abelian primary factors](../audits/literature/Hun74/Yin_U005.md#hun74-u005) | IV.6.7 and IV.6.9 at PID Z; cyclic ell-primary quotient preserving the order-ell Frobenius. Earlier source inspection scope unchanged. |
| dependency | [Finite-field existence and irreducible degrees](../audits/literature/Hun74/Yin_U006.md#hun74-u006) | Actual V.5.7--V.5.10 statements, monic normalization and finite residue Frobenius; selected statement/applicability acceptance only, not a new Chapter V proof audit. |
| dependency | [Strong complete-field Hensel lifting](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Derivative-sensitive lifting in the actual B/Q2 and F_w, quantitative root separation and later simple reciprocal quadratics; original source-proof limits unchanged. |
| dependency | [Monic rational-factor interface](../audits/literature/Con26d/Yin_U001.md#con26d-u001) | Irreducibility over Q from a monic irreducible reduction; recognized global Eisenstein pattern attribution for q_r, while local degree/ramification are proved directly. |
| dependency | [Actual local decomposition and residue lifts](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Inertia, decomposition groups and arithmetic residue-Frobenius lifts at actual number-field primes; selected finite-order lift distinguished from all possible lifts. Source inspection scope unchanged. |
| dependency | [Full unit lattice](../audits/literature/Con26/Yin_U001.md#con26-u001) | Dirichlet logarithmic lattice of the totally real integer-ring unit group; inherited foundational source-proof limits. |
| dependency | [Strict unit cone consequence](../ledger/Yin_L_G0388_v1.md#actual-order-units-in-every-log-cone) | Actual unit with one expanding embedding and all other embeddings contracting; squaring and a finite congruence power retain this cone. |
| dependency | [Accepted even-trace Salem kernel](../ledger/Yin_L_G0162_v1.md#salem-kernel-class-population) | Even t=M j! complex-conjugation vectors span the complete inversion kernel; full group follows from actual faithful root action and regular trace quotient. Original classical attribution retained. |
| support | [Extra-depth norm antecedent](Yin_C_G0146_v1.md#bounded-class-nonnormal-argument) | Credited prime-power amplification and strict complete norm architecture, fully retained here at exact local e=r and exponent4r. |
| support | [Actual ratio-fiber antecedent](../ledger/Yin_L_G0397_v1.md#full-ratio-orbits) | Credited equal pair-to-ratio fibers and original marginal heights, with the complete actual 2d orbit and own-ratio degree D reconstructed in Section10. |
| support | [Accepted orbital comparison](Yin_C_G0162_v1.md#statement) | This supplies actual arithmetic instances of its s=2,gamma=1 input; C162 is not used as a premise of the realization or the direct height proof. |
| support | [Existing normal-trace total-gap coverage](../audits/literature/AM16/Yin_U003.md#am16-u003) | The accepted rank-two theorem already covers every actual Galois Salem trace field in total measure. This supplies comparison only, not a premise of this explicit construction or local absolute-height bound. |
| review | [Whole actual-realization finding](../audits/reviews/Yin_R_G0389_v1.md#actual-realization-whole-independent-finding) | Complete fixed statement, all ten proof sections, every declared source and support, exact local/global existence, all original conjugates, group/abelian-base counts, strict ramification-dependent norm bound and prior-coverage limits. |


### Decision current-salem-kernel-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T15:45 |
| status | proved |
| reason | Select C383 as the complete proof home for the identical originally used L162 Salem full/even kernel and trace quotient, retaining the exact consumed cases and classical CM10 attribution/inspection limits. Preserve this Claim statement, argument, status, every other relation and original review scope. The existing reviews retain their actual original inputs; this proof-home decision does not report an earlier review of the later C383 material. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Every odd prime ell, r=2^a>=1 and j>=max{5,r}; existence and infinitude, original degree and trace field, exact e and residue degree, selected lift and orbital/class counts, every abelian subgroup/base, strict absolute-height and original total-measure bounds. |
| argument | [Exact retained argument](#argument) | Sections1--10 and author boundary, including explicit local field and primitive Hensel neighborhood, simultaneous real/odd-prime constraints, actual local completions, positive unit motion, full Salem kernel, selected pure-shift Frobenius, all group counts and strict own-ratio norm estimate. |
| dependency | [Exact retained dependency](../audits/literature/Hun74/Yin_U005.md#hun74-u005) | IV.6.7 and IV.6.9 at PID Z; cyclic ell-primary quotient preserving the order-ell Frobenius. Earlier source inspection scope unchanged. |
| dependency | [Exact retained dependency](../audits/literature/Hun74/Yin_U006.md#hun74-u006) | Actual V.5.7--V.5.10 statements, monic normalization and finite residue Frobenius; selected statement/applicability acceptance only, not a new Chapter V proof audit. |
| dependency | [Exact retained dependency](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Derivative-sensitive lifting in the actual B/Q2 and F_w, quantitative root separation and later simple reciprocal quadratics; original source-proof limits unchanged. |
| dependency | [Exact retained dependency](../audits/literature/Con26d/Yin_U001.md#con26d-u001) | Irreducibility over Q from a monic irreducible reduction; recognized global Eisenstein pattern attribution for q_r, while local degree/ramification are proved directly. |
| dependency | [Exact retained dependency](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Inertia, decomposition groups and arithmetic residue-Frobenius lifts at actual number-field primes; selected finite-order lift distinguished from all possible lifts. Source inspection scope unchanged. |
| dependency | [Exact retained dependency](../audits/literature/Con26/Yin_U001.md#con26-u001) | Dirichlet logarithmic lattice of the totally real integer-ring unit group; inherited foundational source-proof limits. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0388_v1.md#actual-order-units-in-every-log-cone) | Actual unit with one expanding embedding and all other embeddings contracting; squaring and a finite congruence power retain this cone. |
| dependency | [Exact retained dependency](Yin_C_G0383_v1.md#salem-kernel-class-population) | Even t=M j! complex-conjugation vectors span the complete inversion kernel; full group follows from actual faithful root action and regular trace quotient. Original classical attribution retained. |
| support | [Exact retained support](Yin_C_G0146_v1.md#bounded-class-nonnormal-argument) | Credited prime-power amplification and strict complete norm architecture, fully retained here at exact local e=r and exponent4r. |
| support | [Exact retained support](../ledger/Yin_L_G0397_v1.md#full-ratio-orbits) | Credited equal pair-to-ratio fibers and original marginal heights, with the complete actual 2d orbit and own-ratio degree D reconstructed in Section10. |
| support | [Exact retained support](Yin_C_G0162_v1.md#statement) | This supplies actual arithmetic instances of its s=2,gamma=1 input; C162 is not used as a premise of the realization or the direct height proof. |
| support | [Exact retained support](../audits/literature/AM16/Yin_U003.md#am16-u003) | The accepted rank-two theorem already covers every actual Galois Salem trace field in total measure. This supplies comparison only, not a premise of this explicit construction or local absolute-height bound. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0389_v1.md#actual-realization-whole-independent-finding) | Complete fixed statement, all ten proof sections, every declared source and support, exact local/global existence, all original conjugates, group/abelian-base counts, strict ramification-dependent norm bound and prior-coverage limits. |

### Decision current-complete-unit-cone-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T21:36 |
| status | proved |
| reason | Select the already complete C9 home for exactly the previously used L388 local full-order logarithmic-cone argument; the entire original cone proof is present unchanged and the scope stays actual integral units with every designated strict coordinate. Preserve all fields/other relations/review findings and the old actual source-reading record; no earlier reviewer is claimed to have read this later home. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Every odd prime ell, r=2^a>=1 and j>=max{5,r}; existence and infinitude, original degree and trace field, exact e and residue degree, selected lift and orbital/class counts, every abelian subgroup/base, strict absolute-height and original total-measure bounds. |
| argument | [Exact argument](#argument) | Sections1--10 and author boundary, including explicit local field and primitive Hensel neighborhood, simultaneous real/odd-prime constraints, actual local completions, positive unit motion, full Salem kernel, selected pure-shift Frobenius, all group counts and strict own-ratio norm estimate. |
| dependency | [Exact dependency](../audits/literature/Hun74/Yin_U005.md#hun74-u005) | IV.6.7 and IV.6.9 at PID Z; cyclic ell-primary quotient preserving the order-ell Frobenius. Earlier source inspection scope unchanged. |
| dependency | [Exact dependency](../audits/literature/Hun74/Yin_U006.md#hun74-u006) | Actual V.5.7--V.5.10 statements, monic normalization and finite residue Frobenius; selected statement/applicability acceptance only, not a new Chapter V proof audit. |
| dependency | [Exact dependency](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Derivative-sensitive lifting in the actual B/Q2 and F_w, quantitative root separation and later simple reciprocal quadratics; original source-proof limits unchanged. |
| dependency | [Exact dependency](../audits/literature/Con26d/Yin_U001.md#con26d-u001) | Irreducibility over Q from a monic irreducible reduction; recognized global Eisenstein pattern attribution for q_r, while local degree/ramification are proved directly. |
| dependency | [Exact dependency](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Inertia, decomposition groups and arithmetic residue-Frobenius lifts at actual number-field primes; selected finite-order lift distinguished from all possible lifts. Source inspection scope unchanged. |
| dependency | [Exact dependency](../audits/literature/Con26/Yin_U001.md#con26-u001) | Dirichlet logarithmic lattice of the totally real integer-ring unit group; inherited foundational source-proof limits. |
| dependency | [Exact dependency](Yin_C_G0009_v1.md#actual-order-units-in-every-log-cone) | Actual unit with one expanding embedding and all other embeddings contracting; squaring and a finite congruence power retain this cone. |
| dependency | [Exact dependency](Yin_C_G0383_v1.md#salem-kernel-class-population) | Even t=M j! complex-conjugation vectors span the complete inversion kernel; full group follows from actual faithful root action and regular trace quotient. Original classical attribution retained. |
| support | [Exact support](Yin_C_G0146_v1.md#bounded-class-nonnormal-argument) | Credited prime-power amplification and strict complete norm architecture, fully retained here at exact local e=r and exponent4r. |
| support | [Exact support](../ledger/Yin_L_G0397_v1.md#full-ratio-orbits) | Credited equal pair-to-ratio fibers and original marginal heights, with the complete actual 2d orbit and own-ratio degree D reconstructed in Section10. |
| support | [Exact support](Yin_C_G0162_v1.md#statement) | This supplies actual arithmetic instances of its s=2,gamma=1 input; C162 is not used as a premise of the realization or the direct height proof. |
| support | [Exact support](../audits/literature/AM16/Yin_U003.md#am16-u003) | The accepted rank-two theorem already covers every actual Galois Salem trace field in total measure. This supplies comparison only, not a premise of this explicit construction or local absolute-height bound. |
| review | [Exact review](../audits/reviews/Yin_R_G0389_v1.md#actual-realization-whole-independent-finding) | Complete fixed statement, all ten proof sections, every declared source and support, exact local/global existence, all original conjugates, group/abelian-base counts, strict ramification-dependent norm bound and prior-coverage limits. |


### Decision current-complete-pair-orbit-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T23:21 |
| status | proved |
| reason | Select the already complete C477 home for exactly the original L397 ordered-pair/ratio-fiber and full marginal-height mechanism used here. Every original collision, own-field degree, actual unit/non-torsion and fixed scope is present unchanged; only this same-object formal input locator changes. Preserve every other statement/argument/source/support/review relation, mathematical claim, scope and status. The original reviewer is not claimed to have read this later material or R835, and no target or antecedent independent-review obligation is discharged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Every odd prime ell, r=2^a>=1 and j>=max{5,r}; existence and infinitude, original degree and trace field, exact e and residue degree, selected lift and orbital/class counts, every abelian subgroup/base, strict absolute-height and original total-measure bounds. |
| argument | [Exact argument](#argument) | Sections1--10 and author boundary, including explicit local field and primitive Hensel neighborhood, simultaneous real/odd-prime constraints, actual local completions, positive unit motion, full Salem kernel, selected pure-shift Frobenius, all group counts and strict own-ratio norm estimate. |
| dependency | [Exact dependency](../audits/literature/Hun74/Yin_U005.md#hun74-u005) | IV.6.7 and IV.6.9 at PID Z; cyclic ell-primary quotient preserving the order-ell Frobenius. Earlier source inspection scope unchanged. |
| dependency | [Exact dependency](../audits/literature/Hun74/Yin_U006.md#hun74-u006) | Actual V.5.7--V.5.10 statements, monic normalization and finite residue Frobenius; selected statement/applicability acceptance only, not a new Chapter V proof audit. |
| dependency | [Exact dependency](../audits/literature/Con26e/Yin_U001.md#con26e-u001) | Derivative-sensitive lifting in the actual B/Q2 and F_w, quantitative root separation and later simple reciprocal quadratics; original source-proof limits unchanged. |
| dependency | [Exact dependency](../audits/literature/Con26d/Yin_U001.md#con26d-u001) | Irreducibility over Q from a monic irreducible reduction; recognized global Eisenstein pattern attribution for q_r, while local degree/ramification are proved directly. |
| dependency | [Exact dependency](../audits/literature/The26b/Yin_U001.md#the26b-u001) | Inertia, decomposition groups and arithmetic residue-Frobenius lifts at actual number-field primes; selected finite-order lift distinguished from all possible lifts. Source inspection scope unchanged. |
| dependency | [Exact dependency](../audits/literature/Con26/Yin_U001.md#con26-u001) | Dirichlet logarithmic lattice of the totally real integer-ring unit group; inherited foundational source-proof limits. |
| dependency | [Exact dependency](Yin_C_G0009_v1.md#actual-order-units-in-every-log-cone) | Actual unit with one expanding embedding and all other embeddings contracting; squaring and a finite congruence power retain this cone. |
| dependency | [Exact dependency](Yin_C_G0383_v1.md#salem-kernel-class-population) | Even t=M j! complex-conjugation vectors span the complete inversion kernel; full group follows from actual faithful root action and regular trace quotient. Original classical attribution retained. |
| support | [Exact support](Yin_C_G0146_v1.md#bounded-class-nonnormal-argument) | Credited prime-power amplification and strict complete norm architecture, fully retained here at exact local e=r and exponent4r. |
| support | [Exact support](Yin_C_G0477_v1.md#full-ratio-orbits) | Credited equal pair-to-ratio fibers and original marginal heights, with the complete actual 2d orbit and own-ratio degree D reconstructed in Section10. |
| support | [Exact support](Yin_C_G0162_v1.md#statement) | This supplies actual arithmetic instances of its s=2,gamma=1 input; C162 is not used as a premise of the realization or the direct height proof. |
| support | [Exact support](../audits/literature/AM16/Yin_U003.md#am16-u003) | The accepted rank-two theorem already covers every actual Galois Salem trace field in total measure. This supplies comparison only, not a premise of this explicit construction or local absolute-height bound. |
| review | [Exact review](../audits/reviews/Yin_R_G0389_v1.md#actual-realization-whole-independent-finding) | Complete fixed statement, all ten proof sections, every declared source and support, exact local/global existence, all original conjugates, group/abelian-base counts, strict ramification-dependent norm bound and prior-coverage limits. |

