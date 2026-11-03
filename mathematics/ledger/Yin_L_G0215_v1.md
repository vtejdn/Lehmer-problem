---
author: Yin
---

# Actual affine growth and the limit of accumulated mixing defects

Current complete proof home: [C522](../claims/Yin_C_G0522_v1.md#growth-defect-fixed-scope), selected with [the actual complete current whole SELF](../audits/reviews/Yin_R_G0730_v1.md#current-affine-matching-whole-self-finding).
The [original R111 whole](../audits/reviews/Yin_R_G0111_v1.md#growth-defect-complete-independent-review) remains UNKNOWN at its actual frozen input; its original independent wording/verdict and dates are preserved rather than retrospectively reclassified as SELF or asserted isolation.
The [complete original author checking/contribution account](../audits/reviews/Yin_R_G0730_v1.md#original-affine-matching-author-whole-self-finding) is separately SELF; current SELF does not close the old UNKNOWN or select/resume research Task/E.

Date: 2026-10-10.
The coordinating AI for Yin adopts this restricted result after complete separately organized noncontributor review under the continuing G0001 authorization.
This is fixed mathematical retention, not Task completion or acceptance of an unrestricted Claim.

<a id="growth-defect-fixed-scope"></a>
## Current adopted scope

The complete original binary-law proof gives a degree-block collision inequality with an explicit integer-mixing affinity constant and optimized block-matching statistic.
Two actual algebraic-unit families with opposite asymptotic growth have the same entire optimized matching profile.
The torsion controls have extensive strictness at every scale but a total excess bounded by O(d), uniformly in block number.
This establishes a precise failure of automatic accumulation, while leaving conditional innovation and lag-sensitive algebraic constraints as open questions.
The positive control has fixed non-small measure and does not refute a near-one reciprocal theorem.

G0001 remains unresolved.

<a id="complete-retained-proof-and-review"></a>
## Complete retained author proof and independent review

## Affine growth, finite quotients and actual multiscale constraints

Date: 2026-10-10.
Starting question: Rotate explicit effort to S2: seek a genuinely changed affine semigroup growth or original binary-law constraint using multiscale, finite quotients, additive structure or return geometry.
Preserve fixed dimension, original nonsymmetric generators, the high-degree torsion controls and every asymptotic cost.

Current author result: an exact original-binary Fourier block bound, a quantitative integer-mixing defect and a matching refinement at every block number, together with actual high-degree torsion controls showing why this defect does not accumulate into a growth exponent.
The complete derivation and author self-check were frozen for separate review at 2026-10-09T20:48.
The unrestricted Task remains unresolved.

### Reuse and changed mechanism

The author read [S2](../strategies/Yin_S_G0002.md), the original-binary increment and approximate-invariance argument [L92](Yin_L_G0092_v1.md#decreasing-binary-entropy-increments), the exponential inverse-concentration limitation [L93](Yin_L_G0093_v1.md#power-orbit-inverse-time-cost), and the actual group-growth normalization [L96](Yin_L_G0096_v1.md#group-growth-mahler-cost).
The finite-field perfect-uniformity obstruction in [L81](Yin_L_G0081_v1.md#prime-order-small-binary-quotients) and the full-tail/free-window warnings of S2 remain in force.
None of those statements turns a finite-block entropy value into a lower asymptotic rate.

The present discriminator uses the exact torus integral for the original binary collision probability.
It quantifies the defect in the degree-block Holder inequality by the mixing of integral coordinates, with no stationary law, changed digits, assumed Mahler lower bound, or growing matrix representation of the affine semigroup.
The auxiliary torus densities used to measure this defect are normalized Fourier integrands, not stationary laws on the actual return core.
The power-coordinate dimension d records arithmetic degree; the two affine generators still act in GL_2(C).

The local G-ledger search for block Holder defects, integer-coordinate mixing and multiscale collision controls found the related mechanisms above, but not the specific inequality proved here.
This bounded reuse screen is not a novelty claim.
The radical product law used for the explicit controls is already fixed in [C212 radical-product proof](../claims/Yin_C_G0212_v1.md#radical-collision-control), with its actual relative-degree requirement.
All new inequalities below are elementary finite Fourier, Holder and probability arguments, with their proofs given here.
No new research-source theorem or program is required; the explicit torsion controls use the elementary cyclotomic degree formula.
The coordinator supplied the broad research question only, and none of the deductions below.

<a id="original-binary-degree-block-holder"></a>
### 1. The exact degree-block baseline

Let alpha be an algebraic unit, O=Z[alpha], d=[Q(alpha):Q], and A the integral unimodular matrix of multiplication by alpha in the actual power basis 1,alpha,...,alpha^(d-1).
Torsion inputs are allowed.
For independent fair bits xi_j define

    X_n=sum_(j=0)^(n-1) xi_j alpha^j,
    p_n=sum_x Pr(X_n=x)^2,     H_2(n)=-log p_n.

The affine words generated by x -> alpha x and x -> alpha x+1 have exactly these endpoint fibers after reversing the order of the independent bits.
All logarithms are natural.
The original word probabilities remain 2^(-n).

On the normalized torus (R/Z)^d put

    f(t)=product_(j=1)^d cos^2(pi t_j),
    U=(A^d)^transpose,
    I_k=binom(2k,k)/4^k,      Z_k=I_k^d.                 (1)

The collision Fourier identity and the actual d-step power basis give, for every integer k>=1,

    p_(kd)=integral product_(b=0)^(k-1) f(U^b t) dt,
    integral f(t)^k dt=Z_k,
    p_(kd)<=I_k^d<=(k+1)^(-d/2).                       (2)

Indeed the squared modulus of the Fourier transform of one fair bit of weight v is cos^2(pi <v,t>).
Consecutive degree blocks have weight matrices A^(bd).
Orthogonality of integer characters gives the first identity; no approximate conjugates occur.
Every U^b preserves Haar measure since A is unimodular.
Holder with k equal exponents gives the first inequality.
The constant Fourier coefficient of cos^(2k)(pi t) is I_k.
Finally I_0=1 and

    I_(k+1)/I_k=(2k+1)/(2k+2)<=sqrt((k+1)/(k+2))

prove the second inequality by induction; after squaring and clearing denominators the difference is 3k+2>0.

Adding independent digits contracts the l2 norm of a probability, either by the triangle inequality for convolution or directly by the extra factors cos^2<=1.
Thus for arbitrary n>=d the same upper bound applies with k=floor(n/d).
This is a polynomial-in-time bound, not a positive asymptotic exponent.

For k>=2 equality in the first inequality of(2) holds exactly when U is a signed permutation matrix.
To see necessity, equality in Holder forces all f(U^b t)^k, with their equal integrals, to agree almost everywhere.
Thus f(Ut)=f(t).
In the Fourier expansion of f, the largest nonconstant coefficients, each 2^(-d-1), occur exactly at the 2d frequencies +/-e_j.
The torus automorphism permutes coefficients by U^transpose, so these frequencies must be permuted.
This is exactly the signed-permutation condition.
Conversely such a U preserves f, giving equality at every k.
If A^d is a signed permutation, a power of A^d is the identity, so alpha is a root of unity.
Therefore every nontorsion input has strict inequality at every k>=2.
Some torsion inputs also have strict inequality; that distinction is essential below.

The baseline is attained in unbounded degree: take d a power of two and alpha primitive of order 2d, with minimal polynomial t^d+1.
Then A^d=-I, and the d independent residue classes of exponents give p_(kd)=I_k^d exactly.
These actual fixed-2-dimensional affine inputs have collision-free words for n<=d and zero asymptotic growth.

<a id="integer-mixing-uniform-holder-defect"></a>
### 2. A quantitative integer-coordinate defect, uniform in block number

For V in GL_d(Z), let r(V) be the maximum number of rows which each have at least two nonzero entries and whose sets of nonzero column positions are pairwise disjoint.
Define

    R(V)=max(r(V),r(V^(-1))),
    c=sqrt(1015)/32<1.                                  (3)

All rows of a unimodular integer matrix are primitive.
Thus a row with only one nonzero entry has that entry +/-1.
If every row has just one entry, invertibility forces distinct occupied columns, and V is a signed permutation.
Consequently

    R(V)=0 iff V is a signed permutation,
    1<=R(V)<=floor(d/2) otherwise.                       (4)

The upper bound follows because every chosen row consumes at least two disjoint column positions.
This is a statistic of the specified actual power coordinates, not an invariant under arbitrary changes of integral basis.

For every integer k>=1 define the product probability density

    nu_k(t)=f(t)^k/Z_k.

We claim the Hellinger affinity, defined by integral sqrt(ab) for two probability densities a,b, satisfies

    integral sqrt(nu_k(t) nu_k(Vt)) dt <= c^R(V).       (5)

Here nu_k(Vt) is the density of (V^(-1))_*nu_k.
Invariance of affinity under invertible changes of variables allows comparison of nu_k with V_*nu_k instead, and also interchanges V with V^(-1).

To prove the claim, the one-coordinate density is

    w_k(t)=cos^(2k)(pi t)/I_k,
    a_k(j)=integral exp(2pi i j t) w_k(t) dt
          =binom(2k,k+j)/binom(2k,k) for |j|<=k,

and a_k(j)=0 otherwise.
These coefficients are real, nonnegative and nonincreasing as |j| increases.
Put ell=floor(sqrt(k)) and a=a_k(ell).
The following elementary bounds hold uniformly:

    1/4<=a<=3/4.                                        (6)

For ell=1, k is 1,2 or3, and a=k/(k+1).
For ell>=2, the product formula and log(1+x)<=x give

    log a=-sum_(j=0)^(ell-1) log(1+(2j+1)/(k-j))
          >=-ell^2/(k-ell+1)>=-4/3.

The last ratio is largest at k=ell^2 and ell=2.
The inequality log(1+x)>=x/(1+x) similarly gives

    log a<=-ell^2/(k+ell)<=-ell/(ell+3)<=-2/5,

since k< (ell+1)^2.
The elementary bounds log2>2/3 and log(4/3)<1/3 imply exp(-4/3)>1/4 and exp(-2/5)<3/4, proving(6).
For example log2>2/3 follows by integrating 1/x on [1,2] and strict Jensen, or by pairing x and 3-x; no asymptotic binomial approximation is used.

Take one row v of V with at least two nonzero integer entries.
Under nu_k the coordinates t_j are independent with law w_k.
The corresponding output coordinate Y=sum_j v_j t_j mod1 has

    E cos(2pi ell Y)=product_j a_k(ell v_j)<=a^2,

whereas the target one-coordinate law has expectation a.
Their difference is at least a(1-a)>=3/16.
Because the test cosine is bounded in absolute value by one, their total variation is at least3/32.
For any two probabilities P,Q the Cauchy--Schwarz inequality gives

    TV(P,Q)<=sqrt(1-Aff(P,Q)^2).

This follows by factoring |p-q| as |sqrt(p)-sqrt(q)|(sqrt(p)+sqrt(q)) with a common dominating measure.
Hence the marginal affinity is at most c in(3).

For r(V) rows with disjoint input supports, the corresponding coordinates of V_*nu_k are independent.
The target coordinates are independent as well, so their joint affinity is the product of the marginal affinities, at most c^r(V).
Marginalization can only increase affinity, by Cauchy--Schwarz in each conditional fiber.
The full affinity is therefore no larger.
Apply the same argument to V^(-1) and use its symmetry to obtain(5).
Integer coefficients are crucial: they make each nonzero |ell v_j| at least ell and permit the monotone Fourier-coefficient bound.

<a id="affine-block-matching-defect"></a>
### 3. Pair matching of actual time blocks

For k>=2 let M be any matching of the k block indices 0,...,k-1: its edges are disjoint unordered pairs, with unpaired indices allowed.
Define the exactly specified finite statistic

    B_k(U)=(2/k) max_M sum_({a,b} in M) R(U^(b-a)),
    0<=B_k(U)<=floor(d/2).                              (7)

For each pair orient a<b; using R(V)=R(V^(-1)) makes the orientation immaterial.
The original collision law satisfies

    p_(kd)<=I_k^d c^B_k(U),
    H_2(kd)>=-d log I_k+B_k(U) log(1/c).                 (8)

Indeed group the integrand in(2) into pair products and remaining single factors.
Apply generalized Holder with exponent k/2 for each pair and exponent k for each singleton; the reciprocal exponents sum to one.
For a paired lag h=b-a, Haar invariance gives

    integral [f(U^a t)f(U^b t)]^(k/2) dt
       =Z_k integral sqrt(nu_k(t)nu_k(U^h t)) dt
       <=Z_k c^R(U^h).

Each unpaired integral is Z_k.
Multiplying the bounds with their Holder powers proves(8), then maximize over matchings.
These are bounds on one common integral; no independence of distinct pairs or cross-scale defect is assumed.

In particular consecutive pairing gives

    B_k(U)>=(2 floor(k/2)/k) R(U).                       (9)

For nontorsion alpha, U^h is never a signed permutation for h!=0, since otherwise A would have finite order.
Thus B_k(U)>=2 floor(k/2)/k.
The bound is strict by an explicit fixed factor uniformly over all k>=2 and all nontorsion units.
Nevertheless the correction in(8) is at most(d/2)log(1/c), independent of k.
Dividing by kd makes this certified correction vanish.
It supplies no lower asymptotic entropy or growth exponent, even before degree is allowed to vary.

The statistic can distinguish actual coordinate structures and certify an extensive-in-degree defect at finite times.
Its meaning is stronger than merely detecting a short relation, but weaker than a time-linear entropy gain.
The examples below show that this limitation is not just looseness in the displayed upper bound for B_k.

<a id="identical-matching-profile-opposite-growth"></a>
### 4. Identical full matching profiles with opposite affine growth

Let r=2^j, j>=0, and d=2r.
Compare these actual algebraic units:

    alpha_- = a primitive (6r)-th root of unity,
    P_-(t)=t^(2r)-t^r+1;

    alpha_+ = phi^(1/r)>1,   phi=(1+sqrt5)/2,
    P_+(t)=t^(2r)-t^r-1.                                (10)

Both displayed polynomials are irreducible of degree2r.
For P_-, its roots are exactly the primitive 6r-th roots: if t^r has order6 and r is a power of two, t has order6r.
The elementary cyclotomic degree is phi_Euler(6r)=2r, so P_- is that cyclotomic polynomial.
For P_+, the retained norm argument in L5 applies directly: each stage has even degree and constant term-1, so the norm of its positive root is-1.
It cannot be a square in its field, since the rational norm of a square is a square.
Repeatedly adjoining a square root therefore doubles the degree and proves the assertion.
The actual relative degree over Q(alpha_+^r)=Q(phi), or over Q(alpha_-^r)=Q(zeta_6), is r.

Reorder the power basis into pairs (alpha^j,alpha^(j+r)), 0<=j<r.
This is only a coordinate permutation.
For u=alpha^r, multiplication by u has the same 2-by-2 block in each pair,

    B_delta = [[0,delta],[1,1]],
    B_delta^2 = [[delta,delta],[1,delta+1]],

with delta=-1 in the torsion case and delta=1 in the positive case.
Thus U=(A^d)^transpose is a direct sum of r copies of (B_delta^2)^transpose.
Each block has a mixed row, so R(U)=r in both cases; the upper bound d/2 makes this exact.
Consecutive pairings now show that, for every k>=2, the COMPLETE optimized matching statistic is identical:

    B_k(U_-) = B_k(U_+)
              = (2 floor(k/2)/k) r.                     (11)

Indeed this is attained by consecutive pairs, while any matching has at most floor(k/2) edges and every R is at most r.
It is unnecessary to assert that every individual lag statistic agrees: in the torsion case U_-^3=I, whereas no nonzero power of U_+ is a signed permutation.
Optimizing over matchings discards that distinction.

The original law itself distinguishes the families at a short explicit time.
Relative field-basis independence, with the independent bits grouped by their exponent modulo r, gives

    p_(Nr)(alpha_-) = p_N(zeta_6)^r,
    p_(Nr)(alpha_+) = p_N(phi)^r.                        (12)

This is the exact L5 radical product mechanism; there is no division by r in the limiting rate.
At N=4,

    p_4(zeta_6)=1/8,     p_4(phi)=3/32,
    p_(2d)(alpha_-)/I_2^d = (8/9)^r,
    p_(2d)(alpha_+)/I_2^d = (2/3)^r.                     (13)

For a direct finite verification without a program, use basis(1,u).
If u=phi, its first four powers are (1,0),(0,1),(1,1),(1,2).
The 16 binary words have eight singleton fibers and four fibers of size2; hence their collision numerator is8+4*4=24 over256.
If u=zeta_6, the four powers are (1,0),(0,1),(-1,1),(-1,0).
At second coordinate0,1,2 the nonzero fiber multiplicities are respectively(1,2,1), (1,3,3,1), (1,2,1); their squared sums are6,20,6, giving32 over256.
These counts are finite algebraic calculations, not an executed computational certificate.

For each fixed r, the torsion family's asymptotic support, Shannon and collision rates are zero.
Since alpha_- has finite order6r, there are only6r possible power values.
The original endpoint support at length n has at most(n+1)^(6r) values.
All three entropy rates are nonnegative and bounded above by log support/n, which tends to zero.
This concerns the actual nonsymmetric two-generator affine semigroup, whose common linear part at time n is alpha_-^n; no symmetric growth comparison is used.

In contrast the positive family's original collision and support rates are at least(log2)/2, without invoking a lower bound for its Mahler measure.
At the base input phi, condition on all odd-position bits.
The remaining even-position weights are (phi^2)^j with phi^2>2.
Their binary sums are distinct: the largest differing power strictly exceeds the sum of all smaller powers.
Every conditional atom is therefore at most2^(-ceil(n/2)), and so is every unconditional atom.
Collision probability is at most the largest atom.
Thus

    p_n(phi)<=2^(-ceil(n/2)),
    liminf_n H_2(n;phi)/n >=(log2)/2.

The exact residue-class product decomposition for n=qr+s has s classes of length q+1 and r-s of length q; for each fixed r it transfers the same lower rate to alpha_+.
Support and Shannon entropy dominate collision entropy.
The positive family has M(P_+)=phi, from its r expanding roots of modulus phi^(1/r), so it is not a near-one family and lies outside the unresolved reciprocal core.
Its measure is recorded as scope, not used as the growth lower premise.

Both families have degree d and exactly2^n distinct words for every n<=d, by power-basis independence.
Both also exhibit an extensive-in-degree exact deficit at time2d in(13), and the identical optimized profile(11) at every block number.
Their opposite asymptotic behavior refutes the sufficient proposal that long initial free windows plus a uniformly extensive matched-Holder defect establish positive affine growth.
This control does not refute a statement that adds a quantitative nontorsion, all-power-degree or sufficiently-near-one hypothesis.
It identifies information that the selected statistic has discarded.

<a id="torsion-defect-does-not-accumulate"></a>
### 5. The genuine torsion deficit stays bounded at every later scale

The preceding zero-rate argument can be sharpened to an exact order-of-growth comparison with the baseline.
For the base torsion input zeta_6, the six possible power-coordinate vectors are

    (1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1).

Each coordinate of X_N has variance at most N/4.
Center at its actual mean, which need not be integral.
Chebyshev and a union bound show that the box of coordinate half-width sqrt(N) has probability at least1/2.
It has at most(2sqrt(N)+2)^2<=16N integral points for N>=1.
Cauchy--Schwarz on that box yields

    p_N(zeta_6)>=1/(64N).                               (14)

For N=2k, combine(14) with I_k^2<=1/(k+1) and the degree-two instance of(2):

    1/128 <= p_(2k)(zeta_6)/I_k^2 <=1.

After the exact product decomposition(12), for every k>=1 and every r in(10),

    0 <= -log[p_(kd)(alpha_-)/I_k^d] <= r log128.         (15)

On the other hand the mixed-row bound(8),(11) supplies the persistent lower defect

    -log[p_(kd)(alpha_-)/I_k^d]
       >= (2 floor(k/2)/k) r log(1/c),    k>=2.          (16)

Thus a strict defect proportional to d is present at EVERY degree-block scale, while the actual total defect relative to the polynomial baseline stays O(d), uniformly in k.
Applying the same defect estimate again at more scales does not make it fresh information.
A proposed multiplication of those scale bounds would need a new conditional or disjoint-information argument; it is false as an automatic consequence of their simultaneous validity.
Equations(15)--(16) prove this limitation on actual original binary laws, not on a surrogate continuous or finite-quotient model.

### 6. What this round resolves and the next discriminating gate

The positive result is the full finite-time original-law inequality(8), including an exact, finite, coordinate-defined optimization over block matchings and a uniform integer-mixing constant.
It improves the degree-block polynomial baseline whenever the selected actual matrix has mixed rows, and detects every nontorsion unit at each k>=2.
The control is stronger than a single large-degree free-window example: the two actual families have the same complete matching profile, and a zero-growth family retains extensive strictness at all block scales with a bounded total excess over the baseline.

This is a new tested statistic and a precise failure of its proposed accumulation, not a Mahler gap or a theorem about sufficiently small positive Mahler measure.
The proof keeps the nonsymmetric affine dimension equal to two, charges the arithmetic degree in every bound, and uses the original binary law throughout.
The matrices in power coordinates are bookkeeping for actual endpoints; they are not used to invoke a dimension-dependent linear-group theorem.
No limit in k is interchanged with a varying-r limit.

A useful continuation would have to retain an innovation across scales or a lag-sensitive algebraic constraint that the maximum in(7) loses.
For example, investigate whether actual low-information power orbits force a long collection of approximately redundant blocks to obey a quantitative integral recurrence with controlled span and coefficient cost, and whether that conclusion separates the unresolved nontorsion near-one class from the actual torsion controls.
This is a proposed question, not a proved implication.
The retained L92 approximate invariance and L93 rank/time obstruction must both be respected: an O(epsilon n) generic spanning rank, or another defect whose total is O(d), would not supply the missing time-linear income.
Any final growth lower bound must be obtained before replacing it by a Mahler comparison.

### Author verification and review boundary

The author self-check covers the exact original binary Fourier identity, actual power-basis blocks, Haar invariance, all Holder exponents and equality cases, the binomial coefficient normalization, the uniform Fourier coefficient bounds including k=1,2,3, the direction of affinity under marginalization, disjoint-row independence, inverses/transposes, the complete matching cost, and all torsion/positive family degrees and limit orders.
The finite four-bit counts in(13) were written out directly; no program was run.
The argument reuses the actual radical product interface at its verified relative-degree scope and does not re-audit any external source proof.

The complete Sections1--6 and all displayed formulas are frozen for a separately organized noncontributor review as of 2026-10-09T20:48.
This argument asserts no source acquisition or unrestricted G0001 completion.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0111_v1.md#growth-defect-complete-independent-review), with its original inspected scope and relationship.
