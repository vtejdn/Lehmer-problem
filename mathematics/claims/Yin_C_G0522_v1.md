---
author: Yin
---

# Original binary affine growth: complete integer-mixing matching bound and nonaccumulation controls

The complete necessary original D82 proof is retained from [L215](../ledger/Yin_L_G0215_v1.md#complete-retained-proof-and-review), including every failed-accumulation control, exact measure cost and fixed-degree limit.
The [original R111 whole](../audits/reviews/Yin_R_G0111_v1.md#growth-defect-complete-independent-review) keeps its frozen L215 input, 2026-10-09T20:51 date and complete no-defect verdict.
Its stated noncontribution, broad research question and rotation/J permission do not establish the actual additional mathematical content and its order before the first target inspection; that original whole relationship remains UNKNOWN pending a fresh whole review.
This is not an assertion that mathematical sharing occurred, and fixed proof inputs or upstream author roles alone do not make a target review SELF.
The original R111 sign/binary convention derivation is included explicitly below as an already retained argument.
The complete [original author checking](../audits/reviews/Yin_R_G0730_v1.md#original-affine-matching-author-whole-self-finding) remains separately SELF at its actual original input.

## Statement

For EVERY algebraic unit alpha, including roots of unity, let d=[Q(alpha):Q], and let A in GL_d(Z) be multiplication by alpha in the actual power basis 1,alpha,...,alpha^(d-1).
For independent fair bits xi_j, put X_n=sum_(j=0)^(n-1)xi_j alpha^j, p_n=sum_x Pr(X_n=x)^2, and H_2(n)=-log p_n.
These are the original nonsymmetric affine endpoint fibers, with word probabilities2^(-n) and fixed affine matrix dimension2.
At each fixed n, using signs2xi_j-1 instead gives2X_n minus the fixed sum of the powers: endpoint fibers, collision probabilities, support sizes and entropies are identical, and the common linear part remains alpha^n.
No symmetric-generator growth comparison is used.

On normalized Haar T^d put f(t)=product_j cos^2(pi t_j), U=(A^d)^transpose, I_k=binom(2k,k)/4^k and Z_k=I_k^d.
For EVERY integer k>=1,
p_(kd)=integral product_(b=0)^(k-1)f(U^b t)dt <= I_k^d <= (k+1)^(-d/2).
For arbitrary n>=d the same upper bound holds with k=floor(n/d).
For k>=2 equality in the FIRST Holder inequality occurs exactly when U is a signed permutation matrix.
Every nontorsion input has strict inequality at all k>=2; some torsion inputs also do.
The baseline equality is attained in unbounded actual degree d a power of two by alpha primitive of order2d, minimal polynomial t^d+1, with A^d=-I and p_(kd)=I_k^d.
These torsion controls have collision-free words through time d and zero asymptotic growth.

For V in GL_d(Z), let r(V) be the maximum number of rows, each having at least two nonzero entries, with pairwise disjoint nonzero column supports; put R(V)=max(r(V),r(V^(-1))).
Then R(V)=0 exactly for signed permutations, and otherwise1<=R(V)<=floor(d/2).
This is a statistic of the specified coordinates, not an arbitrary integral-basis invariant.
Set c=sqrt(1015)/32<1.
For EVERY integer k>=1, the product probability density nu_k=f^k/Z_k satisfies Aff(nu_k,nu_k composed with V)<=c^R(V).
The complete proof retains the uniform coefficient1/4<=a_k(floor(sqrt(k)))<=3/4, the total-variation separation3/32, marginalization direction, disjoint-support independence and inverse symmetry.

For EVERY k>=2, let M range over matchings on0,...,k-1, with disjoint unordered pairs and possible singletons, and put
B_k(U)=(2/k) max_M sum_({a,b} in M)R(U^(b-a)).
Then0<=B_k(U)<=floor(d/2), and
p_(kd)<=I_k^d c^B_k(U), H_2(kd)>=-d log I_k+B_k(U)log(1/c),
B_k(U)>=(2floor(k/2)/k)R(U).
For a nontorsion alpha, U^h is never a signed permutation at a nonzero integer lag, and B_k(U)>=2floor(k/2)/k.
The matching proof bounds ONE common integral using pair exponent k/2 and singleton exponent k; it assumes neither pair independence nor independent defects across scales.
Its certified entropy correction is at most(d/2)log(1/c), independent of k, so division by kd gives no positive rate from this correction.

For EVERY r=2^j with integer j>=0, d=2r, compare alpha_- primitive of order6r, P_-(t)=t^(2r)-t^r+1, and alpha_+=phi^(1/r), P_+(t)=t^(2r)-t^r-1, phi=(1+sqrt5)/2.
Both polynomials are irreducible of actual degree2r, with actual relative degree r over Q(zeta_6) or Q(phi).
In the permuted power basis each U is the direct sum of r copies of (B_delta^2)^transpose, where B_delta=[[0,delta],[1,1]], delta=-1 or1, and B_delta^2=[[delta,delta],[1,delta+1]].
Both have R(U)=r and the IDENTICAL COMPLETE optimized profile
B_k(U_-)=B_k(U_+)=(2floor(k/2)/k)r for ALL k>=2.
Individual lag statistics need not agree: U_-^3=I, while no nonzero power of U_+ is a signed permutation.

For ALL integers N>=0, p_(Nr)(alpha_-)=p_N(zeta_6)^r and p_(Nr)(alpha_+)=p_N(phi)^r.
More generally, for n=qr+s,0<=s<r, each probability equals the corresponding base p_(q+1)^s p_q^(r-s).
The genuine relative-degree requirement is retained, and no factor1/r is lost from the FIXED-r limiting rate.
The exact hand calculations p_4(zeta_6)=1/8 and p_4(phi)=3/32 yield p_(2d)(alpha_-)/I_2^d=(8/9)^r and p_(2d)(alpha_+)/I_2^d=(2/3)^r.
No program run or new finite computational certificate is asserted.
For every fixed r, the torsion support is at most(n+1)^(6r), so its support, Shannon and collision entropy rates are all0.
For the positive family, p_n(phi)<=2^(-ceil(n/2)) and the exact incomplete-residue product gives liminf H_2(n;alpha_+)/n >=(log2)/2, and hence the same lower bound for Shannon entropy and logarithmic support.
Both families have exactly2^n distinct fixed-time affine words and endpoint values for every n<=d.
The positive family's multiplicative Mahler measure is phi and its logarithmic measure is log phi; it is a fixed non-small, nonreciprocal control, not a near-one reciprocal counterexample or a premise used to prove its growth lower bound.
No fixed-r limit is interchanged with a varying-r limit.

For EVERY integer N>=1 the actual torsion base satisfies p_N(zeta_6)>=1/(64N).
For ALL k>=1,1/128<=p_(2k)(zeta_6)/I_k^2<=1, and hence
0<=-log[p_(kd)(alpha_-)/I_k^d]<=r log128 uniformly in k and every r=2^j.
For k>=2 the SAME actual total defect is at least(2floor(k/2)/k)r log(1/c).
Thus an extensive strict defect exists at EVERY degree-block scale while the true total excess stays O(d), uniformly in block number.
The optimized profile, long initial free window and simultaneous strictness therefore do not by themselves imply positive asymptotic affine growth or allow multiplication of scale defects.
Conditional innovation, quantitative near-one/nontorsion/all-power-degree hypotheses and the proposed lag-sensitive recurrence remain unproved here.
All source, contribution and nonexecution boundaries and all original unsuccessful-proposal scopes are retained.
No external source theorem, new U/PDF, native program, unrestricted Mahler gap or Task/E resumption is supplied.

## Current assessment
[Selected decision](#decision-complete-current-whole-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-22T04:50 |
| status | open |
| reason | Register the complete fixed original argument and all quantified costs, controls, failures and contribution boundaries. Actual current whole SELF and any adoption follow separately; no old inspection, source depth, native run or research Task/E is rewritten. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire statement](#statement) | ENTIRE original D82 reuse/Sections1--6/equations1--16 plus the original R111 fixed-n sign/binary encoding argument: EVERY actual algebraic unit including torsion/original fair independent bits and nonsymmetric dimension2, full d-block Fourier/Holder baseline/equality/incomplete blocks, uniform integer-mixing affinity and exact finite matching with all costs, actual dyadic relative degrees/norm-minus1 irreducibility and identical optimized profiles with distinct lag data, all hand counts and fixed-r opposite growth rates/full incomplete-class product, genuine all-scale torsion upper and lower total defect, failed automatic accumulation and proposed innovation gate only, original contribution/source/native/Task boundaries. |
| argument | [Entire argument](#argument) | ENTIRE original D82 reuse/Sections1--6/equations1--16 plus the original R111 fixed-n sign/binary encoding argument: EVERY actual algebraic unit including torsion/original fair independent bits and nonsymmetric dimension2, full d-block Fourier/Holder baseline/equality/incomplete blocks, uniform integer-mixing affinity and exact finite matching with all costs, actual dyadic relative degrees/norm-minus1 irreducibility and identical optimized profiles with distinct lag data, all hand counts and fixed-r opposite growth rates/full incomplete-class product, genuine all-scale torsion upper and lower total defect, failed automatic accumulation and proposed innovation gate only, original contribution/source/native/Task boundaries. |
| dependency | [Exact dependency](Yin_C_G0212_v1.md#radical-collision-control) | Only the actual irreducible radical relative-degree/product collision law and norm-minus1 dyadic degree mechanism; no invalid arbitrary-polynomial rate dilution or near-one claim. |
| support | [Exact support](Yin_C_G0283_v1.md#decreasing-binary-entropy-increments) | Only the retained original-binary entropy increments/approximate-invariance boundary; no automatic time-linear income. |
| support | [Exact support](Yin_C_G0286_v1.md#power-orbit-inverse-time-cost) | Only the genuine exponential inverse-concentration/rank-time limitation on the proposed continuation. |
| support | [Exact support](Yin_C_G0289_v1.md#group-growth-mahler-cost) | Only fixed affine dimension2, nonsymmetric word-growth normalization and Mahler-comparison scope; not a symmetric-generator growth theorem. |
| support | [Exact support](Yin_C_G0272_v1.md#prime-order-small-binary-quotients) | Only the finite-field perfect-uniformity obstruction and its original binary-law bounds. |


### Decision complete-current-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T04:55 |
| status | proved |
| reason | Adopt after actual complete reading and mathematical reconstruction of the published entire Statement and entire Argument, including all original quantified mechanisms, costs, finite controls, failed proposals, convention and contribution/source/remaining-scope boundaries. The current whole and complete original author checking are separately SELF; the old complete separately arranged whole remains UNKNOWN at its actual original frozen input. No new isolated review, original proof repair, source audit, computation, research Task/E or broader theorem is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | ENTIRE original D82 reuse/Sections1--6/equations1--16 plus the original R111 fixed-n sign/binary encoding argument: EVERY actual algebraic unit including torsion/original fair independent bits and nonsymmetric dimension2, full d-block Fourier/Holder baseline/equality/incomplete blocks, uniform integer-mixing affinity and exact finite matching with all costs, actual dyadic relative degrees/norm-minus1 irreducibility and identical optimized profiles with distinct lag data, all hand counts and fixed-r opposite growth rates/full incomplete-class product, genuine all-scale torsion upper and lower total defect, failed automatic accumulation and proposed innovation gate only, original contribution/source/native/Task boundaries. |
| argument | [Exact retained argument](#argument) | ENTIRE original D82 reuse/Sections1--6/equations1--16 plus the original R111 fixed-n sign/binary encoding argument: EVERY actual algebraic unit including torsion/original fair independent bits and nonsymmetric dimension2, full d-block Fourier/Holder baseline/equality/incomplete blocks, uniform integer-mixing affinity and exact finite matching with all costs, actual dyadic relative degrees/norm-minus1 irreducibility and identical optimized profiles with distinct lag data, all hand counts and fixed-r opposite growth rates/full incomplete-class product, genuine all-scale torsion upper and lower total defect, failed automatic accumulation and proposed innovation gate only, original contribution/source/native/Task boundaries. |
| dependency | [Exact retained dependency](Yin_C_G0212_v1.md#radical-collision-control) | Only the actual irreducible radical relative-degree/product collision law and norm-minus1 dyadic degree mechanism; no invalid arbitrary-polynomial rate dilution or near-one claim. |
| support | [Exact retained support](Yin_C_G0283_v1.md#decreasing-binary-entropy-increments) | Only the retained original-binary entropy increments/approximate-invariance boundary; no automatic time-linear income. |
| support | [Exact retained support](Yin_C_G0286_v1.md#power-orbit-inverse-time-cost) | Only the genuine exponential inverse-concentration/rank-time limitation on the proposed continuation. |
| support | [Exact retained support](Yin_C_G0289_v1.md#group-growth-mahler-cost) | Only fixed affine dimension2, nonsymmetric word-growth normalization and Mahler-comparison scope; not a symmetric-generator growth theorem. |
| support | [Exact retained support](Yin_C_G0272_v1.md#prime-order-small-binary-quotients) | Only the finite-field perfect-uniformity obstruction and its original binary-law bounds. |
| review | [Actual complete current whole SELF](../audits/reviews/Yin_R_G0730_v1.md#current-affine-matching-whole-self-finding) | ENTIRE original D82 reuse/Sections1--6/equations1--16 plus the original R111 fixed-n sign/binary encoding argument: EVERY actual algebraic unit including torsion/original fair independent bits and nonsymmetric dimension2, full d-block Fourier/Holder baseline/equality/incomplete blocks, uniform integer-mixing affinity and exact finite matching with all costs, actual dyadic relative degrees/norm-minus1 irreducibility and identical optimized profiles with distinct lag data, all hand counts and fixed-r opposite growth rates/full incomplete-class product, genuine all-scale torsion upper and lower total defect, failed automatic accumulation and proposed innovation gate only, original contribution/source/native/Task boundaries. Current constructor whole SELF only; no original UNKNOWN arrangement is retrospectively established. |

## Complete retained argument

<a id="argument"></a>
<a id="complete-retained-proof-and-review"></a>
<a id="growth-defect-fixed-scope"></a>

### Reuse and changed mechanism

The author read [S2](../strategies/Yin_S_G0002.md), the original-binary increment and approximate-invariance argument [L92](Yin_C_G0283_v1.md#decreasing-binary-entropy-increments), the exponential inverse-concentration limitation [L93](Yin_C_G0286_v1.md#power-orbit-inverse-time-cost), and the actual group-growth normalization [L96](Yin_C_G0289_v1.md#group-growth-mahler-cost).
The finite-field perfect-uniformity obstruction in [L81](Yin_C_G0272_v1.md#prime-order-small-binary-quotients) and the full-tail/free-window warnings of S2 remain in force.
None of those statements turns a finite-block entropy value into a lower asymptotic rate.

The present discriminator uses the exact torus integral for the original binary collision probability.
It quantifies the defect in the degree-block Holder inequality by the mixing of integral coordinates, with no stationary law, changed digits, assumed Mahler lower bound, or growing matrix representation of the affine semigroup.
The auxiliary torus densities used to measure this defect are normalized Fourier integrands, not stationary laws on the actual return core.
The power-coordinate dimension d records arithmetic degree; the two affine generators still act in GL_2(C).

The local G-ledger search for block Holder defects, integer-coordinate mixing and multiscale collision controls found the related mechanisms above, but not the specific inequality proved here.
This bounded reuse screen is not a novelty claim.
The radical product law used for the explicit controls is already fixed in [C212 radical-product proof](Yin_C_G0212_v1.md#radical-collision-control), with its actual relative-degree requirement.
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

The following fixed-time convention argument is retained from the original R111 full review, rather than inferred from a symmetric random walk.
The binary digit convention agrees with the Task's two affine generators: at each fixed n, the endpoint with signs 2 xi_j-1 equals 2 X_n minus the fixed sum of the powers.
Thus endpoint fibers, collision probabilities, support cardinalities and entropies are unchanged, and the common linear part remains alpha^n.
No symmetric-generator growth comparison is imported.

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
