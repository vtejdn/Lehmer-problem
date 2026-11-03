---
author: Yin
---

# Complete higher Smith-threshold capacities, compatible labels and paid original norm capture

This retains the complete necessary mathematical argument from [complete original L410](../ledger/Yin_L_G0410_v1.md#higher-smith-depth-reuse).
Original contribution and review accounts remain at their fixed inputs; this maintenance creates no research authority.

## Statement

Let P be monic, irreducible and nontorsion over Z with constant term +1 or -1, alpha a root, d its ORIGINAL degree, m=log M(P)>0, O0=Z[alpha], and A the multiplication matrix on the actual power basis of O0.
Every rational prime p is allowed, including primes dividing the index in the maximal order.
No repeated reduction multiplicity is identified with a field ramification index.
All logarithms are natural unless a base is displayed; phi is the Euler totient and mu in divisor inversion is the Mobius function.

For any integral square B on Lambda=Z_p^d and every integer k>=1 define V_k(B)=red_p{x in Lambda:Bx in p^k Lambda} and h_k(B)=dim_Fp V_k(B).
Zero Smith entries count at every k.
If s_i are the Smith exponents, h_k is their threshold count and equals dim_Fp[p^(k-1)coker(B)/p^k coker(B)].
For nonzero determinant, log_p|ker(B mod p^k)|=sum_i min(k,s_i), which is a different observable.
For EVERY integral square C on the same lattice, without commutation,

    0<=h_k(BC)-h_k(B)<=dim_Fp ker(C mod p).

The upper argument uses only the reduced preimage inclusion; the lower argument is the separate graded-cokernel surjection.

Write Pbar=product_phi phi^(e_phi), f_phi=deg phi, o_phi the prime-to-p order of a root of phi, T0=lcm_phi o_phi, and a0=min{a>=0:p^a>=max_phi e_phi}.
For EVERY finite integer depth cap K>=1, B0=a0+K-1 gives A^(T0 p^B0)=I modulo p^K.
On M=(Z/p^K Z)^d choose E=1 mod T0 and E=0 mod p^B0, set S=A^E and U=A S^(-1), and retain S^T0=I, U^(p^B0)=I and A=SU.
The finite cyclotomic CRT provides compatible free A-stable summands M_o for o|T0, with rank d_o=sum_(o_phi=o)e_phi f_phi and S^o=I there, using the SAME finite bases at all k<=K.
The statement makes no invariant full Z_p block-lift or maximal-order replacement claim.

For each k<=K put g_(k,o)(b)=h_k(A^(o p^b)-I restricted to M_o).
These are nondecreasing in b and eventually equal d_o by b=B0.
Define w_o^(k)=g_(k,o)(0), w_(o p^b)^(k)=g_(k,o)(b)-g_(k,o)(b-1) for b>=1, and zero elsewhere.
For EVERY integer k>=1 there is this unique finite nonnegative INTEGER array, intrinsic by divisor inversion independently of K, E, projector representatives and bases, satisfying

    sum_r w_r^(k)=d, 0<=w_r^(k)<=phi(r),
    h_(p,k)(n):=h_k(A^n-I)=sum_(r|n)w_r^(k)  for ALL n>=1,
    w_r^(k)=sum_(s|r)mu(r/s)h_(p,k)(s).

Choosing K=k gives support only at r=o p^b with b<=a0+k-1; this p-power horizon is not asserted linear in d.
The capacity proof retains g_(k,o)(0)<=sum_(o_phi=o)f_phi<=phi(o) and

    w_(o p^b)^(k)<=sum_(o_phi=o)f_phi min(e_phi,phi(p^b))
                   <=phi(o)phi(p^b),  b>=1.

At k=1 it recovers exactly the original companion law g_(1,o)(b)=sum_(o_phi=o)f_phi min(e_phi,p^b).
For the full original nonzero determinant D_n=det(A^n-I)=Norm_(Q(alpha)/Q)(alpha^n-1), including every powered conjugate with original multiplicity,

    v_p|D_n|=sum_i s_i(n)=sum_(k>=1)h_(p,k)(n)
             >=k sum_(r|n)w_r^(k).

A unimodular basis change inside the SAME order preserves these identities; replacement by the maximal order is not asserted to do so.

The d_o sorted formal activation exponents a_(k,o,j) satisfy a_(k+1,o,j)>=a_(k,o,j), hence their labels o p^a divide the next-depth labels.
This is compatible transport of COUNTING tokens, not a common Smith basis for all n,k or a labeling of individual conjugates.
For every integer K>=1 the REAL normalized array wbar_r^[K]=(1/K)sum_(k=1)^K w_r^(k) has mass d, capacity phi(r), and

    sum_(r|n)wbar_r^[K]=(1/K)sum_i min(K,s_i(n))
                       =(1/K)log_p|ker(A^n-I mod p^K)|,
    v_p|D_n|>=K sum_(r|n)wbar_r^[K].

The unnormalized finite sum has mass Kd and only the K phi(r) bound; the infinite all-depth sum has infinite total mass although each fixed-n divisor sum is finite.
For the COMPLETE mass-d laws at the SAME X, ordered triple lcm density is nonincreasing with depth, and the averaged law has density at most the first-depth law.
This monotonicity supplies no positive short-density premise.

Choose one threshold v=w^(k), q=k, or one average v=wbar^[K], q=K.
For ANY set S of complete positive label weights with W=sum_(r in S)v_r>0 and integer X>=1, define H_X=max_(1<=n<=X)sum_(r in S,r|n)v_r and delta_X=W^(-3)sum_(a,b,c in S,lcm(a,b,c)<=X)v_a v_b v_c.
The triples are ORDERED with replacement; all retained labels above X stay in W and all discarded original mass is paid by any W>=gamma d premise.
For every fixed 0<s<1, C142v2's finite nonnumerical constant K_s gives H_X>=(delta_X/K_s)^(1/s)W^2/X at ONE actual maximizing n<=X, with log|D_n|>=q H_X log p.
If X<=Cd, W>=gamma d, C,gamma>0 and delta_X>0, put eta=q(delta_X/K_s)^(1/s)gamma^2 log p/C.
For 0<h<=exp(-40), put Phi_5(h)=86 sqrt(h)[log(1/h)]^(5/2)/[log log(1/h)]^(3/2).
For eta>0 set H_5(eta)=exp(-40) when eta/2>=Phi_5(exp(-40)); otherwise it is the unique h in(0,exp(-40)) with Phi_5(h)=eta/2.
The actual C147v5 capped inverse yields m>H_5(eta)/C, including the branch outside the small-height domain.
The auxiliary is still t^n-1 with full degree n, content1 and coefficient squared norm2; no selected subnorm, different order, smaller powered degree or different exponent is substituted.
For the nonempty original range U_C(P)=max_(1<=n<=floor(Cd))log|D_n|/d one also has

    delta_X<=K_s[C U_C(P)/(q gamma^2 log p)]^s.

On 0<Cm<=exp(-40), U_C(P)<=Phi_5(Cm).
For FIXED C,gamma,s a hypothetical m->0 therefore forces q^s delta_X->0 uniformly over all primes, thresholds, averages and these selections, using log p>=log2.
Neither such a sequence nor an automatically covered small-measure class is proved.

For EVERY odd integer j>=1 the actual reciprocal irreducible unit P_j=t^2-(2+3^j)t+1 has original degree2, companion [[0,-1],[1,2+3^j]], and A-I with Smith factors1,3^j.
At p=3,n=1, h_(3,k)(1)=w_1^(k)=1 for 1<=k<=j and zero thereafter.
Its all-depth label-one mass j exceeds phi(1) for j>=3; the first K depths give min(K,j), while min(K,j)/K respects the normalized capacity and pays K.
The full original |D_1|=3^j, and the exterior root obeys 3^j+1<alpha<3^j+2, so m>log(3^j+1)->infinity.
This refutes only unpaid depth amalgamation, not a near-one gap or the per-depth theorem.
All seven original sections, twenty-one formulas, complete finite-integral proofs, original contributor declarations, conditional interfaces and countercontrol are retained below.
There is no new numerical run, external source theorem, source-proof audit, arithmetic coverage certificate, Task adoption or research resumption.

## Current assessment
[Selected decision](#decision-complete-current-self-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-22T04:48 |
| status | open |
| reason | Register the exact retained theorem and complete necessary proof; actual whole checking and adoption are separate. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated hypotheses, every original domain, quantifier, sign, cost and limitation. |
| argument | [Complete proof](#argument) | Entire necessary original proof, explicit accepted interfaces and all counterexample, source and expense boundaries. |
| dependency | [Complete first-depth law](Yin_C_G0513_v1.md#nonreduced-layer-definition) | Exact original-order residue multiplicities, prime-to-p orders and primary nilpotent counts; only k=1 is reused, not higher-depth coverage. |
| dependency | [Complete original companion module](Yin_C_G0513_v1.md#nonreduced-layer-capacity-proof) | Cyclic primary gcd/nullity and full original determinant conventions, including index primes; the higher-threshold proof is supplied locally. |
| dependency | [Real totient capacities](Yin_C_G0142_v2.md#general-weak-lcm-final-statement) | Every finite real capacity array and positive ordered triple capture for fixed 0<s<1 and its nonnumerical K_s, at one physical exponent. |
| dependency | [Full cyclic norm expense](Yin_C_G0147_v5.md#statement) | All powered-field multiplicities, monotone Phi5 on its actual domain and strict capped H5 at supplied positive income; no numerical inversion or source-proof upgrade. |
| support | [Earlier aggregate income](Yin_C_G0256_v1.md#aggregate-cyclic-norm-criterion) | Full original norm at one exponent is an antecedent; neither root-subset nor different-time income is pooled. |
| support | [Earlier exact local table](Yin_C_G0256_v1.md#finite-exact-local-cyclic-table) | Nonnegative depth events already reconstruct a full local valuation, without the new per-threshold totient-capacity assertion. |
| support | [Different mixed-resultant Smith layers](Yin_C_G0242_v1.md#collision-layers-and-frobenius-defect) | Comparison only; no semisimple, unramified or splitting hypothesis is transferred into this original companion theorem. |
| support | [Different order-adapted depth capture](../ledger/Yin_L_G0221_v1.md#local-multiplicity-scaled-depth-capture) | Comparison only, with its separate auxiliary, multiplicity versus ramification guard and time cost. |


### Decision complete-current-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T04:54 |
| status | proved |
| reason | Adopt after actual complete whole SELF formed12:53 of the exact current Statement and entire original proof, with both product directions, every prime/depth/index guard, finite integral CRT, normalized full-kernel price, compatible tokens, one-time original norm and complete odd-j countercontrol. No substantive defect or proof repair was found. All original author contributions and prior R561 mathematical/date/input scope remain; missing old context is not reconstructed. Automatic near-one coverage, new computation, source-proof audit and Task/E continuation are not asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Complete stated hypotheses, every original domain, quantifier, sign, cost and limitation. |
| argument | [Exact argument](#argument) | Entire necessary original proof, explicit accepted interfaces and all counterexample, source and expense boundaries. |
| dependency | [Exact dependency](Yin_C_G0513_v1.md#nonreduced-layer-definition) | Exact original-order residue multiplicities, prime-to-p orders and primary nilpotent counts; only k=1 is reused, not higher-depth coverage. |
| dependency | [Exact dependency](Yin_C_G0513_v1.md#nonreduced-layer-capacity-proof) | Cyclic primary gcd/nullity and full original determinant conventions, including index primes; the higher-threshold proof is supplied locally. |
| dependency | [Exact dependency](Yin_C_G0142_v2.md#general-weak-lcm-final-statement) | Every finite real capacity array and positive ordered triple capture for fixed 0<s<1 and its nonnumerical K_s, at one physical exponent. |
| dependency | [Exact dependency](Yin_C_G0147_v5.md#statement) | All powered-field multiplicities, monotone Phi5 on its actual domain and strict capped H5 at supplied positive income; no numerical inversion or source-proof upgrade. |
| support | [Exact support](Yin_C_G0256_v1.md#aggregate-cyclic-norm-criterion) | Full original norm at one exponent is an antecedent; neither root-subset nor different-time income is pooled. |
| support | [Exact support](Yin_C_G0256_v1.md#finite-exact-local-cyclic-table) | Nonnegative depth events already reconstruct a full local valuation, without the new per-threshold totient-capacity assertion. |
| support | [Exact support](Yin_C_G0242_v1.md#collision-layers-and-frobenius-defect) | Comparison only; no semisimple, unramified or splitting hypothesis is transferred into this original companion theorem. |
| support | [Exact support](Yin_C_G0532_v1.md#local-multiplicity-scaled-depth-capture) | Comparison only, with its separate auxiliary, multiplicity versus ramification guard and time cost. |
| review | [Exact review](../audits/reviews/Yin_R_G0729_v1.md#complete-higher-smith-whole-self-finding) | Entire exact current Statement and all seven sections/twenty-one formulas, actual original-order finite integral decomposition, liftable thresholds, intrinsic capacities/compatible labels/paid average, every selected interface, conditional same-time norm and full reciprocal countercontrol; actual current whole is SELF. |

## Complete retained argument

<a id="argument"></a>

The original proofs and input descriptions below retain their dated mathematical scope; they supply no Task/E resumption.

## Higher Smith-depth order capacities with compatible activation labels

Date: 2026-10-18T15:49.
Human author Yin.
Root assigned a bounded S3/S8/S4 question beyond aggregate cyclic income and first-depth nonreduced order layers.
The loglog_cyclic_review agent develops the finite integral decomposition, depth capacities and exact aggregation boundary here.
Root supplied the two separate product-threshold arguments through kernel reduction and cokernel layer surjections; this contribution is used below.
Both are contributors; this fixed exploration supplies conditional depth-sensitive capture, not automatic arithmetic coverage.
No numerical program, factorization run, B3 extension or graph scan is used.

<a id="higher-smith-depth-reuse"></a>
## Reuse and precise changed question

[L74](Yin_C_G0256_v1.md#aggregate-cyclic-norm-criterion) already aggregates full original local incomes at one exponent.
Its [finite exact local table](Yin_C_G0256_v1.md#finite-exact-local-cyclic-table) already reconstructs every local norm valuation by nonnegative events, without an individual-event totient capacity assertion.
[C532](Yin_C_G0532_v1.md#local-multiplicity-scaled-depth-capture) already captures multiplicity-scaled depths using order-adapted auxiliaries at possibly different times.
[L65](Yin_C_G0242_v1.md#collision-layers-and-frobenius-defect) already distinguishes higher Smith layers of a DIFFERENT mixed-resultant operator from its first collision nullity.
The new [L409 first-depth law](Yin_C_G0513_v1.md#nonreduced-layer-definition) gives exact nonnegative phi-capacity labels for the original companion modulo every prime, including repeated reduction.
Those full-norm, depth and first-layer results are not claimed anew.

A bounded G-line search/read of higher Smith depth, liftable kernels, depth/capacity and layer interfaces found no retained proof that EACH higher Smith threshold admits the same capacity, nor the normalized truncated-kernel capacity below.
The proposed object is the SAME original multiplication lattice and SAME cyclic exponent, with fixed Smith threshold k rather than just k=1.
The proof below retains liftability, nilpotent multiplicities, integral prime-to-p projectors and every depth factor.
The combined all-depth event mass is not presumed to satisfy the first-layer capacity.

<a id="smith-threshold-product-lemma"></a>
## 1. The exact threshold and the two product directions

Let Lambda=Z_p^d and let B be an integral d-by-d endomorphism.
For k>=1 put

    V_k(B)=red_p{x in Lambda: Bx in p^k Lambda},
    h_k(B)=dim_Fp V_k(B).

By an integral Smith diagonalization, h_k(B) is exactly the number of Smith exponents at least k; a zero Smith entry is counted at every k.
The SAME diagonalization gives

    h_k(B)=dim_Fp[p^(k-1)coker(B)/p^k coker(B)].        (1)

In contrast, when B has nonzero determinant,

    log_p |ker(B mod p^k)|=sum_i min(k,s_i(B)),

which is generally NOT h_k(B).
Reducing the kernel modulo p, rather than counting its elements, is essential.

For any integral square C on the same lattice one has

    0<=h_k(BC)-h_k(B)<=dim_Fp ker(C mod p).             (2)

For the upper bound, if BCx lies in p^k Lambda then Cx belongs to the set defining V_k(B).
Consequently V_k(BC) is contained in the preimage of V_k(B) under C mod p.
The dimension of that preimage is at most dim V_k(B)+dim ker(C mod p), proving the upper direction.
For the lower bound, image(BC) is contained in image(B), so coker(BC) surjects onto coker(B).
This induces a surjection on the two p^(k-1)/p^k layers in (1), proving the lower direction separately.
No commutation or false equality of the reduced-kernel preimage is assumed.
The proof is finite Smith/module algebra, not an imported Smith-interlacing theorem.

<a id="finite-integral-order-decomposition"></a>
## 2. Order summands on the actual finite integral lattice

Let P be monic, irreducible and nontorsion over Z, with constant term +1 or -1 and original degree d.
Let alpha be a root, let A be multiplication by alpha on the power basis of O0=Z[alpha], and fix any rational prime p.
Write m=log M(P)>0 for its ORIGINAL total logarithmic Mahler measure.
Thus A is in GL_d(Z), including at primes dividing the index of O0 in the maximal order.
Write

    Pbar=product_phi phi^(e_phi),  f_phi=deg phi,
    o_phi=order of a root of phi,
    T0=lcm_phi o_phi,  a0=min{a>=0:p^a>=max_phi e_phi}.

All phi have nonzero constant term and every o_phi is prime to p.
The integers e_phi are polynomial multiplicities, not presumed field ramification indices.
Fix an arbitrary finite depth cap K>=1 and put B0=a0+K-1.
The companion identity and the factorization in characteristic p give

    A^(T0*p^a0)=I mod p,
    A^(T0*p^B0)=I mod p^K.                              (3)

For the second assertion, if a matrix is I+p^s Z with s>=1, its p-th power is I modulo p^(s+1).
The first binomial term has valuation s+1, the intermediate terms have valuation at least 1+2s, and the final term has valuation ps>=s+1.
This proof includes p=2 and s=1; no odd-prime lifting formula is imported.
Iterating K-1 times proves (3).

Work now on M=(Z/p^K Z)^d.
Choose an integer E>=0 with E=1 mod T0 and E=0 mod p^B0, using the ordinary coprime CRT, and set S=A^E and U=A S^(-1) on M.
The conventions T0=1 or B0=0 cause no exception.
Then S and U commute and

    S^T0=I,  U^(p^B0)=I,  A=SU.                         (4)

Modulo p, S is semisimple because t^T0-1 is separable, and S has the same residue eigenvalues as A.
Indeed E is 1 modulo each residue order and a multiple of p^a0, so it preserves each eigenvalue and kills the unipotent part.
This last statement can also be read in each cyclic module F_p[t]/phi^e by expanding (lambda+N)^E over a splitting field; the nilpotent exponent is at most e<=p^a0.

For o dividing T0, the cyclotomic factors Phi_o(t) of t^T0-1 are pairwise coprime over Z/p^K Z.
Here is the finite integral justification.
Their reductions have disjoint roots because p does not divide T0.
A Bezout identity modulo p lifts to an identity with right side 1+p h(t), which is a polynomial unit modulo p^K, with inverse the finite sum of (-p h(t))^j for 0<=j<K.
The polynomial CRT therefore supplies mutually orthogonal idempotents whose sum is 1 modulo t^T0-1.
Evaluation at S yields a direct decomposition into A-stable summands

    M=direct_sum_(o|T0) M_o,
    rank M_o=d_o:=sum_(phi:o_phi=o) e_phi f_phi.          (5)

Each M_o is free over Z/p^K Z.
To see this directly, choose a basis of each idempotent image modulo p and lift its basis vectors into the corresponding image on M.
The combined lifted vectors have determinant a unit and hence form a basis of M.
Applying the idempotents to this basis shows that its vectors in M_o form a basis of that summand.
In that basis A is block diagonal on M.
The ranks in (5) follow from the residue eigenvalues just described, with every original primary multiplicity retained.
The factor Phi_o(S) vanishes on M_o, and hence S^o=I there.

Reduce these SAME summands and bases to each modulus p^k for 1<=k<=K.
This is a compatible finite integral decomposition, not a decomposition in the maximal order or an unproved system of lifted characteristic-zero roots.
For a matrix modulo p^K, the threshold h_k is determined by that reduction whenever k<=K: a vector modulo p with the required lift exists exactly when it has a solution modulo p^k.
Consequently any integral lift of its block matrices computes the same h_k.
The product lemma (2) applies to such lifts and depends only on their products modulo p^k.
No invariant lift of the individual blocks to the full Z_p lattice is required.

<a id="higher-depth-order-capacities"></a>
## 3. Exact phi capacities at every Smith threshold

On M_o define, for 1<=k<=K and b>=0,

    g_(k,o)(b)=h_k(A^(o*p^b)-I restricted to M_o).

Write any n>=1 uniquely as n=p^b u with p not dividing u.
If o does not divide u, then A^n-I is invertible modulo p on M_o and contributes zero at every threshold.
If o divides u, factor

    A^n-I=(A^(o*p^b)-I) Q_(u/o)(A^(o*p^b)),
    Q_v(t)=1+t+...+t^(v-1).

Modulo p the first matrix power A^(o*p^b) is unipotent on M_o, and Q_(u/o)(1)=u/o is nonzero modulo p.
Thus the quotient factor is invertible on M_o, and preserves every threshold count.
It follows that the original full count is

    h_(p,k)(n):=h_k(A^n-I)
               =sum_(o|u) g_(k,o)(b).                  (6)

Each g_(k,o)(b) is nondecreasing in b by (2).
By (4) and S^o=I it equals d_o for b>=B0.
Define the finite nonnegative integer weights

    w_o^(k)=g_(k,o)(0),
    w_(o*p^b)^(k)=g_(k,o)(b)-g_(k,o)(b-1)  (b>=1),
    w_r^(k)=0 for all remaining r.                       (7)

The prime-to-p part of a label identifies o uniquely, so no two different summands are confused in (7).
Telescoping gives sum_r w_r^(k)=sum_o d_o=d.

At b=0, reduction of the lifting condition gives

    g_(k,o)(0)<=g_(1,o)(0)
              =sum_(phi:o_phi=o) f_phi<=phi(o).          (8)

For b>=1 use the exact factor C_b=Phi_(p^b)(A^o) in

    A^(o*p^b)-I=(A^(o*p^(b-1))-I) C_b.

In characteristic p one has Phi_(p^b)(t)=(t-1)^phi(p^b).
On the cyclic primary module F_p[t]/phi^e, the factor phi occurs with multiplicity exactly 1 in t^o-1, since p does not divide o.
Multiplication by (t^o-1)^v therefore has kernel dimension f_phi min(e_phi,v).
For completeness, multiplication by any q on F_p[t]/H has kernel dimension deg gcd(H,q): after writing H=g H1 and q=g q1 with coprime H1,q1, its kernel consists precisely of H1 times the polynomials of degree below deg g.
This is the original companion calculation used in L409, and does not replace a primary multiplicity by a ramification index.
Applying (2) on M_o now gives

    w_(o*p^b)^(k)
      <=nullity(C_b mod p restricted to M_o)
      =sum_(phi:o_phi=o) f_phi min(e_phi,phi(p^b))
      <=phi(o)phi(p^b)=phi(o*p^b).                      (9)

The last inequality counts the distinct roots of all factors of order o among the phi(o) primitive o-th roots; these roots are distinct in characteristic p.
Equations (6)--(9) establish, for EVERY k>=1,

    sum_r w_r^(k)=d,  0<=w_r^(k)<=phi(r),
    h_(p,k)(n)=sum_(r|n) w_r^(k).                       (10)

The arbitrary cap K can be chosen at least k, so this proves all finite thresholds.
Choosing K=k also gives the explicit finite support bound b<=a0+k-1 in every order-o block; that p-power time cost is not claimed to be linear in d.
The weights are intrinsically unique: ordinary divisor inversion of (10) gives

    w_r^(k)=sum_(s|r) mu(r/s) h_(p,k)(s).              (11)

Indeed summing the right side over r dividing n leaves coefficient sum_(a|n/s) mu(a), which is 1 for s=n and 0 otherwise.
Thus choices of K, CRT exponent, idempotent polynomials and block bases do not change the weights.
At k=1, the primary count is g_(1,o)(b)=sum_(phi:o_phi=o) f_phi min(e_phi,p^b), so (7) recovers EXACTLY L409's first-depth law.
The new assertion is its liftable higher-threshold counterpart, not a second proof of first-depth arithmetic coverage.

The determinant and the actual Smith exponents s_i(n) are those of the ORIGINAL integer matrix:

    D_n=det(A^n-I)=Norm_(Q(alpha)/Q)(alpha^n-1),
    v_p|D_n|=sum_i s_i(n)
             =sum_(k>=1) h_(p,k)(n)
             >=k sum_(r|n) w_r^(k).                    (12)

Nontorsion makes D_n nonzero; the sum over k in (12) is finite for each n.
Every original conjugate, including repeated powered values, occurs in this field norm.
Changing the integral basis of the SAME order by a unimodular matrix leaves (10)--(12) unchanged.
Replacing O0 by the maximal order is not an allowed basis change and is not asserted to preserve these higher Smith thresholds.

<a id="compatible-depth-labels"></a>
## 4. Compatible activation labels and the paid truncated-kernel law

For any finite set of adjacent depths, use a common cap K in Section2.
The lifted-kernel inclusions give

    g_(k+1,o)(b)<=g_(k,o)(b) for every b.               (13)

For each k,o, list the d_o activation exponents from (7), with repetition, in nondecreasing order:

    a_(k,o,1)<=...<=a_(k,o,d_o).

Their cumulative counts are g_(k,o)(b), so (13) says

    a_(k+1,o,j)>=a_(k,o,j),
    o*p^a_(k,o,j) divides o*p^a_(k+1,o,j).             (14)

This constructs compatible COUNTING labels on d formal tokens.
It does not construct a common Smith basis for all n,k, or label individual p-adic conjugates by these Smith depths.
The sorted lists are unique from the counts, so the adjacent-depth conclusion is independent of the common finite cap.

For any K>=1 form the finite REAL array

    wbar_r^[K]=(1/K) sum_(k=1)^K w_r^(k).

It satisfies the SAME capacities and total mass as one layer, and its divisor sums are exactly

    sum_r wbar_r^[K]=d,  0<=wbar_r^[K]<=phi(r),
    sum_(r|n) wbar_r^[K]
       =(1/K) sum_i min(K,s_i(n))
       =(1/K) log_p|ker(A^n-I mod p^K)|,
    v_p|D_n|>=K sum_(r|n) wbar_r^[K].                 (15)

Thus division by K gives a uniform phi-capacity representation of the whole truncated kernel length; the matching factor K remains in its actual norm floor.
Without normalization the direct sum of the first K arrays has only the proved capacity K phi(r) and total mass Kd.
The infinite sum of all threshold arrays has infinite total mass d+d+..., although its divisor sum at each fixed n is the finite valuation in (12).
It is not a single finite array of total mass d.

There is an exact monotonicity boundary for arithmetic coverage.
For the complete mass-d laws, draw three independent uniform formal tokens and use their depth-k labels.
By (14) their lcm can only increase as k increases, so their original triple density at any fixed X is nonincreasing in k.
For the averaged law in (15), independently draw a depth uniformly from 1,...,K for each token.
Each resulting label is divisible by its depth-1 label, and hence this averaged law's triple density is also at most the complete first-depth density at the SAME X.
Higher depths do not automatically supply more short compatible triples.
Their possible additional benefit is the explicitly paid factor k or K in (12) or (15), not a manufactured positive-density premise.
For selected labels all removed mass and all retained labels above X must still be accounted for through the selected total W below.

<a id="higher-depth-one-time-budget"></a>
## 5. Conditional capture with every original price retained

Choose either one threshold array w^(k) and q=k, or an averaged array wbar^[K] and q=K.
Denote the chosen array by v_r.
Select any set S of its complete positive label weights, with W=sum_(r in S) v_r>0.
These are complete counting-label weights, not asserted subsets of characteristic-zero roots.
For an integer X>=1 define

    H_X=max_(1<=n<=X) sum_(r in S,r|n) v_r,
    delta_X=W^(-3) sum_(a,b,c in S,lcm(a,b,c)<=X)
                                      v_a v_b v_c.

The three coordinates are ordered and sampled with replacement; labels above X remain in W.
The real phi capacities proved above are precisely the domain of [C142v2](Yin_C_G0142_v2.md#general-weak-lcm-final-statement).
For every fixed 0<s<1, its fixed finite constant K_s therefore gives

    H_X>=(delta_X/K_s)^(1/s) W^2/X.                   (16)

At ONE actual integer n<=X attaining this maximum, (12) or (15) gives

    log|D_n|>=q H_X log p.                            (17)

Assume X<=Cd and W>=gamma d with C,gamma>0.
If delta_X>0, (16)--(17) give actual original norm density at least

    eta=q (delta_X/K_s)^(1/s) gamma^2 log p/C.

Apply [C147v5](Yin_C_G0147_v5.md#statement) to THIS original norm and its actual exponent n, with h=nm/d.
Its exact capped inverse H_5 yields

    m>H_5(eta)/C.                                     (18)

This includes the case h exceeds the small-height domain because that case already exceeds the capped threshold.
The auxiliary remains t^n-1, with full degree n, content 1 and coefficient squared norm 2.
No cost is replaced by a root subset, relative norm, different order, smaller powered degree or collection of different exponents.

For an equivalent necessary budget, define the original

    U_C(P)=max_(1<=n<=floor(Cd)) log|D_n|/d.

The range is nonempty under X>=1 and X<=Cd.
Equations (16)--(17) imply

    delta_X<=K_s [C U_C(P)/(q gamma^2 log p)]^s.        (19)

When 0<Cm<=exp(-40), C147v5 and the monotonicity of Phi_5 give U_C(P)<=Phi_5(Cm).
Thus all q, primes and selected depths remain visible even in the small-measure bound.
For preassigned fixed C,gamma,s, near-zero m would force q^s delta_X to zero uniformly over these choices, using log p>=log 2.
This statement is conditional on such inputs and does not assert their existence.
Conversely, an actual uniform lower bound on q (delta_X/K_s)^(1/s) gamma^2 log p/C would be a genuinely sufficient same-time income certificate.
Nothing here proves that certificate for all small-measure units.
In particular the compatible-label monotonicity in Section4 prevents treating increased depth alone as new automatic arithmetic coverage.

<a id="unnormalized-depth-capacity-countercontrol"></a>
## 6. An original reciprocal countercontrol to unpaid depth aggregation

Let j>=1 be odd and consider the actual reciprocal polynomial

    P_j(t)=t^2-(2+3^j)t+1.

Its discriminant is 3^j(3^j+4), whose 3-adic valuation is the odd number j, so it is not a rational square.
Thus P_j is irreducible over Q, monic and an integer-unit polynomial.
Its exterior positive real root alpha is greater than 1, so it is nontorsion and has original degree 2.
The original companion and its difference are

    A=[[0,-1],[1,2+3^j]],
    A-I=[[-1,-1],[1,1+3^j]].

The latter matrix has an entry equal to 1 and determinant -3^j, so its integer Smith factors are 1 and 3^j.
At p=3 and n=1 this gives

    h_(3,k)(1)=w_1^(k)=1 for 1<=k<=j,
    h_(3,k)(1)=w_1^(k)=0 for k>j,
    sum_(k>=1) w_1^(k)=j>phi(1) when j>=3.            (20)

The first K depths give label-one mass min(K,j), which likewise need not obey phi(1)=1.
Its normalized value min(K,j)/K obeys (15), with the factor K paid in the norm income.
This is an actual reciprocal original-field example of the failure, not an arbitrary Smith matrix or a selected subnorm.
The complete original norm at n=1 has absolute value 3^j.
Modulo 3 the polynomial is (t-1)^2, so its first-depth nilpotent law still agrees with L409.

This family is FAR from a small-measure counterexample.
From alpha+alpha^(-1)=2+3^j and alpha>1 one obtains

    3^j+1<alpha<3^j+2,
    m(P_j)=log alpha>log(3^j+1).                       (21)

The total measure tends to infinity as j grows.
The example refutes only the unpaid amalgamation of all depths into one phi-capacity law, and neither the per-depth theorem nor any near-one gap claim.

<a id="higher-smith-author-check"></a>
## 7. Contribution and exact reuse boundary

Root and loglog_cyclic_review are contributors to the complete argument above.
No numerical program, prime scan, maximal-order computation or new external source was used.

L74 already supplies full original local income aggregation; L221 already handles its distinct order-adapted depth capture.
L409's explicit first-depth law is recovered at k=1, and its arithmetic positive-density problem is not solved here.
The new retained interface is the exact per-threshold capacity and its compatible transport, together with the normalized truncated-kernel capacity and explicit depth price.
Only the conditional capture and inversion in Section5 consume the fixed C142v2 and C147v5 theorems.
Their proofs and inherited source constants are not re-audited or improved here.
The rest is proved above over the original companion lattice.
The broad reuse screen is bounded and no external mathematical novelty is claimed.

The result does not establish an unrestricted Mahler gap or a new automatically covered small-measure class.
