---
author: Yin
---
# Complete centered edge differentiation with full norm, coefficient and root costs

This retains all original L253 arguments and useful finite/negative findings, with the consumed actual centered construction and quadratic all-circle proof explicit below.
Original L253/L249 exploration, source attributions and fixed old review inputs remain available.
No Task/E execution resumes.

## Statement

Let P in Z[t] be monic, irreducible, reciprocal and nontorsion, with degree d=2s>=2 and constant coefficient1; let alpha_1,...,alpha_d be all original roots.
For every integer j>=d-1 set N=2j+1,D=d-1 and let R_j=t^j-Proj_(V_j)t^j in the real Euclidean coefficient space of degree at most2j, where V_j consists of all P U with deg U<=2j-d.
Clear the rational coefficients of R_j and divide by their positive coefficient gcd to obtain the actual primitive integer F=q R_j.
Then q is a positive integer, F(alpha_i)=q alpha_i^j, and unique edge polynomials A,B in Z[t] satisfy

    P F=A+t^N B, deg A,deg B<=D,
    B(t)=t^D A(1/t).

Let S_2(f) be the square root of the sum of squared coefficients, and define

    Z=t(A'B-AB')-NAB,
    c=content(Z)>0, Z_0=Z/c.

Then Z is integral of degree at most2d-2 and nonzero at every original conjugate, with

    Z=tB(PF)'-(NB+tB')PF,
    Z(alpha_i)=q alpha_i^(j+1)P'(alpha_i)B(alpha_i),
    |Res(P,Z)|=q^d |Disc(P)| |Res(P,A)|.

