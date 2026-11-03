---
author: Yin
---

# Complete powered-order and resultant structure with all-power norm descent

This retains the complete original 2026-10-07 mathematics of [L59](../ledger/Yin_L_G0059_v1.md).
The full-root conventions, exact cyclic valuation overlap, explicit degree8 unit control and complete norm-product descent are retained together with their separate original contribution roles.
The adequate existing J9 home owns the native calculations; no program or new research computation is run here.

## Statement

Let alpha be any nonzero nontorsion algebraic integer of positive degree d, with monic minimal polynomial P, original conjugates alpha_i, and e_n=[Q(alpha):Q(alpha^n)] for integersn>=1.
A. The full original d-root polynomial and power-coordinate determinant satisfy

    P^[n]=product_i(t-alpha_i^n)=P_(alpha^n)^(e_n),
    b_n=detC_n=product_(i<j)(alpha_j^n-alpha_i^n)/(alpha_j-alpha_i) inZ,
    b_n!=0 iff e_n=1.

When e_n=1, |b_n| is the exact index [Z[alpha]:Z[alpha^n]] and abs(discP^[n])=abs(discP)b_n^2.
With deg(alpha^(ab))=d the complete signed and absolute cocycles in formula4 hold, using I_b(alpha^a), without replacing it by I_b(alpha).
For every primeell, ell divides b_ell iff ell divides discP, including the zero-determinant case.
At an unramifiedell, ell dividesb_n iff two distinct reduced roots have equal n-th powers; the unit case gives the precise finite-field root-ratio condition.

B. For distinct positive integersa,b, the full-original-root resultant

    R_(a,b)=product_(i,j)(alpha_i^a-alpha_j^b)

is a nonzero integer without any powered-degree hypothesis.
It divides R_(ca,cb) for every positive integerc; exact minimal-polynomial composition has exponent e_c^2, and polynomial substitution has the distinct gcd-corrected absolute identity9 and its stated sign convention.
A prime-power ratio b/a=ell^r supplies exactly the proven single ell^d Frobenius floor, even through intermediate degree drops.
For a unit, c_(|a-b|) dividesR_(a,b), where c_n=Res(P,t^n-1); the additional norm factor for nonunits is retained.
For a monic irreducible reciprocal noncyclotomic unitP with constant1 and d=2r, simultaneous disjoint diagonal/inverse factors give

    R_(a,b)=c_(|a-b|)c_(a+b)Z_(a,b), Z_(a,b) in Z\{0}.

Writing P=t^r T(t+t^(-1)) and U_j as the stated integral recurrence, F_n=Res(T,U_(n-1)) dividesb_n and

    c_(2n)=c_2 F_n^2,
    I_n^2>=abs(c_(2n)/c_2) when degree is preserved.

For all eligible selected distinct primes in the complete C230 finite determinant, the exact Q_arith obeys formula14, with t_p=abs(c_(p-1)c_(p+1))/gcd(abs(c_(p-1)c_(p+1)),p^d).
No overlapping prime valuation is counted twice.
On the accepted original Lehmer control the retained J9 data give Q_arith(k)=9 for every integerk>=1 at selected primes2,3; its cyclic lower product is exactly9, with c_1=c_2=c_3=c_5=c_6=-1,c_4=-9 and normalized t_2=t_3=1.
This is one fixed control, not a uniform surplus-growth claim.

C. The explicit reciprocal integral unit alpha=beta exp(pi i/6), with beta+beta^(-1)=4+sqrt3 and beta>1 in the indicated embedding, has degree8 and complete minimal polynomial

    [t^4-3t^3+20t^2-3t+1]^2-48t^2(t-1)^4.

Its power degree is8 iff6 does not dividen, and4 iff6 dividesn.
Thus every prime and prime-power exponent can preserve degree while a composite exponent fails.
Its actual measure is (beta_+ beta_-)^2>16, so it supplies no near-one counterexample.

D. For any degree-lowering positive exponentn, let K=Q(alpha),L=Q(alpha^n),e=[K:L]>1,gamma=Norm_(K/L)(alpha),f=[L:Q(gamma)].
Then gamma is nonzero integral nontorsion, remains a unit whenalpha is, and

    gamma^n=(alpha^n)^e,
    gamma/alpha^e is an n-th root of unity,
    deg(gamma)=d/(ef)<d,
    M(alpha)=M(gamma)^f, 0<m(gamma)=m(alpha)/f<=m(alpha).

