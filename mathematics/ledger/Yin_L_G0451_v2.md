---
author: Yin
---
# Matrix height-gap transfer: reciprocal-field conjugators and the paid dyadic power choice

<a id="scope-and-strategic-assessment"></a>
## Scope and strategic assessment

This bounded 2026-11-05 continuation of [L451v1](Yin_L_G0451_v1.md#scope-and-strategic-assessment) tests input-dependent conjugators that are jointly unitary only at the original neutral embeddings.
It concerns the unrestricted [G0001 contract](../tasks/Yin_T_G0001_v1.md#contract), through its reciprocal non-torsion unit core, without replacing that core by Salem numbers.
The matrix_height_return agent developed and checked the general local formula and explicit half-sum construction for human author Yin.
The main agent contributed the interval-splitting interpretation, the comparison with a gauge-equivalent hyperbolic half-sum form and the directive to return the actual integer condition through existing auxiliary results.
These are ordinary author exploration and source-applicability checks, without formal review, independent review, a Claim assessment or a uniform Mahler-gap proof.
No program, numerical calculation or solver is used.

The general construction reduces every finite-place joint spectral cost to one actual trace-field element a.
Requiring that element to be integral is weaker than requiring the displayed conjugator to be integral.
The explicit norm-one half-sum family does give an integral non-virtually-solvable matrix pair for every original input after choosing a sufficiently large power.
Its actual finite-place cancellation condition, however, is precisely an integral half-value of a polynomial with at most two reflected binary pairs.
The existing C864v2 result already charges that condition in a degree-linear window.
The remaining power expense is fully retained; increasing an upper bound is not treated as a lower bound on the actual height.

This is a substantive variant within the same matrix-height-transfer exploration.
The fixed-family and fixed Hadamard calculations remain at v1 with their own scopes.
The present account does not extend the class after the explicit test has returned to existing arithmetic costs.

<a id="inputs-and-source-limits"></a>
## Inputs and source limits

[L451v1's source scope](Yin_L_G0451_v1.md#source-scope-and-height-conventions) owns the actual Bre11 published-paper inspection, all-place normalized height, Theorem 3.1, Proposition 3.2 and closed-locus boundaries.
Only the normalized-height conventions, invariance under common conjugation and the fixed two-dimensional height gap are reused here.
No further original-source theorem or proof is claimed to have been inspected.

[C10v2's reciprocal preliminaries](../claims/Yin_C_G0010_v2.md#reciprocal-field-and-order-preliminaries) and [C243's trace-field statement](../claims/Yin_C_G0243_v1.md#statement) supply the actual nonidentity reciprocal involution and quadratic fixed field without total reality.
[C147v5](../claims/Yin_C_G0147_v5.md#statement) supplies the full original-field cyclic-norm bound, with powered-degree loss allowed.
[C864v2](../claims/Yin_C_G0864_v2.md#statement) supplies its already adopted uniform original-window bound for an actual integral half-value with at most four reflected binary pairs.
Its [original binomial price](../claims/Yin_C_G0864_v2.md#original-binomial-norm-return) includes the full ring of integers and keeps every original conjugate.
Those inputs retain their own source and review scopes; none is independently re-reviewed here.

The local search also inspected [C67's paraunitary rigidity](../claims/Yin_C_G0067_v1.md#statement), [C50's complete dyadic period and window costs](../claims/Yin_C_G0050_v1.md#statement), and [C227's symmetric realization and metric boundaries](../claims/Yin_C_G0227_v1.md#statement).
The inspected [S8 account](../strategies/Yin_S_G0008.md) contains only an unadopted arithmetic-hyperbolic-geometry and systole lead.
No arithmetic Fuchsian, systole, collar, quaternion-order existence or geometric lattice theorem is used.
The new calculations below are direct finite algebra and local norm estimates.
The bounded search supplies no exhaustive literature or novelty claim.

<a id="reciprocal-involution-and-general-conjugator"></a>
## Reciprocal involution and the general conjugator

Let alpha be a non-torsion algebraic integer unit with irreducible monic reciprocal minimal polynomial.
Write

    K=Q(alpha), d=[K:Q],
    tau(alpha)=alpha^(-1), F=K^tau=Q(alpha+alpha^(-1)),
    [K:F]=2,
    h=h_abs(alpha)=m(alpha)/d,
    s=alpha-alpha^(-1), D=s^2 in F,
    A=diag(alpha,alpha^(-1)).                          (Q1)

The involution tau is a field automorphism because the reciprocal minimal polynomial vanishes at alpha^(-1).
It is nonidentity, and the quadratic equation for alpha over Q(alpha+alpha^(-1)) identifies that field with the fixed field.
The non-torsion hypothesis makes s nonzero.
The element D is an algebraic integer in F.
The full ring O_K is stable under tau.

Choose arbitrary u,v in K^times such that

    x=u tau(u), y=v tau(v), delta=x+y!=0,
    P=[[u,v],[-tau(v),tau(u)]],
    B=P A P^(-1), G_alpha(u,v)={A,B},
    r=x/delta, q=y/delta=1-r,
    a=D r, b=D q=D-a.                                (Q2)

All matrices and parameters are in the original field K, while x,y,delta,r,q,a,b belong to F.
The nonzero hypotheses give r,q!=0.
The determinant of P is delta and the determinant of B is 1.

As alpha is non-torsion, the Zariski closure of its diagonal powers is the diagonal torus T.
The closure of the group generated by A and B therefore contains T and P T P^(-1).
Put E=diag(1,0) and

    Q=P E P^(-1)
      =delta^(-1)[[x,-uv],[-tau(u)tau(v),y]].           (Q3)

Both off-diagonal entries of Q are nonzero.
The Lie algebra of the closure contains H=diag(1,-1) and 2Q-I.
Its first and second commutators with H isolate the two nonzero off-diagonal directions, so together with H they span sl_2.
Thus the group generated by A and B is Zariski dense in SL_2 for every actual nondegenerate choice in Q2.
No generic choice or unproved non-virtually-solvable supply is needed once u,v,delta satisfy those conditions.

<a id="neutral-and-exceptional-embeddings"></a>
## Neutral and exceptional embeddings, and determinant norms

Let sigma:K->C be an embedding.
If |sigma(alpha)|=1, then sigma composed with tau equals complex conjugation composed with sigma on K, because the two maps agree on the field generator alpha.
At such a neutral embedding,

    sigma(delta)=|sigma(u)|^2+|sigma(v)|^2>0,
    sigma(r)=|sigma(u)|^2/sigma(delta) in (0,1),
    sigma(q) in (0,1).

The columns of sigma(P) are orthogonal and have squared length sigma(delta).
Hence sigma(P)/sqrt(sigma(delta)) is unitary, and both sigma(A) and sigma(B) are unitary.
The local joint spectral radius is exactly 1.

This conclusion is not extended to all embeddings of K.
For a real embedding of F with |sigma(alpha+alpha^(-1))|>2, the two embeddings of K above it are real and tau exchanges them.
The corresponding values u tau(u) and v tau(v) need not be positive, and delta may have either sign.
At a complex embedding of F there is no real-order or positivity assertion.
In particular F is not assumed totally real, and tau is not called complex conjugation globally.

Since delta belongs to F,

    Norm_(K/Q)(delta)=Norm_(F/Q)(delta)^2.              (Q4)

If u and v are algebraic integers then delta is a nonzero integer in F, so its absolute norm is at least 1.
That norm alone does not measure the matrix pair's spectral cost.
For any w in K^times, replacing (u,v) by (wu,wv) replaces P by diag(w,tau(w))P and delta by w tau(w)delta.
The diagonal factor commutes with A and simultaneously conjugates the pair, so every local joint radius and the normalized height remain unchanged.
Its determinant norm nevertheless changes by

    |Norm_(K/Q)(delta_new)|
      =|Norm_(K/Q)(w)|^2 |Norm_(K/Q)(delta)|.           (Q5)

The invariant ratio r, rather than an uncancelled determinant norm, controls the finite costs below.

At an arbitrary infinite embedding, a useful upper bound also keeps the exceptional data explicit.
A local diagonal change of basis commuting with A can balance the two off-diagonal entries of Q to have equal absolute value sqrt(|r q|).
In that basis Q has rank one and Euclidean operator norm |r|+|q|; the same is true of I-Q.
Writing B=alpha^(-1)I+sQ=alpha I-s(I-Q) gives

    R_sigma(G_alpha(u,v))
      <=max{max(|sigma(alpha)|,|sigma(alpha)|^(-1)),
             min(|sigma(alpha)|,|sigma(alpha)|^(-1))
                +|sigma(s)|(|sigma(r)|+|sigma(q)|)}.  (Q6)

The words A^n always give the corresponding lower bound max(|sigma(alpha)|,|sigma(alpha)|^(-1)).
At neutral embeddings the exact radius 1 above is used instead of the coarse upper estimate Q6.
No uniform bound on the exceptional values of r and q follows from the original Mahler measure in this general parameter class.

<a id="all-finite-place-cross-ratio"></a>
## Exact joint radii at all finite places

At every finite place w of K, alpha is a unit and |s|_w<=1.
The projectors E,Q satisfy

    E^2=E, Q^2=Q, E Q E=r E, Q E Q=r Q.              (Q7)

Also

    A=alpha^(-1)I+sE, B=alpha^(-1)I+sQ,
    tr(A B)=2+a.                                     (Q8)

For a product of k>=1 projector letters, remove consecutive repetitions.
The remaining alternating product of length ell is r^j E or r^j Q if ell=2j+1, and r^(j-1)EQ or r^(j-1)QE if ell=2j.
Let C_w be the maximum of 1 and the norms of E,Q,EQ,QE.
Every such product has norm at most C_w max(1,|r|_w)^(k/2).
The empty product has norm 1.

Expand any length-N word in A and B using Q8.
A term with k projector letters has scalar absolute value |s|_w^k.
The ultrametric triangle inequality costs no factor for the number of terms, while C_w is independent of N.
Taking N-th roots yields

    R_w(G_alpha(u,v))
      <=max{1,|s|_w sqrt(max(1,|r|_w))}
       =max{1,|a|_w^(1/2)}.                           (Q9)

For the last equality use |s|_w<=1.
If |a|_w>1, then |tr(A B)|_w=|a|_w because |2|_w<=1.
The determinant-one quadratic for the eigenvalues of A B shows that its spectral radius is |a|_w.
Repeating A B gives the reverse inequality in Q9.
If |a|_w<=1, determinant 1 gives the required lower bound 1.
Thus, at every finite place, including ramified and dyadic places,

    R_w(G_alpha(u,v))=max{1,|a|_w^(1/2)}.              (Q10)

Define h_fin(a)=d^(-1)sum_(w finite)n_w log^+|a|_w using the original K.
This is the usual field-independent finite part of the absolute height, even if a has smaller own degree.
The exact finite contribution to the matrix height is

    h_hat_fin(G_alpha(u,v))=(1/2)h_fin(a).              (Q11)

It vanishes exactly when a belongs to O_F=F intersect O_K.
In that case b=D-a belongs to O_F as well.
One may also see the common local lattice directly: A^(-1)=alpha I-sE and B^(-1)=alpha I-sQ, so the same expansion uniformly bounds all group words whenever |a|_w<=1.
The O_w-span of their translates of O_w^2 is then a full invariant lattice.
Conversely an invariant local lattice forces the basis-invariant radius to be 1.
No simultaneous globally free lattice or integral global basis is inferred.

<a id="interval-splitting-and-norm-condition"></a>
## Interval splitting retains a norm-realizability condition

At every neutral embedding D is strictly negative and r,q are strictly between 0 and 1.
Thus finite-place cancellation would supply nonzero a,b in O_F satisfying

    a+b=D,
    sigma(D)<sigma(a)<0 and sigma(D)<sigma(b)<0
    at every neutral trace embedding.                (Q12)

The interval conditions alone do not construct Q2.
The exact missing realizability condition is

    r/(1-r)=a/b in Norm_(K/F)(K^times).                 (Q13)

It is necessary because x/y=Norm_(K/F)(u/v).
It is also sufficient for realizing a given nondegenerate r by this parameterization: if Norm(w)=r/(1-r), take u=w and v=1.
Then delta=Norm(w)+1=1/(1-r) is nonzero and Q2 has the prescribed r.
This converse does not supply integral u,v or inexpensive exceptional embeddings.

The actual trace-field intervals are not an ordinary symmetric-integer-matrix realization.
C227's real-symmetric representation requires a totally real trace polynomial, while general reciprocal inputs here may have nonreal trace conjugates.
C67 also imposes an exact Laurent paraunitary identity and its declared original-order and support-window hypotheses, rather than merely Q12 at finitely many embeddings.
No result from either class automatically supplies the norm condition Q13 or the desired original-measure cost.
The explicit next construction tests those issues together instead of promoting the interval description to a new covering strategy.

<a id="input-dependent-half-sum-family"></a>
## An explicit input-dependent norm-one half-sum family

For every positive integer n put beta=alpha^n and choose

    u_n=(beta+1)/2, v_n=(beta-1)/2,
    P_n=(1/2)[[beta+1,beta-1],
              [1-beta^(-1),1+beta^(-1)]],
    B_n=P_n A P_n^(-1), G_n={A,B_n}.                  (N1)

Non-torsion makes u_n and v_n nonzero.
Since tau(beta)=beta^(-1),

    u_n tau(u_n)=(beta+1)^2/(4beta),
    v_n tau(v_n)=-(beta-1)^2/(4beta),
    delta_n=1,
    r_n=(beta+1)^2/(4beta).                            (N2)

Thus every G_n is a same-field Zariski-dense SL_2 pair.
The norm-one identity does not make the entries of P_n integral.
The even-exponent version of N1 differs from the choice u=(alpha^j+alpha^(-j))/2, v=(alpha^j-alpha^(-j))/2, n=2j, only by the diagonal gauge in Q5 with w=alpha^j.
Those descriptions have the same normalized matrix height; no new class is created by this gauge.

The exact finite formula Q10 becomes

    R_w(G_n)
      =max{1,|s|_w |alpha^n+1|_w/|2|_w}.              (N3)

At places not over 2 it is 1.
Since |alpha|_w=1 at finite places, put

    W_n(X)=(X^2-1)(X^n+1).

Then N3 gives

    h_hat_fin(G_n)
      =d^(-1) sum_(w|2) n_w
          (log 2+log|alpha^2-1|_w
                    +log|alpha^n+1|_w)_+,             (N4)
    h_hat_fin(G_n)=0
      iff W_n(alpha)/2 belongs to O_K.                (N5)

Indeed a_n=s^2r_n=W_n(alpha)^2/(4alpha^(n+2)), and alpha is a unit.
For every finite valuation, integrality of this square is equivalent to ord_w(W_n(alpha))>=ord_w(2), which proves N5 without replacing the maximal order by Z[alpha].
The actual polynomial W_n has degree and span n+2 and a nonzero value at alpha.
Its endpoints are 1 and -1.

<a id="automatic-mod-two-choice-and-archimedean-expense"></a>
## Automatic mod-two choice and complete archimedean expense

The quotient ring O_K/2O_K has 2^d elements, including ramified nilpotents when present.
The class of alpha is a unit.
Let n be its order in the finite group (O_K/2O_K)^times.
Its order divides the size of that group and therefore

    1<=n<=|(O_K/2O_K)^times|<=2^d-1.                  (N6)

No cyclicity of the unit group, residue-field replacement or squarefree assumption is used.
This actual order gives alpha^n-1 in 2O_K, hence both u_n and v_n are integers.
Their tau-images are integers as well, so P_n belongs to SL_2(O_K).
The resulting A and B_n are integral and their entire finite-place height is zero.
This is an automatic construction for every original input, but N6 is an exponential degree bound.

For each infinite embedding put c_sigma=max(|sigma(alpha)|,|sigma(alpha)|^(-1)).
Let

    H=(1/sqrt(2))[[1,1],[1,-1]].

The exact factorization

    P_n=diag(1,beta^(-1)) H diag(beta,1) H             (N7)

gives ||P_n||_sigma<=c_sigma^n.
The inverse factorization gives the same bound for P_n^(-1).
Therefore

    c_sigma<=R_sigma(G_n)<=c_sigma^(2n+1),
    2h<=h_hat_infinity(G_n)<=(4n+2)h.                 (N8)

Every original embedding and its actual local-degree weight is retained in N8.
No degree of Q(alpha^n) replaces d.
At each neutral embedding N7 is a product of unitary matrices, and the exact local radius is 1.
The exceptional real and complex embeddings are covered by the same upper bound, without treating tau as complex conjugation there.

If a choice n<=C d were available together with N5, N8 would give h_hat(G_n)<= (4C+2/d)m(alpha), so Bre11 would return a positive total-Mahler gap.
The automatic bound N6 supplies no such degree-linear choice.
A large n increases this upper bound; it is not, by itself, a lower bound on the actual archimedean contribution.
No inference about the actual lower growth at large n is made from N8.

<a id="cyclic-norm-price-of-the-power-choice"></a>
## Same-field cyclic-norm price of the power choice

For every integer k>=1 let C_k=|Norm_(K/Q)(alpha^k-1)|, a positive integer.
Both factors of W_n(alpha) are nonzero algebraic integers, and

    |Norm_(K/Q)(W_n(alpha))|
       =C_2 C_(2n)/C_n<=C_2 C_(2n).                  (N9)

At every finite place |W_n(alpha)|_w<=1.
Applying the product formula to N4 therefore gives

    log 2-log|Norm_(K/Q)(W_n(alpha))|/d
      <=h_hat_fin(G_n)<=log 2.                        (N10)

If 2h and 2nh are at most exp(-40), C147v5 gives

    h_hat_fin(G_n)
      >=log 2-Phi_5(2h)-Phi_5(2nh),                  (N11)

where Phi_5 is exactly the original-field function in C147v5.
Combined with N8,

    2h+log 2-Phi_5(2h)-Phi_5(2nh)
      <=h_hat(G_n)<=(4n+2)h+log 2.                   (N12)

Consequently, for any sequence of such original inputs and integer choices n with h->0 and nh->0, the actual full height tends to log 2.
In particular this happens along any hypothetical m(alpha)->0 sequence with n<=C d for fixed C.
The existence of such a vanishing-total-measure sequence is not asserted.

If N5 holds, then N10 requires log|Norm(W_n(alpha))|/d>=log 2.
Thus N11 prevents simultaneous finite-place cancellation and arbitrarily small h,nh.
For the stronger entry-integral choice alpha^n-1 in 2O_K, the already retained C864v2 binomial estimate gives the explicit original-domain price

    n m(alpha)/d> (log 2)/2.                          (N13)

N13 follows from the nonzero integer value (alpha^(2n)-1)/4 and the complete original norm bound in that existing proof.
It does not assume power-degree preservation and is not newly proved as a project theorem here.
The large-power choice can eliminate finite noise, but the known complete return has already incurred a nonvanishing power cost.

<a id="exact-return-to-c864"></a>
## The invariant cancellation condition is already a C864 half-value

The weaker spectral condition N5 itself, rather than only entry integrality of P_n, is also covered by the existing auxiliary mechanism.
Over F_2 the coefficientwise reduction of W_n is as follows:

    n=1: W_1 mod 2=X^3+X^2+X+1,
    n=2: W_2 mod 2=X^4+1,
    n>=3: W_n mod 2=X^(n+2)+X^n+X^2+1.               (N14)

For n=1, the actual span T=3 has two disjoint reflection pairs with e_1=0 and e_2=1.
For n=2, the middle terms cancel and the actual span T=4 has one reflection pair.
For n>=3, the actual span T=n+2 has two disjoint pairs with e_1=0 and e_2=2<T/2.
The leading and constant terms are always nonzero.
The original signed W_n is a valid coefficientwise lift in every case, not a substitution of a different evaluated polynomial.

Suppose n+2<=C d for a fixed C>0 and h_hat_fin(G_n)=0.
Then V=W_n has integral V(alpha)/2 in the full O_K and satisfies the exact binary-reflection hypothesis of C864v2 Part A with at most two pairs.
That adopted theorem yields

    m(alpha)>Gamma_bin(C)>0.                          (N15)

All actual n=1,2 exceptions, degrees, spans, original fields and integer conditions have been included.
C864v2 does not supply N5 automatically in that window.
Conversely the automatic modulo-two construction above supplies N5 only with its paid, potentially exponential n.
Thus this explicit input-dependent quaternion-form parameterization has returned to the existing integral half-value supply problem.
Calling delta_n=1 a free unit construction would miss exactly the denominator and window condition that N14--N15 preserve.

<a id="whole-task-return-and-limits"></a>
## Whole-Task return and limits

The general formula Q11 is a useful invariant distinction: all finite cost is half the finite height of a=s^2r, rather than an uncancelled norm of delta or the entry denominators of P.
Neutral compactness is automatic only where the actual reciprocal involution agrees with complex conjugation.
Exceptional embeddings and the realizability condition a/b in Norm_(K/F)(K^times) remain real mathematical obligations.
The interval formulation by itself is not a supply theorem.

For the concrete family N1, all original-input fields, non-virtually-solvable generation, neutral embeddings, finite-place cancellation and an actual automatic choice of n have been supplied.
The upper return cost is proportional to n m(alpha)/d, and the small-cost regime retains the positive dyadic background N12.
Exact finite-place cancellation in a degree-linear span is already charged by C864v2.
This is a failure of the proposed cheap-return mechanism, not a counterexample to Lehmer positivity or a proof that every input-dependent Hermitian construction must fail.

C67's fixed identity and support restrictions do not classify the entire Q2 parameter class.
C227's varying integral metric constructions do not provide the two-generator norm condition or the needed height control, and their totally real hypotheses cannot be applied to every reciprocal input.
The unadopted Fuchsian and systole analogy supplies no additional estimate in this account.
No new covering strategy is selected on the strength of Q12 alone.

Further work would require a concrete arithmetic construction outside this already paid half-sum class that simultaneously supplies the norm ratio, integral a, and inexpensive exceptional local joint radii on the original input.
No such construction has been found in this bounded test.
The present inquiry stops at that precise boundary without optimizing further powers, varying the same family or introducing another equivalent target.
