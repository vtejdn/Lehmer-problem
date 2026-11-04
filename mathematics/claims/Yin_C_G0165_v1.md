---
author: Yin
---
# Exact degree and measure costs of Salem monomial auxiliaries

Date: 2026-10-18T11:54.
Human author Yin.
Root proposed the off-pair ratio-injectivity and radial-distribution question after the bounded-orbital prior-coverage screen, and then supplied the monomial generalization, torsion-prefix argument and uniform all-support refinement using the accepted Salem kernel and fixed-rank AM16 input.
The loglog_cyclic_review author performs the reuse check, checks the stabilizer and height interfaces and develops the complete unified argument below.
Root and this author are contributors, not independent reviewers of this account.
No numerical test, polynomial construction, prime scan or new source acquisition is performed.
This is a complete author-level structural diagnosis prepared for separate whole review; no original Lehmer gap or independent acceptance is asserted.

<a id="off-pair-salem-ratio-reuse"></a>
## Reuse and classical attribution

The required multiplicative independence is OLD.
The accepted [L176 joint phase account](../ledger/Yin_L_G0176_v1.md#salem-joint-phase-density) gives the complete Galois/modulus proof that one chosen neutral root from each Salem inverse pair has no nontrivial torsion-valued product.
Its [R75 whole noncontributor review](../audits/reviews/Yin_R_G0075_v1.md#periodic-loop-control-independent-review) explicitly checks that proof and its torsion-valued extension.
The surrounding control theorem in L176 assumes the Salem number lies in (1,2), but the independence proof only uses its unique real exterior/interior pair and exterior root greater than1.
The classical statement itself is for every genuine Salem number.

The actual retained [Dub23 primary article](../literature/pdf/Dub23.pdf), Section2, printed page863 / PDF page2, was reread directly with pdftotext for this inquiry.
Its paragraph before Lemma5 states rational independence of pi and the arguments of one root from each neutral conjugate pair, for a Salem number of arbitrary degree d>=4.
It attributes the result to Salem's 1963 book page32 and credits the argument to Pisot.
The existing [source-reading account](../audits/literature/Dub23/readme.md) retains that exact attribution and the limit that the original monograph was not directly inspected.
No novelty or new source-proof audit is claimed for the independence assertion below.

The bounded local reuse screen also read [L397 exact pair degrees, fibers and heights](../ledger/Yin_L_G0397_v1.md#full-ratio-orbits), [L162 actual Salem kernel](../ledger/Yin_L_G0162_v1.md#salem-kernel-class-population), [C146v2 own-ratio normalization](Yin_C_G0146_v2.md#ratio-own-field-author-calculation) and [C162](Yin_C_G0162_v1.md#statement).
Those inputs retain possible ratio collisions and a height inequality for GENERAL units.
The exact off-pair Salem injectivity and full radial equalities below were not found in the inspected scopes.
This bounded absence is not an exhaustive priority search or a novelty claim.
The [AM16-U004 off-pair screen](../audits/literature/AM16/Yin_U004.md#am16-u004) already proves independence of each pair and its classical subdegree consequence; the present argument addresses the whole ratio map and exact cost rather than a new gap domain.
The accepted [AM16-U005 fixed-rank source input](../audits/literature/AM16/Yin_U005.md#am16-u005) supplies the general fixed rank r at base Q and the actual JOINT field degree.
The complete primary Theorem2.1 statement across printed pages1--2 / PDF pages2--3 was also directly reread for this assembly.
Its constant C_r(epsilon) is fixed only after r and epsilon are fixed; the source's original deep proof is not newly audited.
For the uniform bound over ALL support sizes, only its FIXED rank2 and epsilon=1/4 instance is used.
The extra group input is the accepted even-weight inversion kernel in L162, with the classical CM10 attribution and [R61 acceptance](../audits/reviews/Yin_R_G0061_v1.md#complete-independent-written-review-and-adoption) retained at their existing scopes.
The uniform all-support deduction is not obtained by treating the varying-rank constants C_r as uniform.

## Statement

<a id="off-pair-salem-ratio-statement"></a>
### A. Exact off-pair statement

Let alpha>1 be a genuine Salem number of degree d=2t>=4, with roots X, normal closure L and G=Gal(L/Q).
Write m=log alpha=d h_abs(alpha)>0.
Choose ANY ordered pair (x,y) of roots lying in different inverse pairs, so y is neither x nor x^(-1), and let

    Omega=G.(x,y),
    s=|G_x.y|,
    |Omega|=[Q(x,y):Q]=sd.

For every integer p>=2, in particular every rational prime p, put rho=x^p/y.
Then the map (z,w) maps to z^p/w is injective on ALL ordered pairs of roots from different inverse pairs, and hence on Omega.
Consequently

    Q(rho)=Q(x,y),
    D=[Q(rho):Q]=sd.                                   (1)

More strongly, for every positive integer n,

    Q(rho^n)=Q(x,y), deg(rho^n)=sd.                      (2)

This power-stability conclusion follows from the specific Salem independence proof; it is not inferred from the [C218 single-prime degree condition](Yin_C_G0218_v1.md#power-degree-reduction).

The D distinct conjugates of rho have the following exact modulus multiplicities:

| Modulus | Number of distinct conjugates |
| --- | --- |
| alpha^p | s |
| alpha^(-p) | s |
| alpha | s |
| alpha^(-1) | s |
| 1 | s(d-4) |

In particular,

    m(rho)=s(p+1)m,
    h_abs(rho)=(p+1)m/d,
    house(rho)=alpha^p,                                (3)

and rho has exactly2s conjugates outside and2s inside the unit circle.
The remaining s(d-4) conjugates lie on it.
For rho^n replace each displayed modulus by its n-th power; its total measure is n s(p+1)m.
Every assertion includes p=2,d=4 and an arbitrary starting root x.
Only off-pair orbitals are asserted here: the diagonal and inverse orbitals are excluded from the hypothesis.

<a id="fixed-support-salem-monomial-statement"></a>
### B. General monomial statement and uniform all-support exclusion

For the same genuine Salem input, choose r roots x_1,...,x_r from distinct inverse pairs, where 1<=r<=t, and nonzero integers a_1,...,a_r.
Set

    beta=product_(i=1)^r x_i^(a_i),
    A=sum_i |a_i|,
    N=[Q(beta):Q], J=[Q(x_1,...,x_r):Q].

Then beta is a nontorsion algebraic integer unit, and

    h_abs(beta)=A m/d,
    m(beta)=N A m/d,
    N<=J<=r! N,
    N>=t/r=d/(2r).                                    (4)

For every positive integer n, Q(beta^n)=Q(beta), and m(beta^n)=n m(beta).
If the absolute values |a_i| are pairwise distinct, then J=N and Q(beta)=Q(x_1,...,x_r).
For r=1 one has the stronger exact values N=J=d and m(beta)=|a_1|m.

For each FIXED r>=2 and FIXED 0<epsilon<1-1/r, the accepted AM16 source constant gives

    m(beta)>=A C_r(epsilon)(r!)^(-1/r-epsilon)
                   N^(1-1/r-epsilon).                   (5)

Consequently, for fixed r>=2, EVERY sequence of such monomials along genuine Salem inputs with original d tending to infinity has m(beta) tending to infinity, even if the coefficients a_i vary.
There is no bounded-total-measure sequence within this class, and in particular no total-measure-to-zero sequence, irrespective of the behavior of m(alpha).
This is a direct prior-source consequence of the exact field/height accounting, not a new multivariate height theorem.
Formula(5) alone supplies no uniform constant when r grows; the stronger fixed-rank2 argument below resolves that case separately.

Put C_*=C_2(1/4)>0 from the accepted rank-two source.
For EVERY effective support size 2<=r<=t, including r growing with d, one has

    N>=2^(r-1)t/r>=t r^2/8,
    m(beta)>=C_* A N^(1/4)/[r(r-1)]^(3/4)
            >=C_* N^(1/4)/sqrt(r)
            >=C_* (d/16)^(1/4).                         (6)

The same constant works for all genuine Salem inputs, all effective support sizes r>=2 and all nonzero integer coefficients.
Thus EVERY sequence of these multiroot monomials along unbounded original Salem degrees has total measure tending to infinity, even when the support size varies.
For an arbitrary root of unity zeta, possibly outside L, put beta_zeta=zeta beta and N_zeta=[Q(beta_zeta):Q].
Then

    Q(beta) is contained in Q(beta_zeta),
    h_abs(beta_zeta)=h_abs(beta),
    m(beta_zeta)=(N_zeta/N)m(beta)>=m(beta).              (7)

Consequently (6) also holds for arbitrary torsion prefactors.
Effective support zero gives torsion and is excluded; effective support one gives the single-root powers specified above and is outside (6).

For the off-pair ratio, r=2, A=p+1 and J=N=D=sd, so the factorial loss can be omitted:

    m(rho)>=(p+1) C_2(epsilon)D^(1/2-epsilon).           (8)

At epsilon=1/4 the right side is (p+1)C_2(1/4)D^(1/4).
This grows along every unbounded original-degree sequence because D>=d, with p>=2 either fixed or varying.
The conclusion concerns TOTAL measure; small absolute heights remain possible and are not excluded by these bounds.

<a id="argument"></a>
## Complete argument

<a id="off-pair-salem-ratio-proof"></a>
### 1. Reused independence with its full needed scope

Choose one root u_i from each of the t inverse pairs of X, including one of alpha,alpha^(-1) from the real pair.
Suppose integers a_i satisfy

    product_i u_i^(a_i)=zeta

for a root of unity zeta.
For any fixed i, choose g in G with g(u_i)=alpha.
Inversion commutes with G, so u_i^(-1) is the unique root mapping to alpha^(-1).
Since the representatives contain only one root from each inverse pair, every g(u_j) with j!=i lies on the unit circle.
Taking absolute values of the transformed equality gives alpha^(a_i)=1, hence a_i=0.
This holds for every i, and then zeta=1.
Thus the u_i are multiplicatively independent even modulo roots of unity.
This is exactly the classical Galois/modulus argument used in L176, with the harmless real-pair representative included.
Equivalently, the multiplicative group generated by all Salem roots is free abelian of rank t, with inversion as the only relations between the paired generators.
No classification of G or full inversion kernel is needed for this conclusion.

### 2. Injectivity of the actual ratio and each positive power

Represent every root uniquely as u_i^epsilon with epsilon in {1,-1}.
For an off-pair ordered pair (u_i^epsilon,u_j^delta), i!=j, its ratio has exponent vector

    p epsilon e_i-delta e_j in Z^t.                      (9)

If two such ratios are equal, their exponent-vector difference gives a multiplicative relation among the u_i, so their vectors coincide.
Each vector in (9) has exactly two nonzero coordinates, one of absolute value p and one of absolute value1.
Since p>=2 these coordinates are distinguishable: the magnitude-p coordinate recovers i and epsilon; the magnitude1 coordinate recovers j and delta.
Thus the ordered pairs coincide.
This proof covers p=2 without a cancellation exception.

The map is G-equivariant, so its image on Omega is precisely the full conjugate set of rho.
Injectivity therefore gives D=|Omega|=sd.
Since rho lies in Q(x,y), equality of degrees proves the field identity (1).
For positive powers, equality of two n-th powers of ratios means their quotient is a root of unity.
The stronger torsion-valued independence just proved again forces equality of the vectors in (9), hence equality of the pairs.
Applying the same orbit and field-degree argument proves (2).
The ratio is itself nontorsion because its vector (9) is nonzero; it is an algebraic integer unit because both roots are integer units.

### 3. Complete radial multiplicities and equality of the height cost

The two coordinate projections Omega to X are equivariant and onto, each with constant fiber size s, as in L397.
Membership in different inverse pairs is G-invariant, so EVERY pair in Omega remains off-pair.
If its first coordinate is alpha, its second coordinate is on the unit circle; exactly s such pairs give modulus alpha^p.
If its first coordinate is alpha^(-1), exactly s such pairs give modulus alpha^(-p).
If its second coordinate is alpha, its first coordinate is on the unit circle; exactly s such pairs give modulus alpha^(-1).
If its second coordinate is alpha^(-1), exactly s such pairs give modulus alpha.

These four sets are disjoint.
Indeed a pair with both coordinates in the real pair would violate the off-pair hypothesis.
All remaining sd-4s=s(d-4) pairs have both coordinates on the unit circle and give modulus1.
By injectivity these are counts of DISTINCT actual ratio conjugates, not only of pair labels.
Because p>=2 and alpha>1 the four displayed nonunit moduli are distinct.
The positive logarithmic sum is therefore s p log alpha+s log alpha, proving the total measure in (3).
Division by the actual degree sd proves its absolute-height equality, and the largest modulus is alpha^p.
The same count and (2) prove the asserted positive-power formulas.

At d=4 the last row is zero, and the four disjoint classes still exhaust all sd conjugates.
The proof does not assume x itself is alpha; the uniform projections count the real roots wherever they occur in the orbit.
No total reality of the trace field, special Galois group, selected prime or ramification hypothesis is involved.

<a id="fixed-support-salem-monomial-proof"></a>
### 4. Exact height and field degree for every supported monomial

Extend the selected x_i to one oriented representative from every inverse pair.
Section1 gives independence modulo roots of unity of this entire t-tuple.
Let v in Z^t be the exponent vector with entries a_i on the chosen r representatives and zero elsewhere.
The action of G on these generators is by signed permutations, and beta corresponds to v.
Independence says g(beta)=beta exactly when g(v)=v.
It also says beta is nontorsion and g(beta^n)=beta^n exactly when g(v)=v for every positive n.
Thus N is the actual size of the orbit G.v, and the stabilizers of beta and beta^n agree.
Galois correspondence proves Q(beta^n)=Q(beta).
Integrality and unit status hold even for negative a_i, since the original roots are integer units.

To compute the height, average log^+|g(beta)| over every g in G; the constant stabilizer multiplicity makes this exactly h_abs(beta).
For any given g, at most one chosen inverse pair can map to the unique real exterior/interior pair.
All other factors have modulus1, so there is no cancellation among two nonzero logarithmic contributions:

    log^+|g(beta)|=sum_i log^+|g(x_i)^(a_i)|.

For each fixed i, transitivity distributes g(x_i) uniformly over all d original roots.
If a_i>0 its sole positive term comes from alpha; if a_i<0 it comes from alpha^(-1).
In either case the average is |a_i| log alpha/d.
Summing proves h_abs(beta)=A m/d and hence m(beta)=N A m/d.
This argument averages over G before canceling the beta-stabilizer multiplicity; it does not assume that N/d or separate radial counts for each i are integers.

Let H be the pointwise stabilizer of the oriented roots x_1,...,x_r, and K=G_beta the stabilizer of v.
Then H is contained in K, J=[G:H], N=[G:K], and J/N=[K:H].
An element of K permutes the r support inverse pairs.
Once that permutation is given, each orientation is forced by the nonzero coefficients: if pair i maps to pair j, its sign must be a_j/a_i in {1,-1}.
An element in the kernel of this support permutation fixes each pair and must have positive sign on it; it therefore fixes every x_i and lies in H.
Conversely H is in this kernel.
It follows that H is normal in K and K/H embeds into S_r, yielding [K:H]<=r! and the joint-degree bound in (4).
If the |a_i| are pairwise distinct, the support permutation must be identity, giving H=K and J=N.
There is no additional factor2^r: the nonzero coefficients have already determined all support signs.

The action of G on all t inverse pairs is transitive.
The union of the supports of the N vectors in G.v is therefore the entire t-element pair set.
Each such support has size r, giving t<=rN and the lower degree bound in (4).
For r=1, all d oriented roots give distinct powers x_1^(a_1), since a collision would give a torsion-valued relation between distinct generators or opposite signs of the same nonzero generator.
Hence N=J=d and m(beta)=|a_1|m.
The height and total-measure power formulas follow directly from the same exponent-vector argument and h_abs(beta^n)=n h_abs(beta).

### 5. The fixed-rank source consequence and exact ratio specialization

For fixed r and epsilon>0, AM16-U005 applied to the multiplicatively independent x_1,...,x_r gives

    h_abs(alpha)>=C_r(epsilon)J^(-1/r-epsilon).

All these conjugates have the same absolute height m/d.
Using the ACTUAL joint degree J<=r!N from Section4 gives

    h_abs(alpha)>=C_r(epsilon)(r!N)^(-1/r-epsilon).

Multiplying by N A and using the exact monomial height proves (5).
For fixed r>=2 choose any fixed epsilon strictly between0 and1-1/r.
The exponent1-1/r-epsilon is then positive, A>=r and N>=d/(2r), so (5) tends to infinity as the original d tends to infinity.
This covers varying nonzero integer coefficient vectors at the same fixed support cardinality.
Every positive power only multiplies total measure while preserving degree and support, so taking powers gives no exception.

For rho=x^p/y with p>=2 the two coefficients p,-1 have distinct absolute values.
Sections2--3 already give J=N=D=sd and h_abs(rho)=(p+1)h_abs(alpha).
The fixed rank-two source bound therefore yields (8) directly with no factor2! loss.
At epsilon=1/4 it excludes even bounded total auxiliary measure along unbounded original Salem degrees, regardless of whether the original total measures themselves tend to zero.
No original-degree d is substituted for the joint or own degree D in this deduction.
Neither r nor epsilon is allowed to vary while treating C_r(epsilon) as one fixed positive constant.

<a id="all-support-salem-monomial-proof"></a>
### 6. Uniform all-support bound from rank two and the actual inversion kernel

Keep the exponent vector v, its support S of size r>=2 and its stabilizer K=G_beta.
Choose any two of the selected oriented roots x_i,x_j, i!=j, and put

    J_2=[Q(x_i,x_j):Q]=|G.(x_i,x_j)|.

As shown in Section4, K permutes S and the coefficients force the orientation on every image.
There are at most r(r-1) possible ordered support images of x_i,x_j, each with at most one admissible pair of signs.
Hence |K.(x_i,x_j)|<=r(r-1).
Writing G as N left cosets of K expresses its pair orbit as a union of N translates of that K-orbit, giving

    J_2<=N r(r-1).                                    (10)

This is a union bound; the translates may overlap.
It does NOT assume that the full pair stabilizer is contained in K, nor that its joint field contains Q(beta).

The two roots are multiplicatively independent by Section1 and have the same height h_abs(alpha).
The fixed rank-two AM16 input with epsilon=1/4 therefore gives

    h_abs(alpha)>=C_* J_2^(-3/4)
                 >=C_*[N r(r-1)]^(-3/4).

Multiplying by N A and using the EXACT height identity in (4) gives

    m(beta)>=C_* A N^(1/4)/[r(r-1)]^(3/4)
            >=C_* N^(1/4)/sqrt(r),                     (11)

because A>=r and r/[r(r-1)]^(3/4)>=1/sqrt(r).
Only the fixed constant C_* occurs here, regardless of r.

Now use the ACTUAL inversion kernel V in the Salem Galois group.
Accepted L162 says it contains the even-weight subgroup E_t of (C2)^t; for even t it is the full subgroup, but that strengthening is unnecessary here.
Let the distinct support sets of vectors in G.v form the family F.
The top action is transitive on all t inverse pairs, so these r-element supports cover the pair set, and |F|>=t/r.
For each support S' in F choose one exponent vector v' in G.v with that support.
The even-weight flips preserve S' and change signs of its nonzero coefficients.
If r<t, every sign pattern on S' extends to an even-weight pattern by using a coordinate outside S', giving 2^r distinct vectors.
If r=t, the even-weight patterns give 2^(r-1) distinct vectors.
In both cases there are at least 2^(r-1) distinct vectors in G.v with that fixed support; nonzero coefficients and the torsion-free exponent representation prevent identifications.
Vectors having different supports are distinct.
Therefore

    N=|G.v|>=2^(r-1)|F|>=2^(r-1)t/r.                  (12)

For every integer r>=2,

    2^(r-1)>=r^3/8.

At r=2,3,4 this is respectively 2>=1, 4>=27/8 and 8=8.
For r>=4 the ratio of successive values of 2^(r-1)/r^3 is 2(r/(r+1))^3>=128/125>1.
This proves the inequality for all remaining r without a numerical search.
Consequently (12) gives N>=t r^2/8.
Substitution into (11) yields

    m(beta)>=C_*(t/8)^(1/4)=C_*(d/16)^(1/4),

which proves (6) uniformly over all supports and coefficients.
The argument uses neither a varying-rank height theorem nor a factorial asymptotic.

<a id="salem-monomial-torsion-prefactors"></a>
### 7. Arbitrary torsion prefactors cannot lower the cost

Let zeta be any root of unity of finite order n, with no requirement that zeta lie in L, and put beta_zeta=zeta beta.
Then beta_zeta^n=beta^n.
The all-positive-power field identity proved in Section4 gives

    Q(beta)=Q(beta^n)=Q(beta_zeta^n)
       contained in Q(beta_zeta).

Root-of-unity multiplication preserves the absolute height at every place.
Thus N_zeta/N is a positive integer and (7) follows from the exact total-measure normalization.
The untwisted beta is an integer unit and nontorsion, so the same is true of beta_zeta.
This proves that no external torsion factor can evade (6) by reducing its own field degree.
It does not assert that Q(beta_zeta^n)=Q(beta_zeta): the torsion prefactor can increase the field, while the required lower containment remains valid.

## Consequence for the high-subdegree ratio route

For an actual off-pair Salem C162 input, neither of its inequalities D<=sd and m(rho)<=s(p+1)m can provide a hidden saving: both are equalities.
The sharper own-ratio field of C146v2 is exactly the pair field here, and every positive power retains that degree.
For a prime p, C162's canonical exponent n=p^ceil(log_p D) therefore obeys

    sd<=n<p sd,
    s(p+1)m<=n h_abs(rho)<p s(p+1)m.                 (13)

At unbounded s this specific exponent is not bounded by a fixed multiple of the original d.
The auxiliary total-measure cost is exactly s(p+1), so it cannot be reduced by collapsing conjugate ratio labels or strengthening the marginal-height triangle bound for this same auxiliary.
On the high-subdegree Salem frontier from AM16-U004 this identifies a real expense, not a new route to avoid the already covered bounded-subdegree class.
By (8), the canonical quantity n h_abs(rho)>=m(rho) itself tends to infinity along unbounded original degrees.
Thus this canonical amplification cannot remain in the small-positive-height-parameter regime of the C147 envelope along that sequence.
This does not forbid small h_abs(rho) itself or another exponent justified by different arithmetic information.

The conclusion does not rule out angular cancellation in the full cyclic norm, a different exponent choice justified by additional valuations, another auxiliary, or another arithmetic mechanism.
The all-support obstruction applies after combining inverse-pair exponents and discarding zeros, for every effective support r>=2 and arbitrary torsion prefactors.
Single-root powers remain the explicit r=1 exception, and zero support is torsion.
Nonmonomial sums, norm expressions whose effective monomial support collapses to at most one, and different arithmetic constructions require separate analysis.
It also does not identify gamma with all residue coincidences or assert an exact finite-place matching population: additional compatible reductions can occur even though the algebraic ratios are distinct.
There is no automatic small-prime or near-one coverage result for the original unrestricted Salem inputs.

## Author check

The author checked the classical source interface, torsion-valued independence and real-pair extension, injectivity at p=2, recovery of both signs from (9), arbitrary root/orbit choices, exact joint field and every power degree, both marginal fibers and disjoint real-coordinate cases, d=4, all unit-circle counts and the total-versus-absolute-height normalization.
The checks also cover the full-group monomial height average, forced support signs and the exact K/H kernel without an extra2^r, J versus N, transitive support-cover lower bound, r=1 boundary, fixed-rank AM16 normalization, coefficient variation, degree growth and every fixed-parameter restriction.
The all-support checks retain the K-pair orbit and coset union without a false stabilizer inclusion, distinct even-kernel sign vectors above EACH support, the r=t endpoint, d=4, every small integer in the exponential bound, the uniform constant C_*, and the external-torsion field containment without claiming full power stability of a twist.
The useful new retained content is the complete specialized degree/radial accounting, the general monomial stabilizer and exact height account, and the uniform all-support prior-source consequence; classical independence, the Salem kernel and multivariate height are explicitly credited and not presented as newly discovered theorems.
The comparison remains author-level pending the main agent's decision about fixed retention or a separate review.

## Current assessment
[Selected decision](#decision-current-complete-pair-orbit-home)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `unreviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T12:08 |
| status | open |
| reason | Register the complete Salem monomial diagnosis: exact off-pair ratio degree, all powers and radial populations; exact general monomial height and stabilizer cost; uniform all-support total-measure divergence from the accepted inversion kernel and fixed rank-two height bound; arbitrary torsion prefactors and all zero/single-support boundaries. Root and the author contribute; separate whole noncontributor review is required. Classical independence, kernel classification and multivariate height are credited, and no original unrestricted gap or novelty classification is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete Salem monomial statement](#statement) | Every genuine Salem input, all off-pair roots and integers p>=2, exact ratio field and every positive-power degree, complete radial populations; all integer monomials in distinct inverse pairs, any support size, exact height and degree bounds, fixed-rank refinement, uniform all-support estimate and external torsion prefactors. |
| argument | [Complete structural proof and consequences](#argument) | Sections1--7, canonical C147-parameter comparison and author boundary; torsion-valued independence, exponent-vector injectivity, all fibers and radial counts, support-stabilizer signs, coset pair bound without false subgroup inclusion, every support's even-kernel signs, elementary exponential estimate and exact total-height normalization. |
| dependency | [Classical Salem independence mechanism and attribution](../ledger/Yin_L_G0176_v1.md#salem-joint-phase-density) | Reuse of the complete Galois/modulus argument including torsion-valued products and its exact Dub23 printed863/PDF2 attribution to Salem1963 page32 and Pisot; the local proof needs only alpha>1 and includes the real-pair representative, with no control or phase-density theorem consumed and no direct inspection of the original monograph. |
| dependency | [Actual pair-field and coordinate fibers](../ledger/Yin_L_G0397_v1.md#full-ratio-orbits) | Exact pair-orbit degree and uniform coordinate projections; injectivity and radial equalities are proved for the present off-pair Salem domain rather than assumed for general units. |
| dependency | [Accepted Salem inversion kernel](../ledger/Yin_L_G0162_v1.md#salem-kernel-class-population) | Containment of every even-weight flip in the actual kernel, including all odd/even t cases; used above EACH support to count at least2^(r-1) distinct exponent vectors. Original CM10 attribution and accepted scope unchanged. |
| dependency | [Fixed rank-two height input](../audits/literature/AM16/Yin_U003.md#am16-u003) | Only its exact K=Q,r=2 source statement, with fixed epsilon=1/4 for the uniform all-support constant and arbitrary fixed epsilon for the ratio refinement; no normal-trace premise or ambient-Galois-degree substitution. |
| dependency | [Optional fixed-rank height refinement](../audits/literature/AM16/Yin_U005.md#am16-u005) | Exact fixed r and epsilon joint-degree theorem for formula(5); not used with varying r to obtain the all-support bound. Original deep-proof inspection limits unchanged. |
| support | [Earlier own-ratio normalization](Yin_C_G0146_v2.md#ratio-own-field-author-calculation) | Comparison with the general smaller-own-field possibility; the present Salem off-pair equality removes that possible saving at this exact auxiliary. |
| support | [Actual orbital criterion](Yin_C_G0162_v1.md#statement) | Definitions of s,D and canonical exponent, for the exact high-subdegree diagnostic; no gap inequality from that criterion is a premise of the monomial theorem. |
| support | [Complete cyclic parameter domain](Yin_C_G0147_v5.md#statement) | Only its actual parameter n h_abs(rho) and small-positive-parameter domain in the canonical comparison; no angular substitute or inverse theorem is used to prove the lower bounds. |
| support | [Classical off-pair subdegree frontier](../audits/literature/AM16/Yin_U004.md#am16-u004) | Prior rank-two coverage and necessary subdegree growth in hypothetical Salem zero-gap sequences; the present exact costs supply no new original-input gap domain. |
| support | [Single-prime descent boundary](../ledger/Yin_L_G0014_v1.md#power-degree-reduction) | Its endpoint is not silently promoted to arbitrary-power stability; every positive-power field identity here is proved directly from Salem independence. |

### Decision whole-reviewed-2026-10-18

The recorded review description was `independently reviewed`.

| Field | Value |
| --- | --- |
| date | 2026-10-18T12:22 |
| status | proved |
| reason | Adopt the complete Salem monomial theorem after R391 whole noncontributor review. Exact off-pair degrees and radial costs, every power, general stabilizer/height accounting, the uniform all-support bound using a fixed rank-two source constant, arbitrary external torsion factors and every zero/single-support exception are covered. This obstructs the stated auxiliary constructions; it neither proves the original Salem gap nor closes nonmonomial or different-exponent arithmetic mechanisms. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete Salem monomial statement](#statement) | Every genuine Salem input, all off-pair roots and integers p>=2, exact ratio field and every positive-power degree, complete radial populations; all integer monomials in distinct inverse pairs, any support size, exact height and degree bounds, fixed-rank refinement, uniform all-support estimate and external torsion prefactors. |
| argument | [Complete structural proof and consequences](#argument) | Sections1--7, canonical C147-parameter comparison and author boundary; torsion-valued independence, exponent-vector injectivity, all fibers and radial counts, support-stabilizer signs, coset pair bound without false subgroup inclusion, every support's even-kernel signs, elementary exponential estimate and exact total-height normalization. |
| dependency | [Classical Salem independence mechanism and attribution](../ledger/Yin_L_G0176_v1.md#salem-joint-phase-density) | Reuse of the complete Galois/modulus argument including torsion-valued products and its exact Dub23 printed863/PDF2 attribution to Salem1963 page32 and Pisot; the local proof needs only alpha>1 and includes the real-pair representative, with no control or phase-density theorem consumed and no direct inspection of the original monograph. |
| dependency | [Actual pair-field and coordinate fibers](../ledger/Yin_L_G0397_v1.md#full-ratio-orbits) | Exact pair-orbit degree and uniform coordinate projections; injectivity and radial equalities are proved for the present off-pair Salem domain rather than assumed for general units. |
| dependency | [Accepted Salem inversion kernel](../ledger/Yin_L_G0162_v1.md#salem-kernel-class-population) | Containment of every even-weight flip in the actual kernel, including all odd/even t cases; used above EACH support to count at least2^(r-1) distinct exponent vectors. Original CM10 attribution and accepted scope unchanged. |
| dependency | [Fixed rank-two height input](../audits/literature/AM16/Yin_U003.md#am16-u003) | Only its exact K=Q,r=2 source statement, with fixed epsilon=1/4 for the uniform all-support constant and arbitrary fixed epsilon for the ratio refinement; no normal-trace premise or ambient-Galois-degree substitution. |
| dependency | [Optional fixed-rank height refinement](../audits/literature/AM16/Yin_U005.md#am16-u005) | Exact fixed r and epsilon joint-degree theorem for formula(5); not used with varying r to obtain the all-support bound. Original deep-proof inspection limits unchanged. |
| support | [Earlier own-ratio normalization](Yin_C_G0146_v2.md#ratio-own-field-author-calculation) | Comparison with the general smaller-own-field possibility; the present Salem off-pair equality removes that possible saving at this exact auxiliary. |
| support | [Actual orbital criterion](Yin_C_G0162_v1.md#statement) | Definitions of s,D and canonical exponent, for the exact high-subdegree diagnostic; no gap inequality from that criterion is a premise of the monomial theorem. |
| support | [Complete cyclic parameter domain](Yin_C_G0147_v5.md#statement) | Only its actual parameter n h_abs(rho) and small-positive-parameter domain in the canonical comparison; no angular substitute or inverse theorem is used to prove the lower bounds. |
| support | [Classical off-pair subdegree frontier](../audits/literature/AM16/Yin_U004.md#am16-u004) | Prior rank-two coverage and necessary subdegree growth in hypothetical Salem zero-gap sequences; the present exact costs supply no new original-input gap domain. |
| support | [Single-prime descent boundary](../ledger/Yin_L_G0014_v1.md#power-degree-reduction) | Its endpoint is not silently promoted to arbitrary-power stability; every positive-power field identity here is proved directly from Salem independence. |
| review | [Whole independent Salem monomial finding](../audits/reviews/Yin_R_G0391_v1.md#whole-salem-monomial-finding) | Entire statement, all seven proof sections, source/dependency/support declarations and canonical-parameter consequences; exact all-support kernel/sign counts, fixed rank-two constant, all powers and arbitrary external torsion prefixes, with all exceptions and source-proof limits retained. |

### Decision current-prime-input-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T03:04 |
| status | proved |
| reason | Select adopted C218 as the current complete home of the identical retained L14 degree-lowering-prime argument. Its actual selected adoption, complete norm/Bezout proof and precise endpoint were read: the retained endpoint quantifies over primes only and supplies no arbitrary-power stability to this Salem monomial theorem, whose stronger field identities remain locally proved. Mathematical status, statement, complete argument, selected findings, actual review relationships and every relation scope remain unchanged; this is current proof-location maintenance, with no new review and no discharge of existing repaired-proof re-review obligations. All original dated decisions and R bindings retain their actual old inputs and declarations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete Salem monomial statement](#statement) | Every genuine Salem input, all off-pair roots and integers p>=2, exact ratio field and every positive-power degree, complete radial populations; all integer monomials in distinct inverse pairs, any support size, exact height and degree bounds, fixed-rank refinement, uniform all-support estimate and external torsion prefactors. |
| argument | [Complete structural proof and consequences](#argument) | Sections1--7, canonical C147-parameter comparison and author boundary; torsion-valued independence, exponent-vector injectivity, all fibers and radial counts, support-stabilizer signs, coset pair bound without false subgroup inclusion, every support's even-kernel signs, elementary exponential estimate and exact total-height normalization. |
| dependency | [Classical Salem independence mechanism and attribution](../ledger/Yin_L_G0176_v1.md#salem-joint-phase-density) | Reuse of the complete Galois/modulus argument including torsion-valued products and its exact Dub23 printed863/PDF2 attribution to Salem1963 page32 and Pisot; the local proof needs only alpha>1 and includes the real-pair representative, with no control or phase-density theorem consumed and no direct inspection of the original monograph. |
| dependency | [Actual pair-field and coordinate fibers](../ledger/Yin_L_G0397_v1.md#full-ratio-orbits) | Exact pair-orbit degree and uniform coordinate projections; injectivity and radial equalities are proved for the present off-pair Salem domain rather than assumed for general units. |
| dependency | [Accepted Salem inversion kernel](../ledger/Yin_L_G0162_v1.md#salem-kernel-class-population) | Containment of every even-weight flip in the actual kernel, including all odd/even t cases; used above EACH support to count at least2^(r-1) distinct exponent vectors. Original CM10 attribution and accepted scope unchanged. |
| dependency | [Fixed rank-two height input](../audits/literature/AM16/Yin_U003.md#am16-u003) | Only its exact K=Q,r=2 source statement, with fixed epsilon=1/4 for the uniform all-support constant and arbitrary fixed epsilon for the ratio refinement; no normal-trace premise or ambient-Galois-degree substitution. |
| dependency | [Optional fixed-rank height refinement](../audits/literature/AM16/Yin_U005.md#am16-u005) | Exact fixed r and epsilon joint-degree theorem for formula(5); not used with varying r to obtain the all-support bound. Original deep-proof inspection limits unchanged. |
| support | [Earlier own-ratio normalization](Yin_C_G0146_v2.md#ratio-own-field-author-calculation) | Comparison with the general smaller-own-field possibility; the present Salem off-pair equality removes that possible saving at this exact auxiliary. |
| support | [Actual orbital criterion](Yin_C_G0162_v1.md#statement) | Definitions of s,D and canonical exponent, for the exact high-subdegree diagnostic; no gap inequality from that criterion is a premise of the monomial theorem. |
| support | [Complete cyclic parameter domain](Yin_C_G0147_v5.md#statement) | Only its actual parameter n h_abs(rho) and small-positive-parameter domain in the canonical comparison; no angular substitute or inverse theorem is used to prove the lower bounds. |
| support | [Classical off-pair subdegree frontier](../audits/literature/AM16/Yin_U004.md#am16-u004) | Prior rank-two coverage and necessary subdegree growth in hypothetical Salem zero-gap sequences; the present exact costs supply no new original-input gap domain. |
| support | [Single-prime descent boundary](Yin_C_G0218_v1.md#power-degree-reduction) | Its endpoint is not silently promoted to arbitrary-power stability; every positive-power field identity here is proved directly from Salem independence. |
| review | [Actual selected finding](../audits/reviews/Yin_R_G0391_v1.md#whole-salem-monomial-finding) | Entire statement, all seven proof sections, source/dependency/support declarations and canonical-parameter consequences; exact all-support kernel/sign counts, fixed rank-two constant, all powers and arbitrary external torsion prefixes, with all exceptions and source-proof limits retained. |

### Decision current-salem-kernel-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T15:45 |
| status | proved |
| reason | Select C383 as the complete proof home for the identical originally used L162 Salem full/even kernel and trace quotient, retaining the exact consumed cases and classical CM10 attribution/inspection limits. Preserve this Claim statement, argument, status, every other relation and original review scope. The existing reviews retain their actual original inputs; this proof-home decision does not report an earlier review of the later C383 material. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Every genuine Salem input, all off-pair roots and integers p>=2, exact ratio field and every positive-power degree, complete radial populations; all integer monomials in distinct inverse pairs, any support size, exact height and degree bounds, fixed-rank refinement, uniform all-support estimate and external torsion prefactors. |
| argument | [Exact retained argument](#argument) | Sections1--7, canonical C147-parameter comparison and author boundary; torsion-valued independence, exponent-vector injectivity, all fibers and radial counts, support-stabilizer signs, coset pair bound without false subgroup inclusion, every support's even-kernel signs, elementary exponential estimate and exact total-height normalization. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0176_v1.md#salem-joint-phase-density) | Reuse of the complete Galois/modulus argument including torsion-valued products and its exact Dub23 printed863/PDF2 attribution to Salem1963 page32 and Pisot; the local proof needs only alpha>1 and includes the real-pair representative, with no control or phase-density theorem consumed and no direct inspection of the original monograph. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0397_v1.md#full-ratio-orbits) | Exact pair-orbit degree and uniform coordinate projections; injectivity and radial equalities are proved for the present off-pair Salem domain rather than assumed for general units. |
| dependency | [Exact retained dependency](Yin_C_G0383_v1.md#salem-kernel-class-population) | Containment of every even-weight flip in the actual kernel, including all odd/even t cases; used above EACH support to count at least2^(r-1) distinct exponent vectors. Original CM10 attribution and accepted scope unchanged. |
| dependency | [Exact retained dependency](../audits/literature/AM16/Yin_U003.md#am16-u003) | Only its exact K=Q,r=2 source statement, with fixed epsilon=1/4 for the uniform all-support constant and arbitrary fixed epsilon for the ratio refinement; no normal-trace premise or ambient-Galois-degree substitution. |
| dependency | [Exact retained dependency](../audits/literature/AM16/Yin_U005.md#am16-u005) | Exact fixed r and epsilon joint-degree theorem for formula(5); not used with varying r to obtain the all-support bound. Original deep-proof inspection limits unchanged. |
| support | [Exact retained support](Yin_C_G0146_v2.md#ratio-own-field-author-calculation) | Comparison with the general smaller-own-field possibility; the present Salem off-pair equality removes that possible saving at this exact auxiliary. |
| support | [Exact retained support](Yin_C_G0162_v1.md#statement) | Definitions of s,D and canonical exponent, for the exact high-subdegree diagnostic; no gap inequality from that criterion is a premise of the monomial theorem. |
| support | [Exact retained support](Yin_C_G0147_v5.md#statement) | Only its actual parameter n h_abs(rho) and small-positive-parameter domain in the canonical comparison; no angular substitute or inverse theorem is used to prove the lower bounds. |
| support | [Exact retained support](../audits/literature/AM16/Yin_U004.md#am16-u004) | Prior rank-two coverage and necessary subdegree growth in hypothetical Salem zero-gap sequences; the present exact costs supply no new original-input gap domain. |
| support | [Exact retained support](Yin_C_G0218_v1.md#power-degree-reduction) | Its endpoint is not silently promoted to arbitrary-power stability; every positive-power field identity here is proved directly from Salem independence. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0391_v1.md#whole-salem-monomial-finding) | Entire statement, all seven proof sections, source/dependency/support declarations and canonical-parameter consequences; exact all-support kernel/sign counts, fixed rank-two constant, all powers and arbitrary external torsion prefixes, with all exceptions and source-proof limits retained. |

### Decision current-salem-independence-proof-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T18:55 |
| status | proved |
| reason | Select C417v3 as the complete current home of the identical original L176 Galois/modulus independence argument and its exact Dub23 attribution/inspection boundary, now retained at Dub23-U001. The entire current argument was compared, including torsion-valued products and its beta>1 scope; this Claim's own real-pair extension remains locally proved. Only this formal dependency locator changes: no control/phase-density conclusion is consumed. Preserve the statement, argument, status, every other relation and scope, and actual selected R391 finding/unknown relationship. This proof-home decision performs no new review, does not claim R391 inspected the later C/U materials, and does not discharge the original unknown whole independent-review obligation. All original dated decisions and their actual reading facts remain fixed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Every genuine Salem input, all off-pair roots and integers p>=2, exact ratio field and every positive-power degree, complete radial populations; all integer monomials in distinct inverse pairs, any support size, exact height and degree bounds, fixed-rank refinement, uniform all-support estimate and external torsion prefactors. |
| argument | [Exact retained argument](#argument) | Sections1--7, canonical C147-parameter comparison and author boundary; torsion-valued independence, exponent-vector injectivity, all fibers and radial counts, support-stabilizer signs, coset pair bound without false subgroup inclusion, every support's even-kernel signs, elementary exponential estimate and exact total-height normalization. |
| dependency | [Exact retained dependency](Yin_C_G0417_v3.md#salem-joint-phase-density) | Reuse of the complete Galois/modulus argument including torsion-valued products and its exact Dub23 printed863/PDF2 attribution to Salem1963 page32 and Pisot; the local proof needs only alpha>1 and includes the real-pair representative, with no control or phase-density theorem consumed and no direct inspection of the original monograph. |
| dependency | [Exact retained dependency](../ledger/Yin_L_G0397_v1.md#full-ratio-orbits) | Exact pair-orbit degree and uniform coordinate projections; injectivity and radial equalities are proved for the present off-pair Salem domain rather than assumed for general units. |
| dependency | [Exact retained dependency](Yin_C_G0383_v1.md#salem-kernel-class-population) | Containment of every even-weight flip in the actual kernel, including all odd/even t cases; used above EACH support to count at least2^(r-1) distinct exponent vectors. Original CM10 attribution and accepted scope unchanged. |
| dependency | [Exact retained dependency](../audits/literature/AM16/Yin_U003.md#am16-u003) | Only its exact K=Q,r=2 source statement, with fixed epsilon=1/4 for the uniform all-support constant and arbitrary fixed epsilon for the ratio refinement; no normal-trace premise or ambient-Galois-degree substitution. |
| dependency | [Exact retained dependency](../audits/literature/AM16/Yin_U005.md#am16-u005) | Exact fixed r and epsilon joint-degree theorem for formula(5); not used with varying r to obtain the all-support bound. Original deep-proof inspection limits unchanged. |
| support | [Exact retained support](Yin_C_G0146_v2.md#ratio-own-field-author-calculation) | Comparison with the general smaller-own-field possibility; the present Salem off-pair equality removes that possible saving at this exact auxiliary. |
| support | [Exact retained support](Yin_C_G0162_v1.md#statement) | Definitions of s,D and canonical exponent, for the exact high-subdegree diagnostic; no gap inequality from that criterion is a premise of the monomial theorem. |
| support | [Exact retained support](Yin_C_G0147_v5.md#statement) | Only its actual parameter n h_abs(rho) and small-positive-parameter domain in the canonical comparison; no angular substitute or inverse theorem is used to prove the lower bounds. |
| support | [Exact retained support](../audits/literature/AM16/Yin_U004.md#am16-u004) | Prior rank-two coverage and necessary subdegree growth in hypothetical Salem zero-gap sequences; the present exact costs supply no new original-input gap domain. |
| support | [Exact retained support](Yin_C_G0218_v1.md#power-degree-reduction) | Its endpoint is not silently promoted to arbitrary-power stability; every positive-power field identity here is proved directly from Salem independence. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0391_v1.md#whole-salem-monomial-finding) | Entire statement, all seven proof sections, source/dependency/support declarations and canonical-parameter consequences; exact all-support kernel/sign counts, fixed rank-two constant, all powers and arbitrary external torsion prefixes, with all exceptions and source-proof limits retained. |


### Decision current-complete-pair-orbit-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T23:21 |
| status | proved |
| reason | Select the already complete C477 home for exactly the original L397 ordered-pair/ratio-fiber and full marginal-height mechanism used here. Every original collision, own-field degree, actual unit/non-torsion and fixed scope is present unchanged; only this same-object formal input locator changes. Preserve every other statement/argument/source/support/review relation, mathematical claim, scope and status. The original reviewer is not claimed to have read this later material or R835, and no target or antecedent independent-review obligation is discharged. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Every genuine Salem input, all off-pair roots and integers p>=2, exact ratio field and every positive-power degree, complete radial populations; all integer monomials in distinct inverse pairs, any support size, exact height and degree bounds, fixed-rank refinement, uniform all-support estimate and external torsion prefactors. |
| argument | [Exact argument](#argument) | Sections1--7, canonical C147-parameter comparison and author boundary; torsion-valued independence, exponent-vector injectivity, all fibers and radial counts, support-stabilizer signs, coset pair bound without false subgroup inclusion, every support's even-kernel signs, elementary exponential estimate and exact total-height normalization. |
| dependency | [Exact dependency](Yin_C_G0417_v3.md#salem-joint-phase-density) | Reuse of the complete Galois/modulus argument including torsion-valued products and its exact Dub23 printed863/PDF2 attribution to Salem1963 page32 and Pisot; the local proof needs only alpha>1 and includes the real-pair representative, with no control or phase-density theorem consumed and no direct inspection of the original monograph. |
| dependency | [Exact dependency](Yin_C_G0477_v1.md#full-ratio-orbits) | Exact pair-orbit degree and uniform coordinate projections; injectivity and radial equalities are proved for the present off-pair Salem domain rather than assumed for general units. |
| dependency | [Exact dependency](Yin_C_G0383_v1.md#salem-kernel-class-population) | Containment of every even-weight flip in the actual kernel, including all odd/even t cases; used above EACH support to count at least2^(r-1) distinct exponent vectors. Original CM10 attribution and accepted scope unchanged. |
| dependency | [Exact dependency](../audits/literature/AM16/Yin_U003.md#am16-u003) | Only its exact K=Q,r=2 source statement, with fixed epsilon=1/4 for the uniform all-support constant and arbitrary fixed epsilon for the ratio refinement; no normal-trace premise or ambient-Galois-degree substitution. |
| dependency | [Exact dependency](../audits/literature/AM16/Yin_U005.md#am16-u005) | Exact fixed r and epsilon joint-degree theorem for formula(5); not used with varying r to obtain the all-support bound. Original deep-proof inspection limits unchanged. |
| support | [Exact support](Yin_C_G0146_v2.md#ratio-own-field-author-calculation) | Comparison with the general smaller-own-field possibility; the present Salem off-pair equality removes that possible saving at this exact auxiliary. |
| support | [Exact support](Yin_C_G0162_v1.md#statement) | Definitions of s,D and canonical exponent, for the exact high-subdegree diagnostic; no gap inequality from that criterion is a premise of the monomial theorem. |
| support | [Exact support](Yin_C_G0147_v5.md#statement) | Only its actual parameter n h_abs(rho) and small-positive-parameter domain in the canonical comparison; no angular substitute or inverse theorem is used to prove the lower bounds. |
| support | [Exact support](../audits/literature/AM16/Yin_U004.md#am16-u004) | Prior rank-two coverage and necessary subdegree growth in hypothetical Salem zero-gap sequences; the present exact costs supply no new original-input gap domain. |
| support | [Exact support](Yin_C_G0218_v1.md#power-degree-reduction) | Its endpoint is not silently promoted to arbitrary-power stability; every positive-power field identity here is proved directly from Salem independence. |
| review | [Exact review](../audits/reviews/Yin_R_G0391_v1.md#whole-salem-monomial-finding) | Entire statement, all seven proof sections, source/dependency/support declarations and canonical-parameter consequences; exact all-support kernel/sign counts, fixed rank-two constant, all powers and arbitrary external torsion prefixes, with all exceptions and source-proof limits retained. |



## Unselected complete-packet comparison

The following original AD99 application retains its complete group-count, projective-height and conditional-gap comparison at a fixed mathematical home.
It is a supplementary comparison, outside this family's selected original monomial statement and its old review scope; no new assessment is selected for it and no old review is enlarged.
The accepted external input is [AD99 Theorem1.6](../audits/literature/AD99/Yin_U001.md#exact-selected-statement): for each fixed n, product h_abs(x_i)>=c_prod(n) D^(-1)[log(3D)]^(-n kappa(n)), where kappa(n)=(n+1)((n+1)!)^n-n and D is the actual joint degree.
That displayed inequality is denoted (1) within this supplement; its source-proof and unspecified-constant limits remain at AD99 U001.

<a id="complete-salem-packet-specialization"></a>
### Direct complete-Salem-packet specialization

Let alpha>1 be a genuine Salem number of original degree d=2t>=4 and total measure m=log alpha.
Let L be its normal closure and choose one root beta_j from each of its t distinct inverse pairs.
Every beta_j is an algebraic integer unit with h_abs(beta_j)=m/(2t).
The tuple is multiplicatively independent by the [complete inverse-pair argument already fixed above](#off-pair-salem-ratio-proof); no normal-trace or full-kernel hypothesis is needed.

The selected roots and their inverses contain all roots, so Q(beta_1,...,beta_t)=L.
Thus the actual joint degree is D=[L:Q], not d, and D<=2^t t! from the faithful inverse-pair permutation action.
For actual full signed-symmetric root action C2 wreath S_t, equality holds: D=2^t t!.
At t>=3 this is a genuine high-subdegree benchmark: the off-pair subdegree is d-2, and the actual trace field of degree t is not Galois because its S_(t-1) stabilizer is not normal in S_t.
These are conditional counts on that actual root action, not a new field realization or an assertion that every Salem polynomial has that group.

The packet's logarithmic geometry is sparse but pays an exact rank factor.
At every embedding of L exactly one selected coordinate has logarithmic absolute value +m or -m and all other coordinates have logarithmic absolute value zero.
Each chosen beta_j takes each original root value at exactly D/d embeddings.
Consequently

    h(1:beta_1:...:beta_t)=m/2,
    sum_j h_abs(beta_j)=m/2,
    max_j h_abs(beta_j)=m/(2t).                         (2)

More generally, for every integer vector a=(a_1,...,a_t), the same complete embedding count gives

    h_abs(product_j beta_j^(a_j))
      =(m/(2t)) sum_j |a_j|.                           (3)

All finite-place terms are zero because these are units.
Thus the disjoint logarithmic supports do not permit replacing projective height m/2 by the maximum coordinate height m/(2t).
Equations(2)--(3) are direct finite embedding calculations for this application, not a source theorem with an assumed rank-uniform constant.

Applying(1) with the actual n=t gives

    m >= 2t c_prod(t)^(1/t) D^(-1/t)
             [log(3D)]^(-kappa(t)).                   (4)

In the full-group benchmark the degree-only prefactor is

    2t/(2^t t!)^(1/t)=t/(t!)^(1/t),

which stays between 1 and e and tends to e.
This favorable factorial cancellation does not remove either c_prod(t)^(1/t) or the logarithmic loss with kappa(t).
One may always replace the unspecified positive c_prod(t) by min(c_prod(t),1); with that legitimate guaranteed choice the recorded bound's right side tends to zero because the logarithmic loss grows without bound.
This does not bound the optimal possible source constant from above; it says that the inspected theorem supplies no uniform compensating lower estimate for it.
The separately explicit [Del09 substitution](../audits/literature/Del09/Yin_U001.md#del09-u001) gives a fully numerical failure without any unknown-constant issue.

### Exact missing input and the bounded stop

A sufficient new estimate on the actual full signed-symmetric Salem packets would be a constant c>0, independent of t and the input, such that

    D product_j h_abs(beta_j) >= c^t.                  (5)

No such assertion follows from(1).
On this benchmark(5) is quantitatively equivalent, up to an absolute factor e, to a uniform Salem measure gap on that very class.
Indeed its left side is m^t t!/t^t, so(5) gives m>=c t/(t!)^(1/t)>=c.
Conversely a measure gap m>=delta gives that left side at least(delta/e)^t, using t!>=(t/e)^t.
Thus(5) is a substantive new height theorem, not a cheap additional group hypothesis or a source-constant substitution.
The ordinary rank-two result cannot cover this near-linear off-pair subdegree by its fixed sublinear-power criterion, while fixed-rank conclusions cannot silently use n=t.

The bounded feasibility test is complete: the exact current source penalties do not produce a positive degree-uniform bound from the full packet.
No parameter search, group construction, projection computation or source-proof reconstruction is warranted by this substitution alone.
Further work on(5) would need a genuinely new proof using the complete sparse logarithmic geometry, with total logarithmic penalty O(t); the present source screen supplies no such proof.
The separate original-projection frontier remains an independent question; neither the old Newton Toeplitz identities in L9/L10 nor C161's incomplete coefficient-field orbit is a substitute arithmetic upper bound.
No C, T, E or S decision is changed by this retained comparison.
