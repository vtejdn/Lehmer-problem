---
author: Yin
---

# Powered-root collision layers, a fixed-valuation counterfamily and conditional finite capture

This retains the complete original 2026-10-07 proof of [L65](../ledger/Yin_L_G0065_v1.md), including the entire exact reciprocal counterfamily and both conditional gap formulations.
The counterfamily is outside the small-Mahler window; the dense-collision conditions remain substantive additional arithmetic assumptions.

## Statement

Let alpha be a nontorsion algebraic unit with monic irreducible polynomial P of degree d>=2 and Delta=abs(discP).
Fix a prime p not dividing Delta, integers a>=1,r>=1 and q=p^r.
Let A be the integral companion, I_a=[Z[alpha]:Z[alpha^a]] when finite, and R_(a,aq)=det S_(a,aq) for the map below.
Whenever powered order indices or Vandermonde certificates are used, require both alpha^a and alpha^(aq) to preserve degree.
Let u_i be the d distinct reduced roots over an algebraic closure of F_p, c_lambda=#{i:u_i^a=lambda}, a_0=a/p^(v_p(a)), and

    nu_(a,p)=sum_lambda c_lambda^2.

The original-lattice mixed Sylvester map S_(a,aq)(B)=A^a B-B A^(aq) has modp nullity

    nu_(a,p)=d+2#{i<j:u_i^a=u_j^a},
    d<=nu_(a,p)<=d min(d,a_0),

independent of r.
In a finite unramified splitting ring, with beta_i=alpha_i^a, define N_s=#{i<j:v(beta_i-beta_j)>=s} and K_s=#{(i,j):v(beta_i-beta_j^q)>=s}.
Then v_p(I_a)=sum_s N_s, v_p(R_(a,aq))=sum_s K_s, K_1=nu_(a,p), and K_s counts precisely the Smith factors divisible by p^s.
In particular

    v_p(R_(a,aq))>=nu_(a,p),
    nu_(a,p)<=d+2v_p(I_a).

The last inequality is an upper bound on first-layer collision mass, without the reversed depth-to-resultant lower bound.
The exact Frobenius-defect comparison and its possible equal-depth cancellation are retained in the proof.

For every integer k>=2, the reciprocal polynomial

    P_k(t)=t^4-7^k t^3+8t^2-7^k t+1

is irreducible, nontorsion and all-positive-power degree preserving, with 7 not dividing its discriminant, I_2=6*7^(2k), nu_(2,7)=8 and v_7(R_(2,14))=8.
The full exact irreducibility, power-stability, index-product and modulo 49 proof is included.
Hence no lower bound tending to infinity with v_p(I_a) holds throughout this reciprocal all-power-stable unit domain at fixed d=4,p=7,a=2.
This family has M(P_k)>47 and is not a small-Mahler counterexample.

Replacing an eligible multilevel edge automatic p^d floor by its measured p^nu floor adds exactly 2m_a m_b(nu-d)log p=4m_a m_b N_1 log p, bounded above by 4m_a m_b v_p(I_a)log p; the separate powered-index factor is retained and never counted twice.
For each eligible two-level choice,

    m(P)>=[nu_(a,p)log p-d log(2d)]/[(2d-1)a(1+p^r)].