For every rational prime p and every original p-adic root, normalized by v_p(p)=1,

    v_p(Z(alpha_i))=v_p(q)+v_p(P'(alpha_i))+v_p(B(alpha_i)).

Every depth is finite and nonnegative, including ramified/discriminant primes.
Primitive normalization exactly preserves the complete normalized margin7, and the full weighted middle/extreme coefficient identities8--10 and cost inequality11 hold with no omitted monomial or leading coefficient.
More explicitly, writing A=sum_(k=0)^D a_k t^k, b=min{k:a_k!=0}, h=max{k:a_k!=0}, one has h>b,

    [t^D]Z=-sum_(k=0)^D(N+D-2k)a_k^2,
    S_2(Z)>=(N-D)S_2(A)^2,
    [t^(D+h-b)]Z=-(N+D-h-b)a_h a_b !=0.

The actual lowest exponent is D+b-h; removing only this monomial leaves a reciprocal part of degree2(h-b) whose complete leading and exterior-root Mahler costs remain charged.

For every integer a>=3 and every j>=1, use the actual quadratic input P_a=t^2-a t+1, alpha=(a+sqrt(a^2-4))/2, Delta=a^2-4 and g=gcd(2,a), with C_k=alpha^k+alpha^(-k), H=2+sum_(k=1)^j C_k^2 and q=H/g.
Its genuine centered F is given exactly by12 and all its2j roots are simple and on the circle.
Its compressed Z=u(1+t^2)+vt and lambda=qDelta/g satisfy the full formulas13--14 and

    log|Res(P_a,Z_0)|/2-log S_2(Z_0)
        =log lambda-(1/2)log(2u^2+v^2)<0.

For every fixed a, the exact normalized margin plus log N tends to

    log[(alpha^2-1)/sqrt(alpha^4+4alpha^2+1)]<0.

The compressed primitive polynomial has precisely two simple positive reciprocal roots beta_j,beta_j^-1, with1<beta_j<alpha and beta_j tending to alpha, and its full measure is log(u/c)+log beta_j.
Growing or oscillating content does not remove these costs or the log N loss.

The original eighteen declared finite cases comprise a=3,4,5 with j=1,2,4, and P4=t^4-t^3-t^2-t+1, P6=t^6-t^5-t^3-t+1 and the original Lehmer polynomial t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1 at j=d-1,d,2d-1.
Their exact full resultant-minus-S2 signs are strictly negative with all complete coefficients/degrees/content/norms retained in J56.
The nine higher-degree cases supply finite evidence only: no general higher-degree negativity, new root isolation, optimized content/cost, varying near-one coverage or unrestricted Mahler gap is proved.

<a id="argument"></a>
## Complete argument

### Consumed exact centered projection and edge construction

All notation is the actual original coefficient projection from L249; the local equation numbers in these consumed subsections are separate from the original Sections1--6/equations1--17 below.

Choose an integer j>=s, let N=2j+1, and use the real Euclidean coefficient space of all polynomials of degree at most2j.
Its inner product is sum of products of corresponding coefficients.
Define

    V_j={P U: U in R[t], deg U<=2j-d},
    R_j(t)=t^j-Proj_(V_j)(t^j),
    l_j=||R_j||_2^2.                                 (2)

This is the same actual relation-space projection used by the retained work, at the specified centered window.
Its Gram matrix is rational and nonsingular, so R_j has rational coefficients.
R_j is nonzero because it takes the exact nonzero values

    R_j(alpha_i)=alpha_i^j   for every original i.

The orthogonal decomposition also gives l_j=(R_j)_j, its central coefficient, and0<l_j<=1.

Reversal of2j+1 coefficients is an orthogonal involution.
Since P is reciprocal, it preserves V_j and fixes t^j; it therefore fixes R_j.
Reflection here is with respect to the entire declared window, even if the outer coefficients of R_j vanish.
It does not assert that the actual degree is2j.

There is also an exact coefficient-boundary identity.
For k=d,...,2j, the coefficient of t^k in P(t)R_j(t) equals the inner product of R_j with t^(k-d)P, because P is reciprocal.
Every one of these coefficients vanishes by(2).
Thus

    P(t)R_j(t)=A_j(t)+t^N B_j(t),
    deg A_j,deg B_j<=d-1,
    B_j(t)=t^(d-1) A_j(t^(-1)).                      (4)

The last equality uses formal reversal of total degree2j+d=N+d-1 and remains valid when outer coefficients vanish.
In particular the FULL coefficient product has an empty band from degree d through2j.
This identity concerns one specific optimal column, not an arbitrary small-energy representative or a deletion of middle coefficients after evaluation.

For j>=d-1, l_j<1.
Otherwise the projection vanishes and t^j is perpendicular to all the displayed shifts of P.
At j=d-1 those inner products see every interior coefficient p_1,...,p_(d-1); at any j>=d one of them sees p_0=1.
The interior coefficients cannot all vanish, since then P=t^d+1 would be torsion.
This establishes strictness on the range used for the root-count corollary, without asserting a uniform distance of l_j from one.

Take j>=d-1.
Choose a positive integer L_den clearing the coefficients of R_j, let c_F be the positive gcd of all coefficients of L_den R_j, and put

    F_j=(L_den/c_F)R_j,       q=L_den/c_F.

The polynomial F_j is primitive and integral.
Since F_j(alpha)=q alpha^j and alpha is an algebraic unit, q=F_j(alpha)alpha^(-j) is a rational algebraic integer.
Thus q is a positive INTEGER; content division does not leave an uncharged rational scalar.
The exact identities are

    F_j(alpha_i)=q alpha_i^j  for every i,
    |Res(P,F_j)|=q^d,
    S_2(F_j)^2=q^2 l_j,
    log q-log S_2(F_j)=-(1/2)log l_j>0.              (8)

Here q>=2, since q=1 would give a nonzero integral polynomial with S_2<1.
F_j is not a constant or monomial: a primitive integer monomial has coefficient+1 or-1, so its value equation would make a power of the algebraic unit alpha equal to+q or-q, a rational algebraic unit.
The only rational algebraic units are+1 and-1, contradicting q>=2.
If b_F is the first nonzero exponent of R_j, reversal through the full2j window makes its last exponent2j-b_F.
Thus F_j has full actual degree2j-b_F; this b_F is distinct from the later first exponent of the edge polynomial A.
Monic division also gives F_j-q t^j in P Z[t], because this integral difference vanishes at alpha; the congruence therefore holds in the actual order.
For every rational prime p, every original p-adic root has exactly v_p(q) valuation in F_j(alpha_i), since alpha_i is a unit.
All roots, powers and primes in this one norm are retained.
There is no dyadic-denominator claim, and no guarantee that the selected center enjoys the uniform margin of L237's separately selected column.

### Consumed full quadratic centered construction and circle-root proof

Fix an integer a>=3 and take the actual reciprocal unit input

    P_a(t)=t^2-a t+1,
    alpha=(a+sqrt(a^2-4))/2>1.

The discriminant a^2-4 lies strictly between(a-1)^2 and a^2, so P_a is irreducible over Q.
Its roots are alpha and alpha^(-1), and its total measure is the FIXED positive log alpha.
Here s=1,r=0.
For every j>=1 define integer C_k=C_k(a)=alpha^k+alpha^(-k), using C_0=2,C_1=a and the explicit recurrence C_(k+1)=a C_k-C_(k-1).
Put

    H=2+sum_(k=1)^j C_k^2,
    g=gcd(2,a) in{1,2},
    F_j(t)=[2t^j+sum_(k=1)^j C_k(t^(j+k)+t^(j-k))]/g,
    q=H/g.                                         (11)

These are exactly the primitive centered residual auxiliaries, not merely other polynomials with similar roots.
To verify this, a symmetric real coefficient polynomial has the form t^j(c_0+sum_(k=1)^j c_k(t^k+t^(-k))).
Its norm squared is c_0^2+2sum c_k^2.
Prescribing its value alpha^j at alpha gives c_0+sum c_k C_k=1; reciprocity gives the correct value at alpha^(-1) as well.
The unique minimum of that quadratic norm under the linear condition, by Cauchy--Schwarz with its equality condition, is attained at

    c_0=2/H,       c_k=C_k/H,
    l_j=2/H.                                       (12)

Among all nonsymmetric feasible polynomials, averaging with reversal preserves feasibility and cannot increase the norm.
The actual residual is the unique minimum-norm polynomial with those two values, so it is precisely(12).
This is the single-column instance of the retained projection principle, applied here to compute an exact control.

The coefficient gcd of the numerator in(11) is exactly g: it divides both2 and C_1=a, and the recurrence makes every C_k even when a is even.
Thus(11) is primitive, q is integral, its full degree is2j, and its leading/constant coefficient is C_j/g.
For x=t+t^(-1), write R_j=t^j L_j(x); its degree is exactly j because C_j/H is nonzero.
For every real polynomial V of degree at most j-1, P_a(t)t^(j-1)V(x) belongs to the relation space.
Coefficient orthogonality, expressed as a circle integral and then x=2cos(theta), gives integral L_j(x)V(x)(a-x)dx/[pi sqrt(4-x^2)]=0 on(-2,2).
The weight is strictly positive and integrable because a>=3.
If L_j had fewer than j sign-changing interval zeros, multiply the corresponding distinct linear factors to form V of degree less than j; L_j V has constant nonzero sign except at finitely many zeros, contradicting that zero integral.
Thus degree j supplies exactly j simple roots in(-2,2), giving all2j roots of F_j simple and on the unit circle.
The full exact quantities are

    M(F_j)=C_j/g,
    Res(P_a,F_j)=q^2,
    S_2(F_j)^2=2H/g^2,
    log q-log S_2(F_j)=(1/2)log(H/2).                (13)

For example a=3,j=1 gives the exact primitive F_1=3t^2+2t+3, q=11, l_1=2/11, M(F_1)=3, S_2(F_1)^2=22 and Res(P_3,F_1)=121.
These roots are not roots of unity: the primitive quadratic is irreducible by its negative discriminant, and a root of unity would have monic integral minimal polynomial, contrary to this irreducible primitive nonmonic polynomial.
Thus even an auxiliary whose ENTIRE root set is on the circle can carry positive Mahler cost in its leading coefficient.

As j tends to infinity at this fixed input, C_j=alpha^j+alpha^(-j) gives

    m(F_j)/j ->log alpha,
    (log q)/j ->2log alpha,
    [log q-log S_2(F_j)]/j ->log alpha.              (14)

For the middle limit use C_j^2<=H and H<=2+4sum_(k=1)^j alpha^(2k), both with fixed alpha>1; the other limits follow from(13).
The original degree remains2 and the auxiliary degree is2j, so this control is not a degree-linear near-one family.
It decisively prevents treating the original general L249 circle-root count as a bound for the full Mahler cost or as a collection of free cyclotomic factors.
No uniformity as total m tends to zero is inferred.

<a id="edge-derivative-reuse-and-scope"></a>
### 1. Changed object, reuse and declared finite pilot

The arithmetic agent develops this argument independently; root supplied the broad question and the J allocation, not a mathematical step.
Root's separate conditional-projection and quotient-geometry argument is not an input and is not pursued here.

Reuse [L249's complete actual centered column](../ledger/Yin_L_G0249_v1.md#centered-column-fixed-scope), its primitive normalization and full reciprocal edge identity, [L56's projection principle](../ledger/Yin_L_G0056_v1.md#unique-minimum-lift), [L237's separate universal scalar margin](../ledger/Yin_L_G0237_v1.md#monomial-projection-uniform-margin), and [L245's full-space positive-weight boundary](../ledger/Yin_L_G0245_v1.md#root-weight-quadratic-fixed-scope).
The fixed-input [L101 endpoint limit](../ledger/Yin_L_G0101_v1.md#endpoint-row-hardy-closure) and [L139 seed theorem](../ledger/Yin_L_G0139_v1.md#varying-seed-uniform-factor-gap) were checked; neither supplies an input-uniform leading coefficient estimate for the present center.
The old L56/L241 reuse correction is preserved.
A bounded local search of the G ledgers and source registry for centered edges, Bezout/derivative identities, reciprocal Wronskians, orthogonal-polynomial and root-location interfaces found no retained version of the compression and complete-cost test developed below.
This is a bounded screen, not a novelty assertion.
The derivative steps are direct polynomial calculations, rather than an invoked uninspected differential or zero-location theorem.
The full product-of-original-roots resultant and discriminant conventions are the retained ones in [L4](../ledger/Yin_L_G0004_v1.md); the needed derivative product is displayed explicitly below.
L249's Nat26 related attribution and accepted Kronecker interface keep their prior scopes; no new external theorem is adopted.

The new object is a differentiated FULL edge product.
Its degree is bounded by the original degree even when the original auxiliary window grows, but its exact middle and leading coefficients charge the window.
This is a different auxiliary, not an optimization of the old coefficient basis or another circle-zero count.

A finite author pilot is declared before execution in [J56](../computations/programs/Yin_J_G0056/readme.md), with a120-second cap.
It will reconstruct the actual centered projection over Q, without supplied output coefficients, for the retained quartic t^4-t^3-t^2-t+1, degree-six t^6-t^5-t^3-t+1 and original Lehmer polynomial t^10+t^9-t^7-t^6-t^5-t^4-t^3+t+1, at j=d-1,d,2d-1.
The exact quadratic controls a=3,4,5 at j=1,2,4 are included.
This is eighteen explicitly specified inputs/windows, with no expansion of the box.
It checks the polynomial identities, actual degrees and content, all-root remainders, full resultants, squared coefficient costs and exact sign of normalized norm-minus-energy.
No decimal Mahler value or empirical all-input conclusion is a premise.
Programs and outputs remain in J56; the general proof and all-j control belong here.

<a id="edge-derivative-complete-norm"></a>
### 2. A derivative auxiliary with bounded original-degree cost

Let P be monic irreducible reciprocal nontorsion of degree d=2s, with constant coefficient1.
Use its actual L249 centered primitive auxiliary F=q R_j, j>=d-1, N=2j+1, and put D=d-1.
Thus q is a positive integer, F(alpha_i)=q alpha_i^j for ALL original roots, and

    P F=A+t^N B,  B=t^D A(1/t),
    A,B in Z[t], deg A,deg B<=D.                    (1)

A is nonzero and primitive.
Indeed P and F are primitive, and the polynomial product is primitive by the usual coefficient-content identity; alternatively reduction modulo any prime shows the product of two nonzero polynomials remains nonzero.
The two disjoint edge blocks in(1) have the same coefficient content, which proves the assertion for A and B without an extra scalar assumption.
Neither has a common root with P, since they are nonzero of degree less than d and P is irreducible.

Define the genuine integral polynomial

    Z=t(A'B-A B')-N A B.                             (2)

A direct product differentiation gives the entire identity

    Z=t B(P F)'-(N B+t B')P F.                       (3)

This verifies the cancellation of every high-degree term; no middle coefficients are deleted by hand.
In particular deg Z<=2D=2d-2, and at every original root

    Z(alpha_i)=q alpha_i^(j+1) P'(alpha_i) B(alpha_i).
                                                            (4)

P is separable, every alpha_i is a unit and B(alpha_i) is nonzero, so Z is nonzero at every original root.
Its complete resultant satisfies

    |Res(P,Z)|=q^d |Disc(P)| |Res(P,B)|
              =q^d |Disc(P)| |Res(P,A)|.             (5)

The last equality follows by inversion permuting the original roots and product_i alpha_i=1.
The discriminant equality is absolute: the usual sign between Res(P,P') and Disc(P) is not silently removed from a signed formula.
For every rational prime p and every original p-adic root, normalized by v_p(p)=1, (4) gives exactly

    v_p(Z(alpha_i))=v_p(q)+v_p(P'(alpha_i))
                                      +v_p(B(alpha_i)).       (6)

Every term is finite and nonnegative.
This accounts for repeated reductions and discriminant/index primes; no good-prime or squarefree-reduction hypothesis is inserted.
The extra norm factors in(5) are actual whole norms, not a free independent income without their coefficient cost.

If c is the positive coefficient gcd of Z, put Z_0=Z/c.
Then its norm is the full norm in(5) divided by c^d and its squared coefficient norm is S_2(Z)^2/c^2.
In particular the net normalized quantity is exactly invariant under this primitive normalization:

    log|Res(P,Z_0)|/d-log S_2(Z_0)
       =log q+[log|Disc(P)|+log|Res(P,A)|]/d
                                                  -log S_2(Z). (7)

No upper bound for c can be replaced by its numerical value on a control.
This identity keeps the full content cost even if c removes some or all of the apparent new divisibility.

<a id="edge-derivative-middle-leading-cost"></a>
### 3. Exact middle and leading expenses

Write A=sum_(k=0)^D a_k t^k, let b=min{k:a_k!=0} and h=max{k:a_k!=0}.
Formal reversal in(2) gives Z=t^(2D)Z(1/t).
Coefficient multiplication, including the differentiated indices, gives

    [t^D]Z=-sum_(k=0)^D (N+D-2k)a_k^2,
    |[t^D]Z|>=(N-D)S_2(A)^2>0.                    (8)

All weights are positive because N>=2d-1>D.
Thus the short-degree compression retains a forced coefficient expense proportional to the original window; in particular

    S_2(Z)>=(N-D)S_2(A)^2.                          (9)

The extreme exponents of A B are D+b-h and D+h-b.
At the upper one the sole term of(2) is

    [t^(D+h-b)]Z=-(N+D-h-b)a_h a_b.                (10)

Its factor is strictly positive, since h+b<=2D<N+D.
Formal reversal supplies the same lower coefficient.
Therefore the displayed extremes are the ACTUAL first and last exponents of Z, not just bounds.
Removing the monomial t^(D+b-h) leaves a reciprocal polynomial of degree2(h-b), with nonzero leading/constant coefficient given in(10).

In the present nontorsion domain h>b.
Otherwise A=a_b t^b and(1) would read P F=a_b t^b[1+t^(N+D-2b)].
Its exponent is positive because N>D and b<=D, forcing every root of P to be a root of unity, a contradiction.
Hence the primitive Z_0 has a nonconstant reciprocal part.
Removing its monomial changes neither Mahler measure nor the absolute resultant against the unit P.
Its leading coefficient is(10)/c, and the Mahler cost includes its absolute logarithm together with ALL exterior roots of this reciprocal part.
No circle-root count for F is automatically a root-location theorem for Z.

Combining(7),(9) gives the fully charged necessary comparison

    log|Res(P,Z_0)|/d-log S_2(Z_0)
       <=log q+[log|Disc(P)|+log|Res(P,A)|]/d
                         -log(N-D)-2log S_2(A).    (11)

This is a cost bound for one actual polynomial, not a near-one estimate for its sign.
It identifies precisely what an apparent low-degree derivative gain must overcome.
The new norm, original discriminant, edge norm and edge height cannot be optimized independently.


<a id="quadratic-compression-all-window-obstruction"></a>
### 4. An all-window actual control: compression destroys the scalar margin

Fix an integer a>=3 and the actual irreducible unit input P_a=t^2-a t+1.
Let alpha=(a+sqrt(a^2-4))/2>1, Delta=a^2-4, g=gcd(2,a), and reuse the exact L249 centered construction for every j>=1:

    C_k=alpha^k+alpha^(-k),
    H=2+sum_(k=1)^j C_k^2,  q=H/g,
    F=[2t^j+sum_(k=1)^j C_k(t^(j+k)+t^(j-k))]/g.    (12)

The original F is primitive, all its2j roots are simple and on the unit circle, and its scalar-minus-coefficient margin is(1/2)log(H/2)>0.
These facts and the fixed original measure log alpha are reuse from L249, not another new construction or a small-measure family.

Put X=C_j, Y=C_(j+1), N=2j+1.
Direct multiplication with P_a gives the actual edge polynomials

    A=(X-Yt)/g, B=(-Y+Xt)/g,
    Res(P_a,A)=Res(P_a,B)=-Delta/g^2.               (13)

The middle gap is the retained one; the two displayed low coefficients also follow from C_(j+1)=a C_j-C_(j-1).
The norm calculation uses X^2+Y^2-aXY=-Delta.
Both sides of this last identity follow by expanding alpha^k+alpha^(-k) and alpha+alpha^(-1)=a.
Thus the edge norms in this family stay fixed although their coefficients grow.

The derivative polynomial is the FULL trinomial

    Z=u(1+t^2)+v t,
    u=NXY/g^2>0,
    v=[Y^2-X^2-N(X^2+Y^2)]/g^2,
    Z(alpha)=lambda alpha,
    lambda=a u+v=[Y^2-X^2+N Delta]/g^2
                         =Delta H/g^2=q Delta/g>0. (14)

The last equality keeps the full sum H, not just its largest term.
To verify it at every j, the identity Y^2-X^2+N Delta=Delta H holds at j=0, where C_0=2 and H=2.
On advancing j by one, the change in Y^2-X^2 is Delta(C_(j+1)^2-2), by the recurrence and X^2+Y^2-aXY=-Delta; the change2Delta in N Delta supplies the missing term.
The total change is therefore Delta C_(j+1)^2, exactly that in Delta H.
No divisibility or asymptotic approximation substitutes for this equality.
Integrality of u,v,lambda also follows from the actual integer polynomials; the displayed quotients retain g.

There is a strict cost obstruction for this entire infinite family:

    log|Res(P_a,Z_0)|/2-log S_2(Z_0)
        =log lambda-(1/2)log(2u^2+v^2)<0
                        for EVERY a>=3,j>=1.        (15)

Here Z_0=Z/content(Z); no formula or boundedness assertion about that content is needed.
For a direct proof put T=X^2+Y^2 and E=Y^2-X^2.
The numbers C_k increase for k>=0, so E>0 and E<T.
Furthermore

    T>=a^2+(a^2-2)^2>3(a^2-4)=3Delta,

since the difference is(a^2-3)^2+7.
Equation(14) gives v=(E-NT)/g^2<0 and lambda=(E+NDelta)/g^2>0.
Consequently

    |v|-lambda=[N(T-Delta)-2E]/g^2
       >[(N-2)T-NDelta]/g^2
       >[3(N-2)-N]Delta/g^2>=0,

because N>=3.
In particular lambda<|v|<sqrt(2u^2+v^2), proving(15).
The primitive content cancels exactly from the comparison as in(7).
Thus the apparent discriminant and edge-norm income, even after being fully retained, is smaller than the cost of ONE actual coefficient.
This is not merely an example where a guessed content denominator went wrong.

The loss has a precise fixed-input rate.
With a fixed and j tending to infinity,

    [log|Res(P_a,Z_0)|/2-log S_2(Z_0)]+log N
       ->log[(alpha^2-1)/sqrt(alpha^4+4alpha^2+1)]<0. (16)

Indeed X/alpha^j and Y/alpha^(j+1) tend to1, while the geometric sums in(12) give H/alpha^(2j)->alpha^2/(alpha^2-1).
Thus lambda/alpha^(2j)->(alpha^2-1)/g^2, u/(N alpha^(2j))->alpha/g^2 and v/(N alpha^(2j))->-(1+alpha^2)/g^2.
Dividing the exact ratio in(15) proves(16).
The statement is unchanged by arbitrarily large or oscillating coefficient content.
It concerns a fixed positive original measure and unbounded j; it is not uniform as a varying input approaches measure one.

The compressed auxiliary also reintroduces actual exterior roots that the original F did not have.
Let r=Y/X.
The explicit expression

    r=alpha[1+alpha^(-2j-2)]/[1+alpha^(-2j)]

increases in j, so r>=C_2/C_1=a-2/a>=7/3.
The trace of Z's reciprocal roots is

    tau=-v/u=(1-1/N)r+(1+1/N)/r.

For r>1 this is increasing in N.
At N>=3 it is at least(2r+4/r)/3, which is increasing for r>=7/3 and equals134/63>2 at that endpoint.
Equation(14) also gives tau=a-lambda/u<a.
Hence Z_0 has exactly two simple positive reciprocal nonzero roots beta_j,beta_j^(-1), with

    1<beta_j<alpha, beta_j->alpha,
    m(Z_0)=log(u/content(Z))+log beta_j.             (17)

Both terms in this Mahler formula are present; u/content(Z) is a positive integer.
The convergence follows from tau->a and the continuous larger quadratic root.
The original all-circle root count for F therefore does not survive this derivative operation.
It returns an expanding root tending to the original one, and it loses the positive scalar margin at rate log N.
Neither fact rules out a different auxiliary operation on near-one inputs.

For the smallest exact instance a=3,j=1, F=3t^2+2t+3 and q=11 as in L249, while A=3-7t and

    Z=63t^2-134t+63, content(Z)=1,
    lambda=55, |Res(P_a,Z)|=3025,
    S_2(Z)^2=25894.

This is a direct substitution in(12)--(14), independently reproduced by the pilot, not a fitted certificate.

<a id="edge-derivative-exact-pilot"></a>
### 5. Completed exact pilot and its finite scope

The declared [J56 author program](../computations/programs/Yin_J_G0056/verify.py) completed all eighteen cases within the120-second cap.
Its retained complete output (`mathematics/computations/outputs/Yin_J_G0056/verification.json`) reports success for every exact check.
It constructs the relation matrix from the input coefficients, solves the rational projection, clears the actual coefficient gcd, and obtains F,q,A,B,Z and Z_0 from those computed objects.
Expected coefficient lists or resultants are not supplied to the reconstruction.

The checks cover the full gap identity, both expressions(2),(3), exact original-order remainder(4), primitive F and A, all actual first/last degrees, the complete middle and leading coefficients, the full signed resultants and discriminants, content scaling and every squared coefficient norm.
The sign test compares the integers |Res(P,Z_0)|^2 and S_2(Z_0)^(2d), so there is no floating-point margin sign.
All eighteen net margins are STRICTLY NEGATIVE.
The quadratic cases are controls of the all-j proof above; the other nine are only finite actual-input evidence.

For the three higher-degree inputs, the complete primitive degrees and contents are:

| Input | j values in order | actual degree of Z_0 | contents of Z in order |
| --- | --- | --- | --- |
| Quartic t^4-t^3-t^2-t+1 | 3,4,7 | 6,6,6 | 2,2,1 |
| Degree-six t^6-t^5-t^3-t+1 | 5,6,11 | 10,10,10 | 2,2,2 |
| Original Lehmer input | 9,10,19 | 18,18,18 | 2,1,1 |

Their actual irreducible Salem status and fixed positive measure are retained respectively in [L169](../ledger/Yin_L_G0169_v1.md#quartic-infinite-core-theorem), [L200](../ledger/Yin_L_G0200_v1.md#degree-six-principal-saturation-fixed-scope), and [L170](../ledger/Yin_L_G0170_v1.md).
The pilot does not reprove those classifications, isolate any new roots, compute a certified decimal measure, or establish a varying-degree or near-one statement.
It checks exact algebraic quantities on the already identified polynomials.
Its program is an author verification, not a separately organized noncontributor review.
The retained formulas, full output and actual executed scope remain in J56 for later replay.

<a id="edge-derivative-boundary-and-open-test"></a>
### 6. What changed and what remains open

The changed mathematical object is an actual bounded-degree derivative auxiliary with the exact complete norm(5) and rootwise valuations(6), including a possible large primitive content.
Its degree bound does not depend on the original centered window.
The countervailing expense is structural: its central coefficient is the negative weighted edge energy(8), its true leading coefficient has the explicit window factor(10), and its primitive normalization does not alter the arithmetic-minus-S2 margin.
This is new information about the edge operation, not a repeat of L249's original root count or L56's projection optimization.

The all-window quadratic theorem proves that this particular compression cannot turn L249's successful scalar margin into a positive margin there.
It even recreates a positive reciprocal exterior pair from an original all-circle auxiliary.
The full higher-degree pilot is compatible with the tentative conjecture that(7) is never positive for this centered derivative construction, but eighteen cases and the quadratic proof do NOT establish that conjecture on all reciprocal inputs.
No claim of universal negativity or near-one failure is adopted.
Conversely no positive higher-degree example has been found within the declared pilot, and enlarging its box blindly is not the selected next step.

A discriminating continuation would prove a general constraint coupling q, Disc(P), Res(P,A) and S_2(A), or find an actual input where their full coupling beats the coefficient expense rather than counting the norm factors separately.
The original center's leading coefficient and its bounded number of exceptional root slots remain an alternative, as do genuinely different signed or nonlinear edge operations.
L237 still proves all-input primitive linear-degree auxiliaries with uniform positive scalar margin; this derivative experiment neither replaces nor weakens that result.
Any route from one of these statements to a gap still needs an input-uniform estimate on a degree-linear near-one family with all original root, content, norm, support and radial costs.
The unrestricted G0001 goal remains unresolved.

## Current assessment
[Selected decision](#decision-complete-isolated-whole-r800-adoption)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:13 |
| status | open |
| reason | Retain the full centered derivative theorem, every original norm/prime-depth/coefficient/content/root/cost argument, exact quadratic all-window negative and original eighteen finite cases with all required actual-centered interfaces for whole checking. No new higher-degree classification, scan, source theorem or Task execution is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Full exact theorem](Yin_C_G0423_v1.md#statement) | All reciprocal nontorsion original P and integer j>=d-1, every prime/root and primitive content, complete quadratic a>=3/j>=1 control, fixed-input limits and eighteen finite-case boundaries. |
| argument | [Complete proof](Yin_C_G0423_v1.md#argument) | Full actual centered/primitive/missing-band/quadratic-circle input and original Sections1--6/equations1--17; complete signed/absolute norms, p-adic depths, actual extremes, negative margin, all exterior roots and costs. |
| support | [Original J56 group](../computations/programs/Yin_J_G0056/readme.md) | Exactly eighteen declared actual inputs/windows, author and distinct row-space/quotient-determinant checker, finite native scope without an all-input inference. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0056/readme.md#recorded-runs) | All eighteen full coefficient/degree/content/resultant/discriminant/energy/margin records, with nine higher-degree cases only finite evidence. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0056/verification.json`; this target locates its run account. |

### Decision complete-interface-open

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:14 |
| status | open |
| reason | Make the consumed original centered interface complete in this home: spell out the unit/primitive nonmonomial proof, its own support-order notation and the quadratic recurrence, replacing orphan references from the larger L249 proof. The original L253 derivative/norm/negative/root mechanism and theorem are unchanged; v1 remains its actual open home-completeness input. Whole checking of this fixed version is pending. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact theorem](#statement) | Every reciprocal nontorsion original P and integer j>=d-1, every prime/root/content, all quadratic a>=3/j>=1 costs/limits/roots and finite eighteen-case boundaries. |
| argument | [Entire proof](#argument) | Full precise centered/primitive/edge/quadratic-circle interface and all original Sections1--6/equations1--17, with complete norms, ramified depths, coefficients, actual degrees, contents, negative/asymptotic and root costs. |
| support | [Original J56 group](../computations/programs/Yin_J_G0056/readme.md) | Exactly the original eighteen inputs/windows, author and distinct reviewer implementations and native scope; no general higher-degree inference. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0056/readme.md#recorded-runs) | All eighteen complete coefficients/degrees/content/resultants/discriminants/energies/signs, with nine higher-degree cases only finite evidence. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0056/verification.json`; this target locates its run account. |

### Decision complete-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T19:17 |
| status | proved |
| reason | Adopt after the actual full C423v2/R627 whole self-check of the complete centered/primitive/quadratic-circle interface and every original edge derivative, resultant/discriminant/rootwise-depth, actual coefficient/degree/content, all-window quadratic negative, fixed-input asymptotic and full exterior-root/cost argument. The fixed J56 reviewer replay reproduces exactly all eighteen cases and25 fields per case without a new input/window or native write. All higher-degree/near-one negatives and original R152 whole UNKNOWN remain; this is not fresh isolated coverage or Task/E resumption. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact theorem](#statement) | Every reciprocal nontorsion original P and integer j>=d-1, every prime/root/content, all quadratic a>=3/j>=1 costs/limits/roots and finite eighteen-case boundaries. |
| argument | [Entire proof](#argument) | Full precise centered/primitive/edge/quadratic-circle interface and all original Sections1--6/equations1--17, with complete norms, ramified depths, coefficients, actual degrees, contents, negative/asymptotic and root costs. |
| support | [Original J56 group](../computations/programs/Yin_J_G0056/readme.md) | Exactly the original eighteen inputs/windows, author and distinct reviewer implementations and native scope; no general higher-degree inference. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0056/readme.md#recorded-runs) | All eighteen complete coefficients/degrees/content/resultants/discriminants/energies/signs, with nine higher-degree cases only finite evidence. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0056/verification.json`; this target locates its run account. |
| review | [Actual entire self finding](../audits/reviews/Yin_R_G0627_v1.md#edge-derivative-whole-self-finding) | Complete exact statement/argument/supports, all parameters/signs/contents/prime depths/root costs, original finite records and fixed-domain replay, with no empirical general-negativity inference. |


### Decision complete-isolated-whole-r800-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-21T20:59 |
| status | proved |
| reason | Adopt the new complete isolated whole finding after full coordinator reading of its exact mathematics, old whole/negative/source/native comparisons and truthful date/context limits; no target proof repair and no retrospective change to original UNKNOWN or SELF relationships. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Exact statement](#statement) | Every reciprocal nontorsion original P and integer j>=d-1, every prime/root/content, all quadratic a>=3/j>=1 costs/limits/roots and finite eighteen-case boundaries. |
| argument | [Complete selected argument](#argument) | Full precise centered/primitive/edge/quadratic-circle interface and all original Sections1--6/equations1--17, with complete norms, ramified depths, coefficients, actual degrees, contents, negative/asymptotic and root costs. |
| support | [Exact support](../computations/programs/Yin_J_G0056/readme.md) | Exactly the original eighteen inputs/windows, author and distinct reviewer implementations and native scope; no general higher-degree inference. |
| support | [Recorded computation run](../computations/programs/Yin_J_G0056/readme.md#recorded-runs) | All eighteen complete coefficients/degrees/content/resultants/discriminants/energies/signs, with nine higher-degree cases only finite evidence. Original recorded result, output: `mathematics/computations/outputs/Yin_J_G0056/verification.json`; this target locates its run account. |
| review | [Actual complete finding](../audits/reviews/Yin_R_G0653_v1.md#edge-derivative-isolated-whole) | Whole exact centered derivative/primitive/full-root/full-prime theorem, every quadratic parameter and all eighteen-case/source/cost/negative boundaries. |

## Reproducing the reviewed computations

The programs and run-reproduction conditions for the numerical findings selected here are recorded at [Yin_J_G0056](../computations/programs/Yin_J_G0056/readme.md#reproducing-reviewed-runs).
Generated outputs remain local; each finding concerns its recorded run, and this material asserts no new replay.
