---
author: Yin
---
# Signed real places and arithmetic beyond the rational Gram barrier

Date: 2026-10-15.
Human author Yin.
Continuing F0010-inspired investigation under the explicitly resumed G0001 goal.

## Responsible question

Starting from the whole-reviewed [C103](Yin_C_G0103_v1.md#statement), investigate whether the exact negative directions at the other real embeddings of the Salem trace-field Gram provide a usable arithmetic constraint, or whether they instead expose a sharp limitation.
The totally-positive trace descent is already exhausted at the rational ceiling.
Try signed norms, determinant or exterior-power products, exact conjugate invariants, or another substantive leap suggested by the single-Haar formula.
Preserve actual degree, denominators, heights and all places; do not turn a chosen-embedding positive certificate into a uniform gap without paying them.
The original unrestricted G0001 target and near-one coverage remain open.

<a id="signed-gram-reuse-and-contributions"></a>
## 1. Reuse, contributions and exact scope

The delegated f_unitary_scope AI authors all new arguments below.
It authored [C103](Yin_C_G0103_v1.md#statement); that previous contribution is not independent evidence for this new inquiry.
Root assigned the signed-place question and subsequently requested explicit evaluation of its possible gap leverage, but supplied no proof step of the present constructions, determinant or estimates.
No native computation, program or J is used.

The author read the exact C103 statement and proof, [L_F5's exact scalar coefficient-Gram maximum](../ledger/Yin_L_F0005_v1.md#scalar-capacity-finite-sdp), [L66's trace-field and discriminant identities](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain), [L8's actual quartic Salem control](../ledger/Yin_L_G0008_v1.md#quartic-projection-obstruction), and the relevant signed-unit profile distinctions in [C9](Yin_C_G0009_v1.md#statement) and [C12](Yin_C_G0012_v1.md#unique-negative-place-forces-full-trace-degree).
The current complete proof home of the same retained scalar maximum is [C_F6](Yin_C_F0006_v1.md#scalar-capacity-finite-sdp); the original input-reading record above remains fixed.
Those profiles concern actual unit values and normalized field mixtures, not the coefficient Gram constructed here.
[C214 inverse-trace form](Yin_C_G0214_v1.md#inverse-trace-orbit) is a different integral matrix with different dimension/inertia; its warning that signed trace and determinant alone give no uniform gap is retained, not counted as the new exact formula.

A bounded local search for signed/trace Grams, exterior/principal-minor norms and the endpoint derivative T'(-2) found no retained version of the identities below.
This is not a novelty claim.
The finite block congruence and determinant calculation use the already identified elementary Schur method in [C75](Yin_C_G0075_v1.md#general-matrix-boundary-source-resolution) and its [BV04 selected reading](../audits/literature/BV04/readme.md); the present indefinite case is proved directly by completing squares, not inferred from a positive-definite source hypothesis.
The reciprocal product-of-differences mechanism is already explicit in [C243](Yin_C_G0243_v1.md#reciprocal-trace-order-index).
[CPSV18-U001](../audits/literature/CPSV18/Yin_U001.md#cpsv18-u001) keeps the prior ordering/Gram attribution only.
No new external theorem is adopted for the finite algebra.

For the final quantitative diagnostic, the author reads and uses the actual [Pri11-U001](../audits/literature/Pri11/Yin_U001.md#pri11-u001) discrepancy statement and [L168's finite bounded-degree escape](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape), at their already accepted statement/applicability scope.
The compact test and its constants are proved below.
No new source-proof audit, hypothetical near-one sequence existence, source acquisition or global record change is asserted.

## Statement

Let p in Z[z] be a monic irreducible SALEM polynomial of degree d=2h>=4, with roots lambda>1, lambda^(-1), and d-2 circle roots.
Put m=log lambda, t=lambda+lambda^(-1)>2 and F=Q(t).
Let T in Z[x] be the monic trace minimal polynomial of degree h, so p(z)=z^h T(z+z^(-1)).
Its real roots are t_1=t>2 and t_2,...,t_h in(-2,2).
All are distinct.
Define delta_j=t_j-2, C_j(z)=p(z)/(z^2-t_jz+1).
Let Q_j be C103's b=1 rank-three symmetric Gram, namely the coefficient outer products of C_j(z)(z-1)^2, C_j(z)(z-1), C_j(z) with weights1,2delta_j,delta_j^2 respectively, on the ORIGINAL width d.
Only Q_1 is PSD; all Q_j represent the same circle symbol |p|^2.

**A. Primitive third exterior norms.**
For every three-element coefficient-index subset I of{0,...,d}, let M_1[I] be the corresponding three rows of coefficient multiplication by C_1 on1,z,z^2, and u_I=det M_1[I] in Z[t].
Then

    det Q_1[I,I]=2(t-2)^3 u_I^2,
    Norm_(F/Q)(det Q_1[I,I])
       =(-1)^h 2^h T(2)^3 Norm_(F/Q)(u_I)^2.          (A)

For the first three and last three coefficient indices, u_I=1.
Thus the gcd of the absolute norms of all these nonzero principal minors is exactly2^h |p(1)|^3.
No coefficient/other-place factor is omitted from any individual minor.

**B. The actual integral signed trace Gram.**
Let S=sum_(j=1)^h Q_j.
It is an integral symmetric (d+1)-by-(d+1) matrix, with circle symbol h|p|^2, full rank, and exact inertia

    number of positive eigenvalues=h+2,
    number of negative eigenvalues=h-1.

Its determinant is

    det S=-2 disc(T)^2 T(2)^3 T'(-2).                (B)

In particular T'(-2) is nonzero.
The rational matrix R=S/h has the original symbol |p|^2 and determinant det S/h^(d+1); it is an indefinite coefficient Gram, not a feasible PSD capacity certificate.

**C. Exact arithmetic content and paid gap bound.**
Writing A=product_(j=2)^h(2-t_j), one has |p(1)|=(t-2)A.
The primitive norm floor in A, or B after dividing its displayed known arithmetic factors, gives precisely |p(1)|>=1.
It therefore gives t-2>=1/A>4^(-(h-1)), hence only the corresponding degree-dependent bound m>arcosh(1+1/(2*4^(h-1))).
Using only the unrefined integer floor |det S|>=1 is weaker.
This is an exact assessment of these norm-floor inferences, not a claim that every possible extra spectral or arithmetic use of S is exhausted.

For C103's general rational b=a/q>=1 in lowest terms, s=b+b^(-1)<t, put D=aq, U=a^2+q^2, V=4aq-a^2-q^2 and F_1=D^h T(U/D)=q^d p(a/q), F_2=D^h T(V/D).
The first-three-coordinate principal minor Delta_b has

    Delta_b=2 b^-2 (t-s)^2(t+s-4),
    Norm_(F/Q)(Delta_b)
       =(-1)^h 2^h F_1^2 F_2/(a^(5h) q^h).          (C)

Both F_1,F_2 are nonzero integers.
The cleared quantity a^5 q Delta_b is integral.
The coefficient matrix Q_b has the explicit sufficient denominator (aq)^2; neither is asserted least.
These norms are exactly the two displayed rational trace evaluations with their full denominator powers.
In particular t-s >= (aq)^(-h)(s+2)^(-(h-1)); no uniform separation is inferred.

**D. Quantitative failure of discarding the signed part.**
If d>=55 and lambda<=2, put epsilon_d=sqrt(max(log d/d,m/d)).
Then

    R00=[Tr_F(t^2)-2Tr_F(t)+h]/h,
    |R00-3|<=396 epsilon_d.                          (D)

For every real symmetric PSD coefficient Gram G of |p|^2 at the same width,

    ||R-G||_op >= max(0,3-396 epsilon_d-exp(2m)).      (E)

Consequently along any HYPOTHETICAL sequence of Salem inputs with m tending to zero, d tends to infinity, R00 tends to3 while the true PSD maximum M(p)^2 tends to1, and the distance to the same-symbol PSD Gram set has liminf at least2.
This is not an eigenvalue-norm lower bound for the distance to the entire unconstrained PSD cone, and it does not construct such a sequence.
No uniform Mahler gap follows.

**E. Actual column values and their full norm costs.**
In the original field K=Q(lambda), put u_k=C_1(lambda)(lambda-1)^k for k=0,1,2, and let sigma(lambda)=lambda^-1.
These are nonzero elements of Z[lambda], with

    u_k sigma(u_k)=T'(t)^2(2-t)^k,
    Norm_(K/Q)(u_k)=disc(T)^2 p(1)^k.                (F)

Their exact field profile u_2 sigma(u_2)+2(t-2)u_1 sigma(u_1)+(t-2)^2 u_0 sigma(u_0) is zero.
The three weights are algebraic, and the middle weight changes sign at every other real embedding.
This is not a normalized positive rational unit profile, and no nonzero column value or discriminant norm cost is omitted.

## Argument

<a id="signed-trace-domain"></a>
## 2. Original degree, polynomial coefficients and all real places

The reciprocal trace construction in L66 gives [Q(lambda):F]=2, [F:Q]=h and p(z)=z^h T(z+z^-1), with T monic integral irreducible.
For a Salem polynomial the inverse-pair traces consist exactly of t>2 and h-1 real numbers in(-2,2).
Values+/-2 would give a root+/-1 of p and contradict irreducibility of degree at least4.
Separability makes all traces distinct.
Thus T(2)<0, T(-2) has sign(-1)^h, and

    p(1)=T(2),
    p(-1)=(-1)^h T(-2),
    Norm_F(t-2)=(-1)^h T(2).                         (1)

Each C_j is monic of degree d-2 with constant1.
Dividing the original integer p by z^2-xz+1 using its monic leading term constructs a polynomial quotient C(z;x) with coefficients in Z[x].
At x=t_j the remainder vanishes because that quadratic divides p, so C_j=C(z;t_j).
This specifies every coefficient algebraically from the original p and does not presume the value of lambda or a spectral factor.

Let M_j denote coefficient multiplication by C_j from the three-dimensional block1,z,z^2 into1,z,...,z^d.
It is injective.
The first three rows are lower triangular with diagonal1, and the last three are upper triangular with diagonal1, because C_j(0)=1 and C_j is monic.
Both three-row determinants are therefore1.
All entries of M_1 are algebraic integers in Z[t], and M_j is its actual jth conjugate.

In these three coefficient coordinates define

    H(x)=[[(x-1)^2, -2(x-1), 1],
          [-2(x-1), 2x,      -2],
          [1,        -2,       1]].                 (2)

The vectors (1,-2,1),(-1,1,0),(1,0,0), with weights1,2(x-2),(x-2)^2, give exactly H(x) as a sum of weighted coefficient outer products.
Their determinant has square1, so

    det H(x)=2(x-2)^3,
    Q_j=M_j H(t_j) M_j^T.                           (3)

All entries of Q_1 are in Z[t].
The elementary identity from C103 is a polynomial identity in the real parameter x and applies at EVERY t_j, even though its weights cease to be positive.
It gives v_d(z)^* Q_j v_d(z)=|p(z)|^2 for all z on T.
At j1 all three weights are positive.
At j>1 their signs are+,-,+ and the coefficient vectors are independent, giving two positive and one negative eigenvalue of Q_j, with zeros in the remaining directions.

<a id="primitive-third-minor-norms"></a>
## 3. Every third principal minor and its exact norm content

For a three-row selector I, (3) gives the square-matrix determinant identity

    det Q_1[I,I]=det H(t) * det(M_1[I])^2
                =2(t-2)^3 u_I^2.                   (4)

This formula includes zero minors.
Taking the ORIGINAL trace-field norm over all h embeddings and using(1) yields

    Norm_F(det Q_1[I,I])
       =2^h [(-1)^h T(2)]^3 Norm_F(u_I)^2
       =(-1)^h 2^h T(2)^3 Norm_F(u_I)^2.             (5)

The norm of u_I is an integer because u_I is algebraic integral.
If u_I is nonzero its norm is nonzero; its square is a positive integer.
The first-three and last-three selectors have u_I=1.
Thus all absolute nonzero norms are multiples of2^h|T(2)|^3, and that value itself occurs.
This proves the gcd assertion in A without computing any other minor or claiming an arithmetic-complexity bound.

If one instead uses the product of the three nonzero eigenvalues of Q_1, the exact coefficient-basis cost also remains visible.
Cauchy--Binet gives

    product_(three nonzero eigenvalues) Q_1
       =2(t-2)^3 det(M_1^T M_1).                    (6)

At every embedding M_j has full real column rank, so det(M_j^T M_j)>0.
Its field norm is a positive integer, and (6) adds precisely this full coefficient-Gram norm to the same2^h|p(1)|^3 factor.
It is not a free normalization of the coefficient basis.
Equation(6) follows either by summing the principal three-minors in(4), or by the equality of the nonzero eigenvalues of M_1 H(t) M_1^T and H(t) M_1^T M_1.
Only the first, finite-minor proof is needed here.

<a id="integral-trace-gram-inertia"></a>
## 4. Integral trace matrix and exact full inertia

Define S=sum_j Q_j.
Since its entries are traces of algebraic integers in Z[t], S is integral and symmetric.
By the exact circle identities after(3), it represents h|p|^2.
Dividing by h represents |p|^2 but introduces the displayed rational normalization; it does not make the matrix positive.

Write the coefficient columns of p,C_j,zC_j as a,c_j,b_j respectively.
Since

    C_j(z)(z-1)^2=p(z)+(t_j-2)zC_j(z),

expanding the three weighted squares gives

    Q_j=a a^T+delta_j(a b_j^T+b_j a^T)
          +delta_j t_j(c_j c_j^T+b_j b_j^T)
          -2delta_j(c_j b_j^T+b_j c_j^T).            (7)

Let U be the real (d+1)-by-(d+1) matrix with columns

    a,c_1,b_1,c_2,b_2,...,c_h,b_h.

These columns are independent.
Indeed a linear combination of the last d columns is sum_j C_j(z)(u_j+v_j z).
Evaluating at the two distinct roots of z^2-t_jz+1 eliminates every other summand and forces u_j=v_j=0, since C_j is nonzero at those roots.
The p column has degree d whereas the other columns have degree at most d-1, so it adds an independent direction.
This is a real coefficient basis; its arithmetic determinant is computed in Section5 rather than treated as unit volume.

Equation(7) says S=U A U^T, where A has top-left entry h, off-diagonal couplings delta_j only from the top coordinate to each b_j, and local diagonal blocks

    B_j=delta_j [[t_j,-2],[-2,t_j]].                 (8)

Each B_j is invertible, because t_j is neither2 nor-2.
For j1, B_j has two positive eigenvalues.
For j>1, its eigenvalues are delta_j(t_j-2)=delta_j^2>0 and delta_j(t_j+2)<0, so it has one positive and one negative eigenvalue.
No comparison of the eigenvalues of Q_j with those of S is inferred by summing them.

Let B be the direct sum of the B_j and let r be the coupling column whose jth pair is(0,delta_j).
The real invertible change of coordinates completing the square gives

    [[h,r^T],[r,B]] congruent to diag(h-r^T B^-1 r,B).

This follows by expanding x^T B x+2y r^T x+h y^2 at x+B^-1 r y, and requires only invertibility, not positive definiteness, of B.
The scalar is

    h-r^T B^-1 r
       =h-sum_j delta_j*t_j/(t_j^2-4)
       =h-sum_j t_j/(t_j+2)
       =sum_j 2/(t_j+2)>0.                          (9)

All denominators are positive because every t_j>-2.
Hence the blocks contribute h+1 positive and h-1 negative directions, and the final positive scalar adds one.
Invertible real congruence preserves the numbers of positive and negative squares, so S has full inertia(h+2,h-1).
This proves B's signature and full rank, including the smallest Salem degree d4,h2.
No minimum-inertia statement for arbitrary rational Grams is asserted.

<a id="trace-gram-exact-determinant"></a>
## 5. The coefficient-basis determinant and closed arithmetic formula

The determinant of U cannot be dropped.
Let V be the d-by-d coefficient matrix of C_j,zC_j, omitting the degree-d row.
Expansion using the monic p column gives det(U)^2=det(V)^2.
Label the two roots of z^2-t_jz+1 by alpha_j,beta_j, with alpha_j beta_j=1, and let E be evaluation of degrees0,...,d-1 at all these d roots, in paired order.
It is an invertible complex Vandermonde matrix.
Evaluation of V is block diagonal, with jth two-by-two block

    [[C_j(alpha_j), alpha_j C_j(alpha_j)],
     [C_j(beta_j),  beta_j C_j(beta_j)]].

For i distinct from j, evaluating z^2-t_i z+1 at alpha_j or beta_j gives respectively alpha_j(t_j-t_i) and beta_j(t_j-t_i).
Thus

    C_j(alpha_j) C_j(beta_j)=product_(i!=j)(t_j-t_i)^2,
    product_j C_j(alpha_j)C_j(beta_j)=disc(T)^2.      (10)

The square of the determinant of EV is therefore disc(T)^4 product_j(t_j^2-4).
On the other hand det(E)^2=disc(p), and the same grouped-root calculation, also retained in L66, gives

    disc(p)=disc(T)^2 product_j(t_j^2-4).

Every factor is nonzero.
Division proves

    det(U)^2=det(V)^2=disc(T)^2.                      (11)

This is a squared REAL basis determinant; complex root evaluation is only a proof device.
No maximal-order discriminant or square root of disc(T) replaces the actual coefficient discriminant.

From(8), det B_j=(t_j-2)^3(t_j+2).
Also the elementary logarithmic derivative of the finite root product gives

    sum_j 2/(t_j+2)=-2 T'(-2)/T(-2).

Combining(9)--(11) yields

    det S=disc(T)^2 * [product_j(t_j-2)^3(t_j+2)]
                         * [-2T'(-2)/T(-2)]
         =-2 disc(T)^2 T(2)^3 T'(-2).                 (12)

The sign is(-1)^(h-1), agreeing with the h-1 negative eigenvalues.
The derivative is nonzero: T(-2) is nonzero and its logarithmic derivative is a strictly negative sum.
All quantities in(12) are ordinary integers.
For R=S/h, the determinant is exactly(12) divided by h^(d+1); h is the normalization of the symbol sum, not a normalized von Neumann matrix trace or a reduction of the original Mahler degree.

<a id="signed-norm-gap-assessment"></a>
## 6. What the integer norm floors actually imply

Let delta=t-2>0 and A=product_(j>1)(2-t_j)>0.
Since every t_j for j>1 is strictly between-2 and2,

    |p(1)|=-T(2)=delta A in Z_(>0),
    A<4^(h-1),
    delta>=1/A>4^(-(h-1)).                           (13)

In particular m=arcosh(t/2) has only the degree-dependent lower bound in C.
This is the existing original evaluation Norm_(Q(lambda)/Q)(lambda-1)=p(1), with absolute value; no trace-subfield degree has been used to halve the original norm cost.

Equation(5) shows exactly why a third exterior integer norm cannot supply additional primitive income: it is the cube of this same evaluation, times2^h and a squared integral coefficient norm.
The first-three minor has no extra coefficient factor.
The integer floor on that minor norm is already implied by |p(1)|>=1 and gives no stronger lower bound on delta.
If a different minor has large Norm(u_I)^2, it must be retained in both its all-place size and its arithmetic value; suppressing it is not allowed.

The same conclusion can be made exact for the trace determinant.
The known factors satisfy

    |det S|/[2 disc(T)^2 |T'(-2)|]=|T(2)|^3.

Using the fact that this quotient is the cube of a nonzero integer gives precisely |T(2)|>=1, with no stronger floor.
Using only |det S|>=1 instead gives

    delta >= [2 disc(T)^2 |T'(-2)| A^3]^(-1/3),       (14)

which is weaker than1/A because disc(T)^2 and |T'(-2)| are positive integers.
Formula(14) has all of its discriminant, endpoint and degree costs; it must not be read as a uniform numerical gap.
These statements assess the actual integer-floor deductions from the displayed invariants.
A different independently proved bound on the complete spectral geometry or on the displayed arithmetic factors might add information; no theorem excluding every such use is claimed.

<a id="rational-parameter-minor-prices"></a>
## 7. Cofinal rational parameters retain rational-evaluation costs

Use C103's rational parameter b=a/q>=1 with coprime positive integers a,q, s=b+b^-1<t, and its explicit three polynomial columns C_1 g_b, C_1(z-1), C_1, where g_b=b-2z+b^-1z^2.
The coefficient matrix of g_b,z-1,1 in degrees0,1,2 has determinant-1/b.
Its weights are1,2(t-s),(t-s)(t+s-4), all strictly positive in the chosen embedding.
Since the first three rows of multiplication by C_1 have determinant1, the first-three principal minor is

    Delta_b=2 b^-2 (t-s)^2(t+s-4).                    (15)

Set D=aq, U=a^2+q^2 and V=4aq-a^2-q^2.
Direct substitution gives

    a^5 q Delta_b=2(Dt-U)^2(Dt-V).                   (16)

Both Dt-U and Dt-V are algebraic integers.
Define the actual homogeneous evaluations

    F_1=D^h T(U/D)=q^d p(a/q),
    F_2=D^h T(V/D).                                  (17)

They are integers.
Since T is irreducible of degree h>=2, it has no rational root; thus neither evaluation is zero.
Equivalently, F_1 is the full-degree homogeneous original-polynomial evaluation at(a,q), not an omitted leading factor.
Taking every trace-field conjugate in(16) gives

    Norm_F(a^5 q Delta_b)=(-1)^h 2^h F_1^2 F_2,
    Norm_F(Delta_b)=(-1)^h 2^h F_1^2 F_2/(a^(5h)q^h).
                                                                    (18)

This is the exact signed formula, including denominator powers.
A sufficient common denominator for the entries of Q_b is D^2: g_b has coefficients in D^-1 Z, the second weight has denominator D, and the third has denominator D^2, while C_1 has coefficients in Z[t].
Neither D^2 nor a^5q is claimed to be the least denominator.
No numerator integrality survives deletion of their displayed factors.

The nonzero integral floors in(18) are exactly the floors for the two integer evaluations F_1,F_2 (squared for the first).
At b1 both evaluations reduce to T(2), recovering Section3.
For general b they are two explicit trace evaluations, not free extra norm income.
For example the first floor alone, using t_j<2<=s<t, gives

    |T(s)|=(t-s) product_(j>1)(s-t_j)>=D^-h,
    t-s >= D^-h (s+2)^(-(h-1)).                       (19)

Thus the cofinal choice b approaching lambda retains its actual rational-approximation denominator and all h trace places.
The extra evaluation at4-s can be retained as arithmetic input, but no new bound on it or useful uniform gain has been established here.
The calculation rules out only an uncharged minor-norm interpretation, not all multi-evaluation methods.

<a id="signed-average-quantitative-obstruction"></a>
## 8. An order-one false gain in the signed trace average

The first coefficient of C_j is1, so C103's b1 formula gives (Q_j)00=(t_j-1)^2.
Consequently

    R00=(1/h)sum_j(t_j-1)^2
       =[Tr_F(t^2)-2Tr_F(t)+h]/h.                    (20)

Let alpha_1,...,alpha_d be ALL original roots of p and set a_k=(1/d)sum_i alpha_i^k.
The sums are real.
Pairing inverse roots gives the exact identities

    Tr_F(t)/h=2a_1,
    Tr_F(t^2)/h=2+2a_2,
    R00=3+2a_2-4a_1.                                 (21)

Assume d>=55 and lambda<=2.
Every original root has modulus at most2.
Define chi(z)=1 for |z|<=2, chi(z)=2-|z|/2 on2<=|z|<=4, and chi=0 outside radius4.
For k1,2 set phi_k(z)=chi(z) Re(z^k).
This is a real compactly supported test equal to Re(z^k) on every original root and on the unit circle.
Its circle mean is zero.

On the radius4 disk, Re(z^k) has Lipschitz constant at most k4^(k-1), absolute value at most4^k, and chi has Lipschitz constant1/2.
Thus phi_k has Lipschitz constant at most k4^(k-1)+4^k/2, namely3 for k1 and16 for k2.
For two points inside the disk the product estimate proves this directly.
If one point is outside, the segment to the other crosses the radius4 boundary where phi_k=0, giving the same bound; if both are outside both values vanish.
Hence these are GLOBAL Lipschitz constants, not just root-set bounds.

Apply the accepted Pri11 Theorem3.1 interface to the ORIGINAL degree-d polynomial p, the support radius4 and these tests.
All roots are simple by irreducibility in characteristic zero, the polynomial is integral and monic, and log M(p)=m.
With epsilon_d=sqrt(max(log d/d,m/d)), the exact source factor2R+1 is9, yielding

    |a_1|<=27 epsilon_d,
    |a_2|<=144 epsilon_d,
    |R00-3|<=396 epsilon_d.                          (22)

No power substitution or changed minimal field occurs.
Pri11's original analytic proof is inherited only at its accepted statement/applicability scope, exactly as in L168.

For any PSD real symmetric G in the SAME coefficient Gram fiber at width d, F0010's exact maximum gives G00<=M(p)^2=exp(2m).
Since the operator norm of a real symmetric matrix dominates its quadratic value on the unit coordinate vector e0,

    ||R-G||_op>=|R00-G00|
              >=max(0,R00-exp(2m))
              >=max(0,3-396 epsilon_d-exp(2m)).       (23)

The middle bound is valid even when R00<=exp(2m), because the displayed maximum then is zero.
Taking the infimum over the same-symbol PSD fiber proves E.

Now suppose, without asserting existence, that a sequence of Salem inputs has m tending to zero.
Its degrees must tend to infinity by L168's finite bounded-degree positive-height separation: a bounded-degree subsequence would have height m/d bounded below by a positive constant.
Eventually d>=55 and lambda<=2, and epsilon_d tends to zero.
Thus R00 tends to3, the true PSD maximum tends to1, and(23) has lower limit2.
The exact negative inertia h-1 from Section4 cannot be discarded as a perturbation that is o(1) in operator norm while retaining the same circle symbol.

This is deliberately a distance to the FEASIBLE SAME-SYMBOL PSD set.
It is not a lower bound for the largest absolute negative eigenvalue of R, not a distance theorem for the entire unconstrained PSD cone, and not a statement that the h-1 negative directions alone each have fixed size.
Those different claims do not follow from(23).

<a id="actual-column-values-and-costs"></a>
## 9. Actual column values: coefficient conjugation cannot be omitted

There is a useful distinction between vanishing at roots with coefficients held fixed and taking an actual field norm.
The fixed-coefficient C_1(z) vanishes at the d-2 circle roots, but its coefficients must also be conjugated when evaluating conjugates of C_1(lambda).
It is therefore INCORRECT to infer that the latter algebraic number has zero conjugates.
This potential shortcut was rejected during author checking; the exact calculation is as follows.

The unit relation p(lambda)=0 expresses lambda^-1 as an integer polynomial in lambda.
Thus t lies in Z[lambda], and C_1's coefficients in Z[t] show u_k=C_1(lambda)(lambda-1)^k is in Z[lambda].
None is zero, because lambda is not a root of C_1 and lambda is not1.
The involution sigma fixes t and sends lambda to lambda^-1.
For every j>1,

    (lambda^2-t_j lambda+1)
       (lambda^-2-t_j lambda^-1+1)=(t-t_j)^2.

Multiplying gives

    C_1(lambda) C_1(lambda^-1)=T'(t)^2,
    (lambda-1)(lambda^-1-1)=2-t,
    u_k sigma(u_k)=T'(t)^2(2-t)^k.                   (24)

The trace norm of T'(t) is the product of its h actual conjugates, namely(-1)^(h(h-1)/2)disc(T), as follows by pairing the factors t_i-t_j.
Also Norm_F(2-t)=T(2)=p(1).
The complete original-field norm tower therefore yields

    Norm_(K/Q)(u_k)=Norm_F(u_k sigma(u_k))
                   =disc(T)^2 p(1)^k.                (25)

In particular these values are not presumed units or free sources of income: they carry the exact discriminant factor and the old p(1) evaluations, with original degree d.
Let delta=t-2.
Substituting(24) gives the exact cancellation

    u_2 sigma(u_2)+2delta u_1 sigma(u_1)
                  +delta^2 u_0 sigma(u_0)
       =T'(t)^2[delta^2-2delta^2+delta^2]=0.          (26)

At the distinguished embedding the middle relative norm is negative, while at the other embeddings the middle WEIGHT is negative.
All three column values remain nonzero under their genuine field conjugations.
The weights1,2delta,delta^2 are not normalized positive rational weights; even division by their sum(t-1)^2 leaves the sign-changing middle weight.
Therefore this zero profile is outside C9/C12's positive rational field-profile hypotheses.
The comparison fails for this exact reason, not because the actual values vanish.
Replacing u_k by u_k/C_1(lambda) returns exactly the already integral powers(lambda-1)^k: this exact cancellation REMOVES the common discriminant norm income and supplies no extra arithmetic gain or unavoidable new denominator.

<a id="signed-gram-control-and-outcome"></a>
## 10. Exact control, unsuccessful leverage and continuation boundary

For the retained actual quartic p=z^4-z^3-z^2-z+1, one has T(x)=x^2-x-3, h2, disc(T)=13, T(2)=-1 and T'(-2)=-5.
Equations(5),(12) give signed first-three minor norm-4 and

    inertia(S)=(4 positive,1 negative),
    det S=-1690,
    det R=-845/16.

Newton sums of T give sum_j t_j=1 and sum_j t_j^2=7, hence S00=7 and R00=7/2.
This already exceeds the true capacity lambda^2: since lambda^2+lambda^-2=t^2-2=t+1 and t=(1+sqrt13)/2<5/2, one has lambda^2<t+1<7/2.
Thus this ACTUAL input, not a hypothetical limiting family, has a positive same-symbol feasible-distance lower bound7/2-lambda^2.
Every asserted number follows from the displayed quadratic relations, without a numerical run.
Its fixed m>0 and degree4 are not altered.

This round obtains exact signed arithmetic structure and a quantitative obstruction to treating the signed average as almost feasible.
It also evaluates the most direct norm-floor attempt: the primitive third minors recover only the original p(1) income cubed, the trace determinant has exactly the displayed discriminant/evaluation/endpoint factors, and rational cofinal parameters retain the two specified integer evaluations plus their denominators.
The resulting elementary t-2 bound decays with h.
Therefore no uniform positive gap is supplied by these invariants alone in the identified norm-floor use.

A remaining genuinely different question is whether the full signed matrix has additional spectral or arithmetic constraints beyond these explicit factors which can yield a usable bound after every negative direction and normalization is retained.
Another is a joint bound for the two evaluations T(s),T(4-s) strong enough to beat their rational-denominator costs.
Neither is proved here.
Section9 records the actual NONZERO column values, their full discriminant/evaluation norms, and the sign-changing algebraic weights that prevent direct C9/C12 use.
No unchanged rational/totally-positive descent is proposed again.
The unrestricted G0001 target remains open.

<a id="signed-gram-entire-author-freeze"></a>
## 11. Entire bounded-round author freeze

2026-10-14T19:47.
The author freezes the ENTIRE actual account, Statement A--E, Sections1--10, equations(1)--(26), all quantitative/domain/source boundaries, the exact quartic control and the useful rejected coefficient-conjugation shortcut, for separately organized whole review.
Author checking reconstructed the rank-three matrix and all minor signs; first/last triangular selectors and integer gcd; integral trace construction, actual coefficient-basis determinant and its discriminant square; indefinite block congruence and every h>=2 sign; normalized determinant and integer-floor comparison; rational-b homogeneous evaluations and all denominator powers; original-degree Pri11 support/Lipschitz constants and conditional degree escape; same-symbol distance versus unconstrained PSD distance; and nonzero original-field column values with correct coefficient conjugation, signed norms and exact common-factor cancellation.
The inaccurate initial continuation sentence conflating fixed-coefficient circle zeros with field conjugates was corrected BEFORE freeze and its mathematical distinction is fully retained in Section9.
No other proof gap was found by this author check.

The direct inputs remain C103, the exact C_F6 coefficient-Gram maximum, L66, the actual L8 control, Pri11-U001 and L168's finite degree-escape lemma at their stated scopes.
Existing comparison/attribution accounts are not promoted to stronger dependencies.
The whole proof is this author's contribution; root supplied direction and scope requests, not a new proof step.
This freeze is not independent review or Claim adoption.
No native mathematical program, J, new external theorem, source acquisition, uniform Mahler gap or existence of a near-one family is asserted.

## Fixed organization

The entire author-frozen original above is retained, including every signed invariant, paid bound, corrected coefficient-conjugation distinction, actual control, source and contribution account.
This actual fixed artifact awaits a separate noncontributor whole review.
Root contributed to the earlier accepted C103 input but supplied no proof step for this new argument.

## Current assessment
[Selected decision](#decision-current-isolated-whole-review-20261022-m04)

## Assessment history

### Decision initial

The original assessment wording was `proof draft`.
The recorded review description was `under review`.

| Field | Value |
| --- | --- |
| date | 2026-10-14T19:49 |
| status | open |
| reason | Retain the complete signed-trace Gram arithmetic, exact cost comparison and quantitative same-symbol obstruction for separate whole review. These conclusions do not supply an unrestricted Mahler gap or exclude unexamined spectral mechanisms. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--E at their stated Salem, field, width, denominator and hypothetical-sequence domains. |
| argument | [Entire argument](#argument) | All retained constructions, proofs, exact controls, rejected shortcut and source/degree boundaries. |
| dependency | [Accepted Gram family](Yin_C_G0103_v1.md#statement) | Actual scalar coefficient convention and explicit Salem b-parametrized Grams. |
| dependency | [Exact scalar maximum](../ledger/Yin_L_F0005_v1.md#scalar-capacity-finite-sdp) | Original same-symbol PSD maximum M(p)^2, with source inspection limits retained. |
| dependency | [Trace field](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain) | Original reciprocal field degree and integral trace polynomial. |
| dependency | [Trace discriminant mechanism](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-order-index) | Grouped inverse-pair difference formula at actual coefficient-discriminant scope. |
| dependency | [Actual quartic control](../ledger/Yin_L_G0008_v1.md#quartic-projection-obstruction) | Exact irreducible Salem quartic and trace roots. |
| dependency | [Finite discrepancy](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Accepted Theorem3.1 statement/applicability only, original degree and global compact Lipschitz tests. |
| dependency | [Bounded-degree escape](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | Finite positive height separation, with no near-one sequence existence asserted. |

### Decision current-quartic-control-home

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:01 |
| status | proved |
| reason | Select the adopted C213 v2 as the current responsible home of the identical retained L8 quartic control at the exact anchor below. Its actual selected adoption and complete quartic projection section were read, including the exact polynomial, inverse/circle root pattern and trace values; the explicitly selected C206 Section6 supplies the complete modulo-2 irreducibility argument and was read at that scope. Mathematical status, statement, complete argument, selected finding and every relation scope are inherited unchanged; this is current locator maintenance and supplies no new mathematical or independent review. The selected finding now declares unknown initial context, while the older dated decision and its R bindings retain their actual original L8 inputs and fields. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--E at their stated Salem, field, width, denominator and hypothetical-sequence domains. |
| argument | [Entire argument](#argument) | All retained constructions, proofs, exact controls, rejected shortcut and source/degree boundaries. |
| dependency | [Accepted Gram family](Yin_C_G0103_v1.md#statement) | Actual scalar coefficient convention and explicit Salem b-parametrized Grams. |
| dependency | [Exact scalar maximum](../ledger/Yin_L_F0005_v1.md#scalar-capacity-finite-sdp) | Original same-symbol PSD maximum M(p)^2, with source inspection limits retained. |
| dependency | [Trace field](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain) | Original reciprocal field degree and integral trace polynomial. |
| dependency | [Trace discriminant mechanism](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-order-index) | Grouped inverse-pair difference formula at actual coefficient-discriminant scope. |
| dependency | [Actual quartic control](Yin_C_G0213_v2.md#quartic-projection-obstruction) | Exact irreducible Salem quartic and trace roots. |
| dependency | [Finite discrepancy](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Accepted Theorem3.1 statement/applicability only, original degree and global compact Lipschitz tests. |
| dependency | [Bounded-degree escape](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | Finite positive height separation, with no near-one sequence existence asserted. |
| review | [Actual whole finding](../audits/reviews/Yin_R_G0796_v1.md#signed-gram-whole-independent-finding) | Entire actual A--E and argument, all selected direct dependencies, actual field-conjugation correction and exact quantitative/source boundaries. |


### Decision current-haar-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T02:44 |
| status | proved |
| reason | Select the adopted complete C_F6/C_F7/C_F8 responsible homes, as applicable below, for the unchanged retained scalar finite Gram maximum. The actual selected adoptions and complete needed interface sections were read and matched to the original fixed L_F5/L_F6/L_F7 text. Mathematical status, statement, full argument, selected findings and every relation scope remain unchanged; this is current proof-location maintenance with no new mathematical or independent review. Original dated decisions and all R bindings keep their actual old inputs and declarations. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--E at their stated Salem, field, width, denominator and hypothetical-sequence domains. |
| argument | [Entire argument](#argument) | All retained constructions, proofs, exact controls, rejected shortcut and source/degree boundaries. |
| dependency | [Accepted Gram family](Yin_C_G0103_v1.md#statement) | Actual scalar coefficient convention and explicit Salem b-parametrized Grams. |
| dependency | [Exact scalar maximum](Yin_C_F0006_v1.md#scalar-capacity-finite-sdp) | Original same-symbol PSD maximum M(p)^2, with source inspection limits retained. |
| dependency | [Trace field](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain) | Original reciprocal field degree and integral trace polynomial. |
| dependency | [Trace discriminant mechanism](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-order-index) | Grouped inverse-pair difference formula at actual coefficient-discriminant scope. |
| dependency | [Actual quartic control](Yin_C_G0213_v2.md#quartic-projection-obstruction) | Exact irreducible Salem quartic and trace roots. |
| dependency | [Finite discrepancy](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Accepted Theorem3.1 statement/applicability only, original degree and global compact Lipschitz tests. |
| dependency | [Bounded-degree escape](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | Finite positive height separation, with no near-one sequence existence asserted. |
| review | [Actual whole finding](../audits/reviews/Yin_R_G0796_v1.md#signed-gram-whole-independent-finding) | Entire actual A--E and argument, all selected direct dependencies, actual field-conjugation correction and exact quantitative/source boundaries. |

### Decision current-local-trace-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T04:51 |
| status | proved |
| reason | Select C241/C243 as the complete current responsible homes for the identical already used L64 unramified local or L66 reciprocal trace/order/module interfaces at the exact selected anchors below. The full original arguments, current extracted statements and used guards were read; this is same-content locator adoption. Status, selected statement/argument/finding, all relation scopes and every other current proof home remain unchanged. Prior dated decisions and R bindings keep their actual L64/L66 inputs; no new independent review, local assumption, cheaper entropy normalization or stronger arithmetic estimate is claimed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Statement](#statement) | Entire A--E at their stated Salem, field, width, denominator and hypothetical-sequence domains. |
| argument | [Argument](#argument) | All retained constructions, proofs, exact controls, rejected shortcut and source/degree boundaries. |
| dependency | [Dependency](Yin_C_G0103_v1.md#statement) | Actual scalar coefficient convention and explicit Salem b-parametrized Grams. |
| dependency | [Dependency](Yin_C_F0006_v1.md#scalar-capacity-finite-sdp) | Original same-symbol PSD maximum M(p)^2, with source inspection limits retained. |
| dependency | [Dependency](Yin_C_G0243_v1.md#reciprocal-trace-domain) | Original reciprocal field degree and integral trace polynomial. |
| dependency | [Dependency](Yin_C_G0243_v1.md#reciprocal-trace-order-index) | Grouped inverse-pair difference formula at actual coefficient-discriminant scope. |
| dependency | [Dependency](Yin_C_G0213_v2.md#quartic-projection-obstruction) | Exact irreducible Salem quartic and trace roots. |
| dependency | [Dependency](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Accepted Theorem3.1 statement/applicability only, original degree and global compact Lipschitz tests. |
| dependency | [Dependency](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | Finite positive height separation, with no near-one sequence existence asserted. |
| review | [Review](../audits/reviews/Yin_R_G0796_v1.md#signed-gram-whole-independent-finding) | Entire actual A--E and argument, all selected direct dependencies, actual field-conjugation correction and exact quantitative/source boundaries. |


### Decision current-actual-product-proof-homes

| Field | Value |
| --- | --- |
| date | 2026-10-21T16:32 |
| status | proved |
| reason | Select the complete C393/C391 proof homes for exactly the originally used L167/L168 actual-energy, norm-tower, bounded-degree-escape, uniform-budget or finite same-time-income capabilities, after complete proof/interface comparison. Preserve this Claim statement, argument, status, all other input relations and scopes, source depth and existing review coverage. Every old reading retains its actual fixed input; this proof-home decision does not report an earlier review of the later C materials or establish a new isolated relationship. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire A--E at their stated Salem, field, width, denominator and hypothetical-sequence domains. |
| argument | [Exact retained argument](#argument) | All retained constructions, proofs, exact controls, rejected shortcut and source/degree boundaries. |
| dependency | [Exact retained dependency](Yin_C_G0103_v1.md#statement) | Actual scalar coefficient convention and explicit Salem b-parametrized Grams. |
| dependency | [Exact retained dependency](Yin_C_F0006_v1.md#scalar-capacity-finite-sdp) | Original same-symbol PSD maximum M(p)^2, with source inspection limits retained. |
| dependency | [Exact retained dependency](Yin_C_G0243_v1.md#reciprocal-trace-domain) | Original reciprocal field degree and integral trace polynomial. |
| dependency | [Exact retained dependency](Yin_C_G0243_v1.md#reciprocal-trace-order-index) | Grouped inverse-pair difference formula at actual coefficient-discriminant scope. |
| dependency | [Exact retained dependency](Yin_C_G0213_v2.md#quartic-projection-obstruction) | Exact irreducible Salem quartic and trace roots. |
| dependency | [Exact retained dependency](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Accepted Theorem3.1 statement/applicability only, original degree and global compact Lipschitz tests. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#bounded-power-degree-escape) | Finite positive height separation, with no near-one sequence existence asserted. |
| review | [Exact retained review](../audits/reviews/Yin_R_G0796_v1.md#signed-gram-whole-independent-finding) | Entire actual A--E and argument, all selected direct dependencies, actual field-conjugation correction and exact quantitative/source boundaries. |

### Decision current-isolated-whole-review-20261022-m04

| Field | Value |
| --- | --- |
| date | 2026-10-22T23:29 |
| status | proved |
| reason | Adopt the current isolated whole statement/argument review in R796 after direct mathematical initial judgment and subsequent complete comparison of the original findings. The new finding is independently reviewed and the complete superseded original account retains its actual unknown relationship, date, bindings, source depth and limitations in that R. Preserve the exact statement, complete argument, proved status, every selected support/dependency and its scope, all prior decisions and all fixed mathematics. No historical relationship is promoted, original external proof or native computation is newly certified, unrestricted coverage or Task completion is inferred, or stopped research resumed. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact retained statement](#statement) | Entire A--E at their stated Salem, field, width, denominator and hypothetical-sequence domains. |
| argument | [Exact retained argument](#argument) | All retained constructions, proofs, exact controls, rejected shortcut and source/degree boundaries. |
| dependency | [Exact retained dependency](Yin_C_G0103_v1.md#statement) | Actual scalar coefficient convention and explicit Salem b-parametrized Grams. |
| dependency | [Exact retained dependency](Yin_C_F0006_v1.md#scalar-capacity-finite-sdp) | Original same-symbol PSD maximum M(p)^2, with source inspection limits retained. |
| dependency | [Exact retained dependency](Yin_C_G0243_v1.md#reciprocal-trace-domain) | Original reciprocal field degree and integral trace polynomial. |
| dependency | [Exact retained dependency](Yin_C_G0243_v1.md#reciprocal-trace-order-index) | Grouped inverse-pair difference formula at actual coefficient-discriminant scope. |
| dependency | [Exact retained dependency](Yin_C_G0213_v2.md#quartic-projection-obstruction) | Exact irreducible Salem quartic and trace roots. |
| dependency | [Exact retained dependency](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Accepted Theorem3.1 statement/applicability only, original degree and global compact Lipschitz tests. |
| dependency | [Exact retained dependency](Yin_C_G0391_v1.md#bounded-power-degree-escape) | Finite positive height separation, with no near-one sequence existence asserted. |
| review | [Current isolated whole finding](../audits/reviews/Yin_R_G0796_v1.md#fresh-c0107-whole-finding) | Entire exact current statement and complete retained argument, every finite/conditional/asymptotic scope, decisive direct input interfaces, controls, original arithmetic costs and source/negative/execution limitations. Current isolated whole review after fixed-input initial judgment, with complete original unknown account preserved separately in the same R; no mathematical repair or scope enlargement. |

## Historical assessments

<a id="decision-whole-reviewed-2026-10-15"></a>

### Historical assessment whole-reviewed-2026-10-15

| Field | Value |
| --- | --- |
| date | 2026-10-14T19:56 |
| status | proved |
| review-status | independently reviewed |
| reason | Adopt [R796 original signed-Gram](../audits/reviews/Yin_R_G0796_v1.md#signed-gram-whole-independent-finding)'s independent whole review of actual A--E, the entire retained argument and every direct input. Exact signed invariants, their paid norm/denominator costs, actual nonzero column values and the quantitative same-symbol PSD-distance obstruction are established at their stated Salem scope. No general spectral impossibility or unrestricted Mahler gap is inferred. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Entire A--E at their stated Salem, field, width, denominator and hypothetical-sequence domains. |
| argument | [Entire argument](#argument) | All retained constructions, proofs, exact controls, rejected shortcut and source/degree boundaries. |
| dependency | [Accepted Gram family](Yin_C_G0103_v1.md#statement) | Actual scalar coefficient convention and explicit Salem b-parametrized Grams. |
| dependency | [Exact scalar maximum](../ledger/Yin_L_F0005_v1.md#scalar-capacity-finite-sdp) | Original same-symbol PSD maximum M(p)^2, with source inspection limits retained. |
| dependency | [Trace field](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-domain) | Original reciprocal field degree and integral trace polynomial. |
| dependency | [Trace discriminant mechanism](../ledger/Yin_L_G0066_v1.md#reciprocal-trace-order-index) | Grouped inverse-pair difference formula at actual coefficient-discriminant scope. |
| dependency | [Actual quartic control](../ledger/Yin_L_G0008_v1.md#quartic-projection-obstruction) | Exact irreducible Salem quartic and trace roots. |
| dependency | [Finite discrepancy](../audits/literature/Pri11/Yin_U001.md#pri11-u001) | Accepted Theorem3.1 statement/applicability only, original degree and global compact Lipschitz tests. |
| dependency | [Bounded-degree escape](../ledger/Yin_L_G0168_v1.md#bounded-power-degree-escape) | Finite positive height separation, with no near-one sequence existence asserted. |
| review | [Actual whole independent finding](../audits/reviews/Yin_R_G0796_v1.md#signed-gram-whole-independent-finding) | Entire actual A--E and argument, all selected direct dependencies, actual field-conjugation correction and exact quantitative/source boundaries. |