For every fixed C>0, if all powered residues coincide and a<=Cd, this gives m(P)>=log p/[4C(1+p^r)] whenever log(2d)<=d log p/2.
More generally fix constants p_0>=2,C>0,0<eta<=1 across the class of inputs admitting p<=p_0, p not dividing Delta, an integer a<=Cd, both alpha^a and alpha^(ap) degree preserving, and nu_(a,p)>=eta d^2.
That entire specified class has a uniform positive Mahler gap: for degrees with log(2d)/d<=eta log 2/2 it is at least eta log 2/[4C(1+p_0)], and bounded degrees are completed by the finite integer-coefficient argument.
Every finite-entropy rational flow all of whose positive irreducible factors lie in this class has only finitely many such factors with multiplicity and captures its entropy in a finite-dimensional invariant subspace and a finite set.
No occurrence/frequency or small-core coverage theorem, unrestricted gap, new flow normalization or uniform surplus-growth law is asserted.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:40 |
| status | open |
| reason | Register the complete original proof and its exact domains in a responsible Claim; actual full current review and any adoption follow separately. Old dated inputs and review accounts remain separate, with no new research, computation or original-source proof audit. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact complete statement](#statement) | Full original exact nullity/layer/Smith identities, complete all-power reciprocal counterfamily and its large-measure boundary, all finite costs, conditional dense-collision gap and rational finite-capture consequences. |
| argument | [Complete retained proof](#argument) | Entire original semisimple proof, local splitting/layers/defects, complete quartic family, index and modular arithmetic, edge accounting, full Vandermonde certificate and bounded-degree completion. |
| dependency | [Complete mixed Sylvester interface](Yin_C_G0237_v1.md#nonbase-index-and-nullity) | Original companion/endomorphism lattice, nonzero mixed resultants and exact semisimple versus repeated-Jordan distinction; no normalized determinant replaces the actual module. |
| dependency | [Powered-order identities](Yin_C_G0231_v1.md#powered-order-index) | Full-original-root Vandermonde/order-index relation at each explicitly degree-preserving selected exponent. |
| dependency | [Exact multilevel edge factorization](Yin_C_G0232_v2.md#prime-power-edge-floor) | Distinct existing order-index and prime-power-ratio resultant factors with actual 2m_a m_b exponent; a measured extra floor changes discarded arithmetic data. |
| dependency | [Complete finite determinant](Yin_C_G0230_v1.md#direct-confluent-vandermonde) | Exact two simple levels, nonzero powered discriminants, full original conjugates and the stated Hadamard exponent cost. |
| dependency | [Rational capture equivalence](Yin_C_G0205_v1.md#capture-equivalence) | Positive irreducible weights with multiplicities in an arbitrary-dimensional finite-entropy rational flow; no arbitrary-abelian or uniform unrestricted Mahler assertion. |
| support | [All-positive-power existence descent](Yin_C_G0231_v1.md#all-positive-power-existence-descent) | Supplies eligible endpoints only for counterexample-existence reductions; no pointwise degree-stability or dense-collision coverage is inferred. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:45 |
| status | proved |
| reason | Adopt the complete collision/layer theorem, full all-k counterfamily and conditional dense-collision gap/capture proof after actual whole current self-review of every formula, exact modular factor, original lattice guard and cost. The large-measure counterfamily and unproved small-core/coverage boundary remain explicit, without a general gap or new computation. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Full original exact nullity/layer/Smith identities, complete all-power reciprocal counterfamily and its large-measure boundary, all finite costs, conditional dense-collision gap and rational finite-capture consequences. |
| argument | [Argument](#argument) | Entire original semisimple proof, local splitting/layers/defects, complete quartic family, index and modular arithmetic, edge accounting, full Vandermonde certificate and bounded-degree completion. |
| dependency | [Dependency](Yin_C_G0237_v1.md#nonbase-index-and-nullity) | Original companion/endomorphism lattice, nonzero mixed resultants and exact semisimple versus repeated-Jordan distinction; no normalized determinant replaces the actual module. |
| dependency | [Dependency](Yin_C_G0231_v1.md#powered-order-index) | Full-original-root Vandermonde/order-index relation at each explicitly degree-preserving selected exponent. |
| dependency | [Dependency](Yin_C_G0232_v2.md#prime-power-edge-floor) | Distinct existing order-index and prime-power-ratio resultant factors with actual 2m_a m_b exponent; a measured extra floor changes discarded arithmetic data. |
| dependency | [Dependency](Yin_C_G0230_v1.md#direct-confluent-vandermonde) | Exact two simple levels, nonzero powered discriminants, full original conjugates and the stated Hadamard exponent cost. |
| dependency | [Dependency](Yin_C_G0205_v1.md#capture-equivalence) | Positive irreducible weights with multiplicities in an arbitrary-dimensional finite-entropy rational flow; no arbitrary-abelian or uniform unrestricted Mahler assertion. |
| support | [Support](Yin_C_G0231_v1.md#all-positive-power-existence-descent) | Supplies eligible endpoints only for counterexample-existence reductions; no pointwise degree-stability or dense-collision coverage is inferred. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0519_v1.md#current-collision-capture-finding) | Entire exact current statement, complete retained proof and every selected interface, self-reviewed; all original dated findings remain at their actual old inputs. |

## Complete retained argument

<a id="argument"></a>

The entire original mathematical argument, local equation numbering, failure controls and remaining boundaries are retained below.
Only heading depth and already established current responsible proof locators change.

<a id="unramified-powered-collision-nullity"></a>
### Domain and exact first-layer nullity

Let alpha be a nontorsion algebraic unit with monic irreducible polynomial P of degree d>=2, conjugates alpha_1,...,alpha_d, and Delta=|disc P|.
Fix a rational prime p not dividing Delta, a>=1 and q=p^r with r>=1.
Require both selected powers alpha^a and alpha^(aq) to preserve degree when using their order indices and the finite Vandermonde certificate.
This is automatic at an all-positive-power endpoint of [L G0059](Yin_C_G0231_v1.md#all-positive-power-existence-descent), not for an arbitrary unreplaced input.

Write A for the integral companion matrix and

    S_(a,aq)(B)=A^a B-B A^(aq),
    R_(a,aq)=det S_(a,aq)
            =product_(i,j)(alpha_i^a-alpha_j^(aq)).

The full-root conventions and nonvanishing are those of L G0063.
In an algebraic closure of F_p let u_1,...,u_d be the distinct reductions of the roots of P.
They are nonzero because P has unit constant coefficient.
For every nonzero lambda put

    c_lambda=#{i:u_i^a=lambda},
    nu_(a,p)=sum_lambda c_lambda^2.

Only finitely many multiplicities are nonzero.
Then

    dim_Fp ker(S_(a,aq) mod p)=nu_(a,p)
       =d+2 #{i<j:u_i^a=u_j^a}.                       (1)

Indeed A is diagonalizable after extending the residue field, and A^a has lambda-eigenspace dimension c_lambda.
Frobenius permutes the multiset of powered roots, preserving its multiplicities, so A^(aq) has the same multiplicities.
The space of intertwiners has dimension sum c_lambda^2.
Extending a field does not change matrix rank.
This also proves that the first-layer nullity is independent of r, although higher valuations need not be.

Put a_0=a/p^(v_p(a)).
On the algebraic closure of the residue field, the p-power map is bijective and a nonzero equation x^(a_0)=lambda has at most a_0 roots.
Thus

    1<=c_lambda<=min(d,a_0)   when c_lambda!=0,
    d<=nu_(a,p)<=d min(d,a_0).                         (2)

In particular p-power factors of a do not enlarge the first-layer fibers.
The hypothesis p not dividing Delta is essential to this semisimple-root argument; no replacement of repeated Jordan blocks by distinct roots is made at ramified primes.

<a id="collision-layers-and-frobenius-defect"></a>
### Pair-collision depth and Frobenius defect are different data

Work in a finite unramified splitting extension of Q_p, with valuation v(p)=1, and put beta_i=alpha_i^a.
This setup follows by splitting the squarefree reduction in a finite residue extension and lifting its simple roots.
The simple-root lifting step is elementary: if P(x)=0 modulo p^s and P'(x) is a unit, choosing x+p^s h fixes the next digit by the unique linear equation for h.
The resulting roots have distinct reductions, so v(alpha_i-alpha_j)=0 for i!=j.

Let

    N_s=#{i<j:v(beta_i-beta_j)>=s},
    K_s=#{(i,j):v(beta_i-beta_j^q)>=s}       (s>=1).

Degree preservation and the mixed-exponent nonvanishing make all valuations in these definitions finite, apart from no diagonal terms being present in N_s.
The divided-difference formula gives

    v_p(I_a)=sum_(i<j) v(beta_i-beta_j)=sum_(s>=1) N_s,
    v_p(R_(a,aq))=sum_(s>=1) K_s,
    K_1=nu_(a,p)=d+2N_1.                              (3)

The values of v are nonnegative integers.
In particular

    v_p(R_(a,aq))>=nu_(a,p),
    nu_(a,p)<=d+2v_p(I_a).                            (4)

The second inequality goes in the opposite direction to a claimed resultant lower bound d+2v_p(I_a).
It says that first-layer collision data are a truncated part of the order-index depth, not all of it.

These layer counts also have a precise Smith interpretation.
The Vandermonde change of basis diagonalizing A is invertible over the unramified valuation ring, since its determinant is a product of unit root differences.
On the matrix endomorphism lattice it diagonalizes S_(a,aq) with entries beta_i-beta_j^q.
Hence K_s is the number of its p-primary Smith factors divisible by p^s.
Unramified scalar extension does not change these exponents: an integral Smith diagonal remains a Smith diagonal over the extended DVR.
Thus K_1 is only the first layer of the actual finite module.

There is a useful direct explanation of the possible truncation.
Let phi be the residue Frobenius lift on the unramified splitting field.
It permutes the original roots; write phi^r(beta_j)=beta_(sigma j) and define

    e_j=v(beta_j^q-beta_(sigma j))>=1.

These defects are finite.
If equality held before taking v, a finite iterate of phi would make beta_j a root of unity.
For any i, put k_ij=v(beta_i-beta_(sigma j)), allowing k_(sigma j,j)=infinity.
The nonarchimedean triangle inequality gives

    v(beta_i-beta_j^q)>=min(k_ij,e_j),                (5)

with equality whenever k_ij!=e_j.
Thus a deep pair collision k_ij>e_j contributes only e_j at that cross factor.
Cancellation when the depths are equal, or a larger defect e_j, is genuinely additional information.
No lower estimate proportional to all collision depth follows from (1) alone.

<a id="fixed-resultant-growing-index-family"></a>
### A reciprocal all-power-stable family with fixed resultant valuation

For every integer k>=2 set s=7^k and

    P_k(t)=t^4-s t^3+8t^2-s t+1.                       (6)

This is an irreducible reciprocal unit polynomial with a unique positive root of largest modulus, and every positive power of each root preserves degree.
To verify all these assertions, write

    P_k(t)=t^2 H_k(t+t^(-1)),
    H_k(x)=x^2-sx+6.

The discriminant s^2-24 lies strictly between (s-1)^2 and s^2, so H_k is irreducible.
Its two roots satisfy

    z_+ in (s-1,s),       z_- in (0,1).

In the real quadratic field Q(z_+), the element z_+^2-4 becomes negative under the other real embedding, and therefore is not a square.
The quadratic equation t^2-z_+t+1 then has degree two over that field, proving irreducibility of P_k.
Its roots consist of a positive reciprocal pair lambda,lambda^(-1), lambda>1, and a conjugate pair on the unit circle.
In particular lambda is the unique root of largest modulus.
If two conjugates had equal n-th powers, a Galois automorphism taking one of them to lambda would give a different conjugate of modulus lambda, impossible.
This proves all-positive-power degree preservation.

For a=2 the order index is exactly

    I_2=6s^2=6*7^(2k),       v_7(I_2)=2k.              (7)

Here is a direct product calculation.
Label the roots lambda,lambda^(-1),mu,mu^(-1) with trace sums z_+,z_-.
The product of the two within-pair sums is z_+z_-=6.
The four cross sums have product s^2, because

    (lambda+mu)(lambda+mu^(-1))=lambda(z_++z_-)=lambda s

and the analogous product with lambda^(-1) is lambda^(-1)s.
Their product is b_2=product_(i<j)(alpha_i+alpha_j)=6s^2, which proves (7) without a numerical root calculation.

Modulo 7, P_k=t^4+t^2+1 has the four distinct roots +/-2,+/-3.
Thus 7 does not divide disc P_k and all four roots lift to Q_7.
For every k>=2, modulo 49 we have the exact factorization

    P_k(t)=(t^2-4)(t^2-37) modulo 49.                 (8)

The powered roots beta_i=alpha_i^2 therefore form two groups of size two: beta=4 modulo 49 and beta=37 modulo 49.
The two groups have distinct residues 4 and 2 modulo 7.
Direct integer arithmetic gives

    4^7=18 modulo 49,       37^7=30 modulo 49.

Within the first matched group every beta_i-beta_j^7 is -14 modulo 49, and within the second it is 7 modulo 49.
All eight of these factors have valuation exactly one.
The eight remaining cross-group factors are units.
Consequently

    nu_(2,7)=8,
    v_7(R_(2,14))=8             for every k>=2.        (9)

For k=2 already, 8<d+2v_7(I_2)=12.
More strongly, with d=4, p=7 and a=2 fixed, the resultant valuation stays constant while v_7(I_2) tends to infinity.
Therefore no lower bound with a positive linear coefficient on v_p(I_a), or any function of that depth tending to infinity, holds throughout this reciprocal all-power-stable unit domain.

This is a large-measure control.
In fact lambda>z_+-1>s-2>=47.
It is not an example in the small-Mahler core, and it does not refute an estimate restricted by M(P)<the plastic number.
Nor does it rule out a lower bound involving genuinely new Frobenius defect or higher lifting data in addition to the order index.

<a id="measured-nullity-cost-and-certificate"></a>
### Actual gain accounting and a conditional finite certificate

In the multilevel determinant of [L G0060](Yin_C_G0232_v2.md#prime-power-edge-floor), an eligible edge a->b=ap^r with multiplicities m_a,m_b contains the factor |R_(a,b)|^(2m_a m_b).
Replacing its automatic p^d floor by the measured first-layer p^nu floor contributes the additional guaranteed logarithmic amount

    2m_a m_b(nu_(a,p)-d)log p
       =4m_a m_b N_1 log p
       <=4m_a m_b v_p(I_a)log p.                     (10)

This accounting is for that actual resultant factor.
The same determinant also contains its separate order-index factor I_a^(2m_a^2); neither factor is to be deleted or counted twice.
Equation (10) does not prove a resultant lower bound in terms of the full index depth.
It bounds the size of the first-layer gain one has actually justified.
In particular at a=1 it is zero, and at other levels it requires a prime dividing the powered order.

The measured nullity can nevertheless support a genuine conditional certificate.
For the two simple node levels a and b=ap^r, use the 2d by 2d Vandermonde matrix V.
Its determinant identity and Hadamard's inequality give

    |det V|^2=|disc P_a| |disc P_b| |R_(a,b)|^2,
    p^(2nu_(a,p))<=|det V|^2
       <=(2d)^(2d) M(P)^(2(2d-1)(a+b)).

Both powered discriminants are nonzero integers, so using their lower bound one is legitimate.
Therefore

    m(P)>=[nu_(a,p)log p-d log(2d)]
                 /[(2d-1)a(1+p^r)].                 (11)

No new flow entropy or degree normalization is introduced in this inequality.
For example, fix p,r and a constant C>0.
On the class of eligible inputs for which all d reduced roots have the same a-th power and a<=Cd, we have nu=d^2.
Whenever log(2d)<=d log p/2, equation (11) gives the explicit bound

    m(P)>=log p/[4C(1+p^r)].                          (12)

The large-collision condition here is substantive arithmetic information.
It is not automatic for an all-power endpoint or for a small-Mahler polynomial.
No occurrence, frequency, or coverage theorem for this condition has been proved here.
Consequently the parameter-only decay theorem of L G0060 cannot simply be quoted with d replaced by measured nullities; its discarded arithmetic data have now changed.
Conversely, (11) does not establish a general gap without control of the nullity relative to its exponent cost.
The counterfamily (6) shows why full order-index depth alone is not such control.

<a id="bounded-prime-dense-collision-class"></a>
### A precise restricted gap and finite-capture consequence

Fix constants p_0>=2, C>0 and 0<eta<=1.
Consider the class of nontorsion algebraic units P for which there exist a rational prime p<=p_0 not dividing disc P and an integer a<=Cd such that both alpha^a and alpha^(ap) preserve degree and

    nu_(a,p)>=eta d^2.                                (13)

These constants are fixed across the class.
For every d satisfying log(2d)/d<=eta log2/2, equation (11), now with r=1, yields

    m(P)>=eta log2/[4C(1+p_0)].                        (14)

Indeed its numerator is at least eta d^2 log2/2, and its denominator is at most 2Cd^2(1+p_0).
The remaining degrees are bounded.
Among their monic integer polynomials with M(P)<=2, the coefficient bound gives a finite set; every nontorsion irreducible member has positive m.
Combining its positive minimum with log2 and (14) proves a uniform positive gap on this specified class.
This finite-degree completion asserts existence of a constant, not a computed sharp minimum.

By the rational-flow criterion of [L G0002](Yin_C_G0205_v1.md#capture-equivalence), a finite-entropy rational flow whose positive irreducible factors all belong to this class has only finitely many such factors, counted with multiplicity, and captures its entropy in a finite-dimensional invariant subspace, and hence in a finite set.
This is a restricted consequence at the fixed constants p_0,C,eta.
No assertion that the full small-Mahler core satisfies (13), or that these constants can be chosen to cover it, is made.
Such a coverage theorem would be an additional arithmetic input; the existence descent to all-power endpoints supplies eligibility of exponents but not dense modular collisions.