The complete direct embedding-product proof supplies these measure identities without an extra height theorem.
Repeated actual degree drops terminate at an endpoint preserving degree under every positive integer power.
This preserves the infimum of positive logarithmic measures, also within units, and permits termwise reduction of hypothetical vanishing sequences and summable distinct-primary counterexample-existence constructions.
The unit endpoint is reciprocal in the explicit original window1<M(alpha)<theta_0,theta_0^3-theta_0-1=0, by the accepted nonreciprocal gap; norm replacements themselves need not preserve reciprocity.
No finite algorithm deciding universal power stability, preservation of the original flow or its entropy/discriminant, existence of a counterexample, uniform arithmetic growth or unrestricted entropy gap is asserted.

## Current assessment
[Selected decision](#decision-complete-retained-proof-adoption)

## Assessment history

### Decision retained-registration

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:02 |
| status | open |
| reason | Register the complete retained order/resultant/cyclic structure, exact control and full all-power norm descent; actual current complete inspection and adoption follow separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact complete statement](#statement) | All original-root multiplicities, index/local scalar domains, exact signed/composition/cyclic identities, eligible-prime floor, degree8 control and existence-only norm descent with every unit/sequence/flow boundary. |
| argument | [Complete original proof](#argument) | Entire original sections and formulas1--19, including complete field/conjugate-quartic control, direct norm-product proof, cyclic gcd overlap and exact retained finite control; no proof summary replaces any step. |
| dependency | [Complete finite arithmetic surplus](Yin_C_G0230_v1.md#confluent-arithmetic-lower-bound) | Exact factorized Q_arith at selected good primes, all original roots and cross-exponent Galois nonvanishing; degree1 nonvanishing is the immediate same torsion contradiction, and the reciprocal surplus branch has d>=2. |
| dependency | [Rational primary capture construction](Yin_C_G0205_v1.md#capture-equivalence) | Exact summable-distinct positive-primary criterion, used only to reconstruct a possibly different finite-entropy rational counterexample if one exists. |
| dependency | [Accepted nonreciprocal threshold](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Only theta0-root gap at statement/applicability depth, to recover reciprocity at a unit endpoint of no larger positive measure. |
| dependency | [Retained exact native control](../computations/programs/Yin_J_G0009/readme.md#results-and-limits) | Existing complete programs and both exact outputs, all-k Q_arith9 and the six needed cyclic indices/gcd overlap; no new execution or global growth inference. |
| dependency | [Accepted original Salem input](Yin_C_G0226_v1.md#lehmer-joint-prime-control) | Only the original degree10 irreducible unit and all-power degree-preserving domain of the finite J9 control, not any new cyclic computation. |
| support | [Earlier prime-only endpoint](Yin_C_G0218_v1.md#power-degree-reduction) | Exact earlier existence/sequence reduction and distinct-subsequence reasoning, kept separate from the stronger all-positive-power endpoint proved here. |


### Decision complete-retained-proof-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:08 |
| status | proved |
| reason | Adopt the complete retained order/resultant/cyclic and all-power norm-descent theorem after actual full current self-review, including all original-root/scalar/field/control and existence-only interfaces. Existing native evidence is read statically, source thresholds retain their accepted depth and no surplus-growth or original-flow preservation is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | All original-root multiplicities, index/local scalar domains, exact signed/composition/cyclic identities, eligible-prime floor, degree8 control and existence-only norm descent with every unit/sequence/flow boundary. |
| argument | [Argument](#argument) | Entire original sections and formulas1--19, including complete field/conjugate-quartic control, direct norm-product proof, cyclic gcd overlap and exact retained finite control; no proof summary replaces any step. |
| dependency | [Dependency](Yin_C_G0230_v1.md#confluent-arithmetic-lower-bound) | Exact factorized Q_arith at selected good primes, all original roots and cross-exponent Galois nonvanishing; degree1 nonvanishing is the immediate same torsion contradiction, and the reciprocal surplus branch has d>=2. |
| dependency | [Dependency](Yin_C_G0205_v1.md#capture-equivalence) | Exact summable-distinct positive-primary criterion, used only to reconstruct a possibly different finite-entropy rational counterexample if one exists. |
| dependency | [Dependency](../audits/literature/Smy08/Yin_U002.md#smy08-u002) | Only theta0-root gap at statement/applicability depth, to recover reciprocity at a unit endpoint of no larger positive measure. |
| dependency | [Dependency](../computations/programs/Yin_J_G0009/readme.md#results-and-limits) | Existing complete programs and both exact outputs, all-k Q_arith9 and the six needed cyclic indices/gcd overlap; no new execution or global growth inference. |
| dependency | [Dependency](Yin_C_G0226_v1.md#lehmer-joint-prime-control) | Only the original degree10 irreducible unit and all-power degree-preserving domain of the finite J9 control, not any new cyclic computation. |
| support | [Support](Yin_C_G0218_v1.md#power-degree-reduction) | Exact earlier existence/sequence reduction and distinct-subsequence reasoning, kept separate from the stronger all-positive-power endpoint proved here. |
| review | [Actual complete current self-review](../audits/reviews/Yin_R_G0515_v1.md#current-arithmetic-norm-finding) | Entire exact current statement, complete retained proof and every selected interface, self-reviewed; original dated checks and evidence remain separate. |

## Complete retained argument

<a id="argument"></a>

Original proof date: 2026-10-07.

<a id="powered-order-index"></a>
## The powered discriminant quotient is an order index

Let alpha be a nonzero nontorsion algebraic integer of degree d, with monic minimal polynomial P and conjugates alpha_1,...,alpha_d.
For every n>=1 define the full degree-d polynomial

    P^[n](t)=product_i(t-alpha_i^n).

It is monic integral, but its roots need not be distinct.
If e_n=[Q(alpha):Q(alpha^n)], the equal embedding fibers give

    P^[n]=(minimal polynomial of alpha^n)^(e_n).         (1)

Thus deg(alpha^n)=d is exactly the assertion that P^[n] is squarefree.
This gives a finite exact eligibility test for every specified composite exponent.
Removing its multiplicities while keeping d in a determinant construction is not a valid substitute.

Let C_n be the d by d integral matrix whose j-th column is the coordinate vector of alpha^(nj) in the basis 1,alpha,...,alpha^(d-1), for 0<=j<d.
Evaluating at the conjugates shows that

    det C_n=b_n(alpha)
       =product_(i<j) (alpha_j^n-alpha_i^n)/(alpha_j-alpha_i).
                                                               (2)

This also directly proves integrality of b_n.
It is nonzero exactly when e_n=1.
In that case both rings are full-rank orders in the same field and

    I_n(alpha):=[Z[alpha]:Z[alpha^n]]=|b_n(alpha)|,
    |disc P^[n]|=|disc P| I_n(alpha)^2.                 (3)

This is the index between the two displayed monogenic orders, not the index of either order in the maximal order.
If e_n>1, b_n=0 and there is no finite-index interpretation as two rank-d orders.

For a,b>=1 with deg(alpha^(ab))=d, all intermediate degrees equal d.
The chain of orders gives the exact multiplicative cocycle

    I_(ab)(alpha)=I_a(alpha) I_b(alpha^a)
                =I_b(alpha) I_a(alpha^b).              (4)

With the compatible conjugate orderings in (2), the same identities hold for the signed b's.
One can also prove them by cancelling the two successive divided-difference products.
In particular I_a divides I_(ab), but it is incorrect to replace I_b(alpha^a) by I_b(alpha) without an additional argument.

There is a useful exact local test.
For a rational prime ell, C_n modulo ell is the power-coordinate matrix in F_ell[t]/(P mod ell).
At n=ell it is the matrix of the Frobenius map.
That map is invertible precisely when this finite algebra is reduced, equivalently when P mod ell is squarefree.
Consequently

    ell divides b_ell  if and only if  ell divides disc P.       (5)

This statement remains valid with zero determinants; for its order interpretation assume degree preservation.
For ell not dividing disc P, evaluation at the distinct roots of P mod ell further gives

    ell divides b_n
      if and only if two distinct reduced roots have equal n-th powers.
                                                               (6)

For units those roots are nonzero, so (6) is a condition on a root ratio being an n-th root of unity in the algebraic closure of the finite field.
Frobenius powers themselves are permutations there; an unramified ell supplies no automatic ell factor in b_ell.
Equations (5)--(6) expose the local arithmetic that an index-growth argument must control.
They supply no uniform frequency or size bound for such collisions.

<a id="mixed-power-resultant-identities"></a>
## Mixed-power resultants and their composition laws

For distinct positive a,b put

    R_(a,b)(alpha)=Res(P^[a],P^[b])
                 =product_(i,j)(alpha_i^a-alpha_j^b).

This nonzero integer is defined using all d conjugates, whether or not either power has degree d.
Nonvanishing follows from the cross-exponent Galois argument in L G0057; it only needs alpha nonzero and nontorsion.

For any c>=1,

    R_(ca,cb)/R_(a,b)
      =product_(i,j) sum_(r=0)^(c-1)
           (alpha_i^a)^(c-1-r)(alpha_j^b)^r

is an integer.
Thus

    R_(a,b) divides R_(ca,cb).                          (7)

The quotient is an algebraic integer fixed by the Galois group, so divisibility here is in Z.
If e_c=[Q(alpha):Q(alpha^c)], then the exact minimal-polynomial version of composition is

    R_(ca,cb)(alpha)=R_(a,b)(alpha^c)^(e_c^2),           (8)

where the right-hand resultant now uses the distinct conjugates of alpha^c.
Both sets of embedding fibers have size e_c; their product explains the square.
The exponent may be dropped only when c preserves degree.

For completeness the polynomial-composition resultant has another exact identity.
With g=gcd(a,b),

    |Res(P(t^a),P(t^b))|
       =|R_(a/g,b/g)(alpha)|^g.                        (9)

Indeed, for nonzero x,y the roots of t^a-x give

    Res(t^a-x,t^b-y)
       =(-1)^(a+g)(x^(b/g)-y^(a/g))^g.

Multiplying this identity over conjugate pairs and taking absolute values proves (9).
This operation should not be confused with R_(a,b): substitution in the polynomial and powering its roots are different constructions.

If b/a=ell^r is a positive prime power, coefficientwise Frobenius gives P^[b]=P^[a] modulo ell, hence ell^d divides R_(a,b).
It gives this single ell^d floor, not ell^(rd).
The full polynomial and multiplicity convention above makes the congruence valid even through intermediate degrees that drop.
The nonzero confluent construction still separately requires degree preservation at every level actually used as d distinct nodes.

<a id="cyclic-resultant-extraction"></a>
## Cyclic factors in the unit and reciprocal-unit scopes

Define the nonzero cyclic resultants

    c_n=Res(P,t^n-1)=product_i(alpha_i^n-1),       n>=1.

They are integers.
For an algebraic unit, the diagonal i=j in R_(a,b) has absolute value |c_(|a-b|)|, since the remaining norm factor is a unit.
The product over off-diagonal pairs is also a Galois-invariant algebraic integer.
Hence

    c_(|a-b|) divides R_(a,b)       for units.           (10)

Without the unit assumption, the exact diagonal also includes Norm(alpha)^min(a,b), with a possible sign.
It must not be silently removed from a quantitative identity.

There is a stronger simultaneous factorization in the original reciprocal core.
Assume P is monic irreducible reciprocal noncyclotomic, with constant coefficient one and d=2r.
Inversion permutes its roots without a fixed point.
In addition to the diagonal, select the disjoint inverse-matching pairs (alpha_i,alpha_i^(-1)).
Their product is exactly c_(a+b), since Norm(alpha)=1.
Both selected sets and their complement are Galois stable.
Thus

    R_(a,b)=c_(|a-b|) c_(a+b) Z_(a,b),
    Z_(a,b) is a nonzero integer.                      (11)

Here the two factors divide as one product because they arise from disjoint factors of the resultant.
This is stronger than merely knowing two separate divisibilities.
At d=2 the complement is empty and Z_(a,b)=1.

The powered index has a related reciprocal factor.
Write

    P(t)=t^r T(t+t^(-1)),       T in Z[x] monic.

The existence of T follows by expressing integral reciprocal Laurent polynomials in t+t^(-1).
Put U_0(x)=1, U_1(x)=x and U_j(x)=x U_(j-1)(x)-U_(j-2)(x).
Define

    F_n=Res(T,U_(n-1)).

Each reciprocal root pair alpha,alpha^(-1) contributes

    (alpha^n-alpha^(-n))/(alpha-alpha^(-1))
       =U_(n-1)(alpha+alpha^(-1))

to b_n.
The remaining unordered pairs are Galois stable too, so

    b_n=F_n H_n       with H_n in Z,
    c_(2n)=c_2 F_n^2.                                 (12)

The second identity follows by grouping each cyclic resultant into reciprocal pairs and dividing: the ratio of the pair factors is the square of the displayed divided difference.
F_n is nonzero because alpha is nontorsion.
Thus c_(2n)/c_2 is a positive integer square, and when degree is preserved,

    I_n^2 >= |c_(2n)/c_2|.                             (13)

No assertion that the factors H_n or Z_(a,b) are units is made.

<a id="explicit-cyclic-surplus-bound"></a>
## An explicit lower bound for the retained arithmetic surplus

Keep the reciprocal-unit assumptions and the L G0057 selected primes p_1,...,p_S, each preserving degree.
For every selected p set

    D_p=|c_(p-1)c_(p+1)|,
    t_p=D_p/gcd(D_p,p^d).

By (11), D_p divides R_(1,p), while Frobenius gives p^d dividing the same integer.
Therefore t_p divides R_(1,p)/p^d.
This gcd correction is essential: multiplying the cyclic factor by the Frobenius floor as if they were coprime would overcount valuations.

The exact Q_arith of L G0057 consequently satisfies

    Q_arith >= product_p |c_(2p)/c_2|
          * product_p t_p^(2k)
          * product_(p<q) |c_(q-p)c_(p+q)|^2.           (14)

Every factor on the right is a positive integer.
The first product uses (13), the second the corrected normalized base resultants, and the third the cross-prime factorization (11).
This is a concrete lower estimate on retained arithmetic data, valid at arbitrary degree and without a Perron assumption.
It is not a positive uniform lower estimate after the determinant's analytic costs.

A growth argument now has identifiable arithmetic content: it could control the actual order indices, extra local resultant valuations, or cyclic resultants at the difference and sum indices in (14).
The identities and divisibilities alone do not force those quantities to offset the discriminant and norm costs.
In particular integer factors may equal one, and the same prime valuation cannot be counted twice within a normalized resultant.
No distribution, primitive-divisor, or uniform separation theorem for these factors is assumed here.

The exact standard Lehmer control in [J G0009](../computations/programs/Yin_J_G0009/readme.md) makes this boundary concrete.
For the selected primes 2 and 3 it gives I_2^2=9, I_3^2=1, both normalized base resultants of absolute value one, and |R_(2,3)|=1.
Thus Q_arith=9 for every base multiplicity k.
Increasing this k does not amplify that control's surplus.
This single retained input does not rule out a different prime selection or a general growth mechanism.
The computation is separately owned and reviewed; no new computation is part of this argument.

The same exact control also evaluates precisely the cyclic indices needed in (14):

    c_1=c_2=c_3=c_5=c_6=-1,       c_4=-9.

Thus |c_4/c_2|=9 and |c_6/c_2|=1, while D_2=1 and D_3=9.
The whole factor D_3 is already contained in 3^10, so t_3=1, not nine; also t_2=1 and |c_1 c_5|=1.
Formula (14) equals nine for every k, exactly saturating this input's Q_arith.
This is a concrete valuation-overlap check and a sharp control for the factor extraction, not a uniform growth theorem.
The two retained algorithms and their 67 payload checks belong to J G0009; the drafting agent read the resulting exact values without rerunning either program.

<a id="prime-endpoint-composite-counterexample"></a>
## Prime-degree preservation is not pointwise all-power preservation

The finite-level degree condition deserves an actual reciprocal unit control.
Let s=sqrt(3), put a_+=4+s and a_-=4-s, and let

    beta_+>1,       beta_++beta_+^(-1)=a_+,
    beta_->1,       beta_-+beta_-^(-1)=a_-.

The polynomial of beta=beta_+ is

    t^4-8t^3+15t^2-8t+1.

It is irreducible: Q(beta) contains s=beta+beta^(-1)-4, and the quadratic discriminant 15+8s over Q(s) has rational norm 33, so cannot be a square in Q(s).
Both real embeddings of that discriminant are positive.
Thus K=Q(beta) is totally real of degree four, with four distinct positive conjugates beta_+,beta_+^(-1),beta_-,beta_-^(-1).

Let zeta=exp(pi i/6) be a primitive twelfth root of unity and set alpha=beta zeta.
Positive powers of the four distinct positive beta conjugates remain distinct, so Q(beta^6)=K.
Since alpha^6=-beta^6, K is contained in Q(alpha).
Also zeta=alpha/beta, and zeta satisfies t^2-s t+1 over K.
It is nonreal, so [K(zeta):K]=2 and deg alpha=8.

The conjugates above the two embeddings of s occur in pairs: beta_+ and its inverse are each multiplied by zeta,zeta^(-1), whereas beta_- and its inverse are each multiplied by zeta^5,zeta^7.
The four moduli are distinct; within each equal-modulus pair the ratio has exact order six.
Therefore

    deg(alpha^n)=8 if 6 does not divide n,
    deg(alpha^n)=4 if 6 divides n.                      (15)

In particular every prime, and even every prime-power exponent, preserves degree, while exponent six does not.

For U=t^4-3t^3+20t^2-3t+1, the four conjugates over the embedding s=sqrt(3) have polynomial U-4s t(t-1)^2; the other four have U+4s t(t-1)^2.
Multiplying these conjugate quartics shows that the minimal polynomial of alpha is the reciprocal integral unit polynomial

    [t^4-3t^3+20t^2-3t+1]^2-48t^2(t-1)^4.              (16)

Its degree-eight minimality was established by the field argument, not a numerical factorization.
Its Mahler measure is (beta_+ beta_-)^2>16, since beta_+>4 and beta_->1.
Thus this is a pointwise quantifier control outside the small-measure window; it is not a Lehmer counterexample or evidence that the same phenomenon occurs near measure one.

<a id="all-positive-power-existence-descent"></a>
## A norm descent nevertheless gives all-power endpoints in existence scope

The preceding counterexample does not obstruct a stronger existence reduction.
The following proof was supplied by the coordinating AI, with the direct root-product version checked by assess_shortness_route and the drafting agent.

Let alpha again be any nonzero nontorsion algebraic integer.
If some n>=1 lowers its degree, put

    K=Q(alpha),       L=Q(alpha^n),       e=[K:L]>1,
    gamma=Norm_(K/L)(alpha),
    f=[L:Q(gamma)].

Then gamma is a nonzero algebraic integer in L, and is a unit if alpha is.
Taking norms gives

    gamma^n=(alpha^n)^e,
    gamma/alpha^e is an n-th root of unity.             (17)

So gamma is nontorsion.
Its degree is d/(ef)<d.
Moreover the exact Mahler relation is

    M(alpha)=M(gamma)^f,
    m(gamma)=m(alpha)/f<=m(alpha).                      (18)

One direct proof of (18) uses no new height theorem.
For every embedding tau of L there are e extensions sigma to K.
All their values sigma(alpha) have a common modulus r_tau, since their n-th powers equal tau(alpha^n).
Hence |tau(gamma)|=r_tau^e, and

    M(alpha)=product_tau max(1,r_tau)^e
            =product_tau max(1,|tau(gamma)|)
            =M(gamma)^f.

The last equality counts each embedding of Q(gamma) exactly f times.
Monicity supplies these ordinary root-product Mahler measures.
Equivalently the retained absolute-height identity gives h(gamma)=e h(alpha), with the same degree calculation.
The direct product proof fixes the normalization without using that equivalent route as an extra premise.

Whenever an exponent lowers degree, replace alpha by gamma.
Each actual replacement strictly lowers a positive integer degree and preserves positive Mahler logarithm without increasing it.
Thus the process terminates at an algebraic integer satisfying

    deg(alpha^n)=deg alpha for every n>=1.              (19)

This is an existence descent, not a finite procedure for deciding the universal condition (19).
It strengthens the available endpoint of the prime-only descent in [L G0014](Yin_C_G0218_v1.md#power-degree-reduction), rather than inferring (19) pointwise from that earlier endpoint.
On (16) at n=6 the norm replacement is beta^2; its degree drops to four and its Mahler measure is unchanged.

Consequently the infimum of positive logarithmic Mahler measures is unchanged on restricting to all-positive-power degree-preserving algebraic integers, and likewise within algebraic units.
A hypothetical positive sequence tending to zero can be replaced termwise, and a distinct subsequence can be extracted as in L G0014.
The same norm argument preserves summability of positive weights in the [finite-capture counterexample construction](Yin_C_G0205_v1.md#capture-equivalence).
It does not preserve a specified original flow or its numerical entropy.
Within the explicit unit window 1<M(alpha)<theta_0, where theta_0 is the real root greater than one of x^3-x-1, the accepted [Smy08-U002 nonreciprocal gap](../audits/literature/Smy08/Yin_U002.md#smy08-reciprocal-number) supplies reciprocity again at the endpoint, since the measure did not increase.
Reciprocity is not asserted to be invariant under every norm replacement.

This supplies a legitimate all-power endpoint for testing gap or nonattainment existence.
On an arbitrary unreplaced input the finite eligibility condition (1) still has to be checked.
The [multilevel finite certificate](Yin_C_G0232_v2.md#multilevel-degree-hypotheses) uses exactly that condition, while its floor-only optimization ceiling remains separate from growth of Q_arith.
