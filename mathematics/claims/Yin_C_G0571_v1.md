---
author: Yin
---

# Complete actual anti columns, primitive Gram orders and signed trace edges

This common actual anti row-space object retains BOTH complete [L296](../ledger/Yin_L_G0296_v1.md) and [L300](../ledger/Yin_L_G0300_v1.md) proof chains, with separate column, whole-row-space and torsion quantifiers.
Their original formal findings and fixed old inputs remain in R195/R199, with no research or native execution.

<a id="statement"></a>
## Complete statement

Let P in Z[t] be the ACTUAL monic irreducible reciprocal nontorsion unit polynomial of degree d=2s and constant1, with TOTAL m=log M(P)>0.
Write P=t^s Q(t+t^-1), alpha an original root, tau=alpha+alpha^-1, O=Z[alpha], B=Z[tau].
The trace polynomial Q is actual monic irreducible degree s; it need not be totally real.
For EVERY n>=s, define
    U_0=1,U_1=x,U_(j+1)=x U_j-U_(j-1),
    C_c(t)=sum_(l=1)^n c_l(t^(n+l)-t^(n-l)),
    R[:,l]=coeff rem_Q U_(l-1), H=RR^T, Delta=det H,
    W=image_R R^T, Pi=R^T H^-1 R.
The first s remainder columns are triangular unimodular, H>0 and W has REAL dimension s.
For EVERY1<=k<=n, c_k=Pi e_k is nonzero,
    ell_k=Pi_kk=||c_k||^2>0, sum_k ell_k=s,
    C_(c_k)(alpha_i)=alpha_i^(n-k)(alpha_i^(2k)-1)
at EVERY original root.
For the least minimum-diagonal k, ell_k<=s/n.
Let q>0 be the exact rational primitive scale of c_k and F=C_(q c_k).
With Z_(2k)=|Res(P,t^(2k)-1)|>=1, the complete signed/norm/energy identities are
    Res(P,F)=q^d Res(P,t^(2k)-1),
    S_2(F)^2=2q^2 ell_k,
    B_net(F):=log|Res(P,F)|/d-log S_2(F)
       =log Z_(2k)/d-(1/2)log(2ell_k)>=(1/2)log[n/(2s)].
q may be rational; its reduced denominator b divides the actual order remainder content of t^(2k)-1 and b^d divides Z_(2k).
At EVERY original p-adic root, v_p(F(alpha_i))=v_p(q)+v_p(alpha_i^(2k)-1)>=0, including ramification/index primes.
The rational term may be negative.
Exact-column height<=Delta, S_2<=sqrt(2n)Delta, M(F)<=S_2 and rho=S_1^2/S_2^2<=2n retain every leading/content/coefficient cost.

For EVERY nonzero rational c in W and nonzero integral polynomial F proportional to C_c, let h=max{l:c_l!=0}, b=n-h.
After removing t^b the ACTUAL degree is2h, with its true leading coefficient, forced t^2-1 and EVERY reciprocal quadratic trace-root factor.
The full signed edge identity is
    P F=A-t^(2n+1)A*, deg A<=d-1, A*=t^(d-1)A(1/t),
with A nonzero and primitive if F is primitive.
The reversal uses formal degree d-1 even if A's actual degree drops.
Let r be the number of Q roots in(-2,2), so r<=s-1.
Weighted partial orthogonality forces at least max(0,n-s-r) sign changes of V_c=sum_l c_l U_(l-1) there.
For n>=s+r, b<=s+r-1 and at most2(s+r-1-b)<=2d-4 auxiliary root slots can lie off the circle.
For n<s+r retain the trivial2h-2 bound.
These count roots only; neither their moduli nor the actual leading coefficient is free.

Fix C>2 and n=ceil(Cs), and remove any monomial from the selected primitive F to get actual degree T<=2n.
Then B_net(F)-Tm/d>=(1/2)log(C/2)-(C+1)m.
Uniformly over ALL k<=n along a hypothetical m->0 input sequence, C391 gives log Z_(2k)/d=o(1), retaining actual powered-degree loss.
Thus the surplus does not supply same-exponent linear cyclic income.
Only on the actual separate domain u=(C+1)m in(0,h_0] of C570, its epsilon gives
    (rho-1)epsilon(u)+4rho u>=(C/2)exp(-2u)-1,
    rho>=[(C/2)exp(-2u)-1+epsilon(u)]/[epsilon(u)+4u].
No upper coherence or cheap Delta estimate is proved.

There is a stronger exact integral interpretation:
    W intersect Z^n=R^T Z^s, content(R^T w)=content(w).
For nonzero w in Z^s, let v_w have coefficient vector H w.
Then
    Res(P,C_(R^T w))=P(1)P(-1) Norm_(Q(tau)/Q)(v_w(tau))^2,
    S_2(C_(R^T w))^2=2w^T H w.
Put r_k=R e_k, delta_k=content(r_k), u_k=r_k/delta_k,
    v_k=adj(H)u_k, gamma_k=content(v_k),
    L_k=Delta/gamma_k, w_k=v_k/gamma_k.
Here gamma_k DIVIDES Delta, L_k is a positive INTEGER and w_k is primitive.
L_k is EXACTLY the additive order of u_k modulo H Z^s, and
    q_k=L_k/delta_k,
    F_k=C_(R^T w_k)=C_(q_k c_k),
    F_k(alpha_i)=L_k alpha_i^n(alpha_i-alpha_i^-1)u_k(tau_i),
    Res(P,F_k)=L_k^d P(1)P(-1)Norm(u_k(tau))^2,
    S_2(F_k)^2=2(L_k/delta_k)^2 ell_k.
F_k belongs to(P,L_k), with each original p-adic depth at least v_p(L_k), retaining the exact additional integral factors.
The paid scalar margin is log L_k-log S_2=log delta_k-(1/2)log(2ell_k).
For a minimum-diagonal column n>2s forces L_k>=2, without a dyadic restriction.
Exactly Z_(2k)=delta_k^d |P(1)P(-1)| |Norm(u_k(tau))|^2.
delta_k^d divides Z_(2k), but L_k^d need not divide it.
For fixed C>=1 and s<=n<=Cs, hypothetical sufficiently small total m forces EVERY delta_k=1 simultaneously, hence q_k=L_k integral.
This pays neither L_k nor energy/coherence and improves no generic scalar-existence theorem.

The actual integral direct sum O=B direct_sum alpha B gives O^sigma=B for inversion sigma.
For EVERY nonzero a in B and n>=s,
    A_n(a)=rem_P(alpha^(n+s)a),
    F_n(a)=[A_n(a)-t^(2n+1)A_n(a)*]/P
is a nonzero integral actual row-space anti polynomial.
Together with the inverse a=alpha^(-(n+s))A(alpha), this is a Z-linear bijection
    B <--> {C_c:c in W intersect Z^n},
    content(a)=content(A_n(a))=content(F_n(a)).
Its full EDGE norm is Res(P,A_n(a))=Norm_(Q(tau)/Q)(a)^2>=1 with original inverse-pair prime multiplicities.
The auxiliary norm uses H w, its edge norm uses an integral unimodular but not height-bounded E_n w, and coefficient energy is2w^T H w.
They are distinct quantities.
Taking a=1 gives a primitive admissible row-space polynomial on EVERY input/window with edge norm1 and full original-conjugate evaluation expense(n+s)m.
It excludes positive edge-norm income across the WHOLE row-space class, but makes no assertion that this polynomial is a single or minimum-diagonal paired column.

For actual P=t^2-a t+1, integer a>=3, alpha=(a+sqrt(a^2-4))/2, r_l=U_(l-1)(a) and H_n=sum r_l^2, every primitive column is
    F_n=sum_l r_l(t^(n+l)-t^(n-l)), q_k=H_n/r_k,
    Res(P,F_n)=(4-a^2)H_n^2, S_2(F_n)^2=2H_n,
    B_net(F_n)=(1/2)log[(a^2-4)H_n/2].
ALL2n auxiliary roots are on the circle, but full M(F_n)=r_n and
    B_net(F_n)-n log alpha<-(1/2)log[2(1-alpha^-2)]<0
for every n>=1, with equality only as the limit n->infinity.
The edge is A_n=-r_n+r_(n+1)t, Res(P,A_n)=1 and M(A_n)=r_(n+1).
For a=3,n=2,k=2, delta=3,L=10,q=10/3,
    F=3t^4+t^3-t-3,A=-3+8t,
    Res(P,F)=-500,S_2(F)^2=20,M(F)=3,M(A)=8.
The actual irreducible odd-prime radicals t^(2p)-3t^p+1, p>=3, lift these residue-zero columns, preserving coefficients/M/rho and the negative radial excess, with actual degree2p and FIXED positive total measure.
No assertion that the lifted column minimizes every larger diagonal is made.

A SEPARATE torsion control replaces P by Phi_p, p odd prime, n=Kp, K>=1, and uses1<=j<=s=(p-1)/2, excluding zero columns at multiples of p.
Then ell_j=1/(2K), q=2K, and
    F_j=t^j(1-t^(p-2j))sum_(a=0)^(2K-1)t^(ap),
    |Res(P,F_j)|=p(2K)^(p-1), S_2^2=rho=4K,
    M(F_j)=1, B_net(F_j)=(1/2)log K+log p/(p-1).
After monomial removal its actual degree is2(n-j).
For fixed K>=2 and p->infinity, positive surplus and bounded rho coexist at TORSION measure zero.
This is no counterexample to the separate nontorsion/small-h coherence input.

Both complete original proofs, the actual2026-10-10T05:55 nonzero-quantifier clarification, all source/contribution/negative controls and the original whole author self-check2026-10-10T06:27 remain explicit.
No mathematical program/J/source proof audit, actual near-one family, upper coherence estimate, adjacent-centered realization, unrestricted gap or new scalar-existence mechanism is asserted.

## Complete argument

<a id="argument"></a>

## Complete actual-column, cyclic and root argument

<a id="actual-anti-column-reuse"></a>
### 1. Changed realization and precise reuse

The actual Task contract and Yin's applicable policies were read.
The resultant_research AI for Yin develops the argument below; root supplied the broad question, not a derivation.
The full [L292 enlarged anti class](Yin_C_G0545_v1.md#statement) and [L229 coefficient/conjugate bound](Yin_C_G0570_v1.md#actual-resultant-coefficient-energy-bound) are the immediate inputs.
[L237's monomial projection](Yin_C_G0570_v1.md#monomial-projection-uniform-margin) already uses rank and the sum of projection diagonals to obtain unrestricted scalar auxiliaries.
The dimension argument below is explicitly that SAME mechanism specialized to L292's actual anti-reciprocal quotient; it is not a new proof mechanism or a new discovery of scalar positive-margin existence.

The changed conclusion is a genuine SINGLE paired-monomial projection with exact cyclic values at every original root, together with the complete root and two-edge structure of its actual rational coefficient vector.
This differs from L292's arbitrary maximum/moment direction and its ambient-grid rounding.
The sign-change proof reuses [L249's signed partial-orthogonality argument](Yin_C_G0570_v1.md#centered-column-fixed-scope), with the positive semicircle weight appropriate to the anti basis instead of its centered reciprocal/arcsine weight.
L249's checked Nat26 attribution and source-reading limits remain unchanged; no source theorem is newly imported.
[L253](../ledger/Yin_L_G0253_v1.md#edge-derivative-fixed-scope) already charges a differentiated centered edge, and the present result does not remove that expense or assume a derivative gives a gain.

A bounded local ledger/draft screen for anti projections, paired columns, cyclic projection, trace Gram and root-weight structure found these interfaces and the older [L10 inverse-trace constraints](../ledger/Yin_L_G0010_v1.md#general-reciprocal-necessary-bound).
L10's signed spectral form is not the Euclidean coefficient projection used here.
Its determinant or integer trace identities are not repackaged as a new coherence estimate.
The following direct specialization, exact torsion control and whole root accounting require no new external theorem or program.
No priority claim is made.

Let P be monic irreducible reciprocal in Z[t], of degree d=2s, constant coefficient1, with no root of unity.
Write P=t^s Q(t+t^-1), where Q is the actual monic irreducible trace polynomial of degree s.
All original roots are retained.
Set m=log M(P)>0.
For n>=s use the L292 anti coefficient map

    C_c(t)=sum_(l=1)^n c_l(t^(n+l)-t^(n-l))
          =t^(n-1)(t^2-1)V_c(t+t^-1),
    V_c=sum_(l=1)^n c_l U_(l-1),
    U_0=1, U_1=x, U_(l+1)=x U_l-U_(l-1).             (1)

Its squared coefficient norm is2||c||^2.
Let R be the integral s-by-n matrix of these U remainders modulo Q, H=RR^T, W=row_R R and

    Pi=R^T H^-1 R.                                  (2)

By L292, H is positive definite, W has REAL dimension s even with nonreal trace conjugates, and Pi is its rational Euclidean orthogonal projection.
Kernel R consists exactly of the trace multiples of Q in this window.

<a id="single-anti-column-cyclic-realization"></a>
### 2. A single actual column, its full norm and its selected exponent

For1<=k<=n put c^(k)=Pi e_k and ell_k=Pi_kk.
Every ell_k is strictly positive.
Otherwise c^(k)=0 and R e_k=0, so Q divides U_(k-1); evaluating(1) at an original root would give alpha^(2k)=1.
This contradicts nontorsion.
Projection gives

    ||c^(k)||^2=c_k^(k)=ell_k,
    sum_(k=1)^n ell_k=s,
    C_(c^(k))(alpha)=alpha^(n-k)(alpha^(2k)-1).       (3)

The last equality holds because e_k-c^(k) belongs to ker R and hence its anti polynomial is a real multiple of P; its coefficients are in fact rational.
It holds simultaneously at EVERY original root, with no chosen embedding or average in its place.

Choose the least index minimizing ell_k, so ell_k<=s/n.
Let D be the least positive INTEGER clearing all coordinates of c^(k), g the positive gcd of D c^(k), q=D/g>0 rational, and F=C_(q c^(k)).
Then F is primitive integral and nonzero.
Write the positive integer

    Z_(2k)=|Res(P,t^(2k)-1)|>=1.

Since the product of all original roots is1, the COMPLETE identities are

    F(alpha_i)=q alpha_i^(n-k)(alpha_i^(2k)-1),
    Res(P,F)=q^d Res(P,t^(2k)-1),
    S_2(F)^2=2q^2 ell_k,
    B(F):=log|Res(P,F)|/d-log S_2(F)
          =log Z_(2k)/d-(1/2)log(2ell_k)
          >=(1/2)log[n/(2s)].                       (4)

The signed identity is valid because q is positive rational and the unit monomial product is1.
Its left side is a nonzero integer; the product on the right is not separated into unproved integer factors.
The selected common cyclic exponent2k satisfies2k<=2n.
This does NOT prove log Z_(2k)>=eta*d: the whole lower bound can come from the small coefficient norm of the projection rather than from large cyclic income.
No costs or incomes at different k are added.

In particular this is an actual one-column realization in the enlarged anti window, not an assertion that it is one of the adjacent centered differences in L257.
The trace-average construction is reused from L237, but the actual root values here are a cyclic binomial instead of a monomial.
Their primitive denominator/content behavior is consequently different.

<a id="anti-column-content-and-depth"></a>
### 3. Actual order and complete primitive depth

It is essential not to assume that q in(4) is an integer: the proof supplies a positive rational scale, and the complete family of projection columns really can have a denominator after primitive normalization, as Section6 exhibits.
No additional integer-scale theorem for the selected minimum is used.
Write q=a/b in lowest terms, a,b positive.
Let w_k be the coefficient vector of the remainder of t^(n-k)(t^(2k)-1) modulo P in the ACTUAL order Z[t]/(P).
Since F has integral coefficients, q w_k is an integral vector.
Thus

    b divides every coordinate of w_k.              (5)

Conversely this is the precise integrality condition on q times that root value.
Multiplication by alpha^(n-k) is a unimodular integral map of the actual order because alpha is a unit, so the content of w_k equals the content of the remainder of t^(2k)-1.
Neither maximal-order saturation nor an index-prime assumption is used.
Relation(5) also gives b^d dividing the nonzero integer Z_(2k).
It does not force b=1, because the binomial value need not be primitive in the order.

At each original p-adic root, normalized by v_p(p)=1, the exact finite-place identity is

    v_p(F(alpha_i))=v_p(q)+v_p(alpha_i^(2k)-1)>=0.   (6)

The rational scalar term may be negative, and is retained with that sign.
Thus one cannot silently reuse L237's content-divides-integer-scalar conclusion or assign a surviving uniform dyadic floor.
Equation(6), summed over the original d roots, gives exactly the valuation of(4), including repeated reductions, ramification and index primes.
The original degrees d and s, rather than the enlarged degree, govern scalar norm changes.

There are finite explicit coefficient bounds, but no input-uniform cheap-height assertion.
Put Delta=det H and A=R^T adj(H)R.
Then Pi=A/Delta, all entries of A are integers, and ||Pi||<=1 gives |A_lk|<=Delta.
If gamma is the gcd of the k-th column of A, the primitive vector is exactly A[:,k]/gamma and

    q=Delta/gamma,
    height(F)<=Delta,
    S_2(F)<=sqrt(2n) Delta,
    M(F)<=S_2(F),
    rho(F)=S_1(F)^2/S_2(F)^2
          =2||c^(k)||_1^2/ell_k<=2n.               (7)

Here q=Delta/gamma agrees with D/g, by primitive normalization of the same rational direction; gamma need not divide Delta.
The positive diagonal A_kk ensures the sign of the chosen primitive direction is fixed.
All inequalities include the complete leading coefficient and all nonzero coefficient positions.
Determinant size may depend strongly on P and n; unlike L292's ambient approximation theorem, this exact-column construction does not currently give a polynomial height bound.
Removing a monomial factor changes no original-root norm or coefficient norm, since P is a unit polynomial.

<a id="anti-column-full-edges-and-root-count"></a>
### 4. Whole signed edge identity and all exceptional root slots

This section applies to EVERY nonzero rational c in W, not only the selected column.
Such a c has nonzero resultant: a shared trace root would force Q to divide the rational polynomial V_c, giving c in W intersect ker R={0}.
Let h=max{l:c_l!=0}, b=n-h, and let F be any nonzero integral polynomial proportional to C_c.
After removing t^b, its actual degree is2h, its leading coefficient is the corresponding c_h times that scalar, and

    F/t^b=beta(t^2-1) product_(j=1)^(h-1)(t^2-r_j t+1), (8)

where beta is the actual leading coefficient and the r_j are ALL roots of the trace polynomial, counted with multiplicity.
No nonreal or exterior root is omitted.

The relation-space orthogonality has a complete coefficient consequence.
For1<=j<=n-s, the polynomial P(t)(t^(n-s+j)-t^(n-s-j)) lies in the anti window.
Orthogonality of c to ker R is exactly its coefficient inner product with F being zero, up to the common factor2 in the anti basis.
Since P is reciprocal,

    <F,P t^a>=[t^(a+2s)] P F.

The product P F is anti-reciprocal at FORMAL degree2n+2s, so the two coefficients at n+s+j and n+s-j are opposite.
Orthogonality makes them both zero.
The middle coefficient is zero by anti-reciprocity itself.
Consequently the entire coefficient band from2s through2n vanishes and

    P F=A(t)-t^(2n+1) A*(t),
    deg A<=d-1,  A*=t^(d-1)A(1/t).                 (9)

A is nonzero.
If F is primitive then A is primitive: the monic integer P times primitive F is primitive by coefficient reduction modulo each prime, and the two disjoint edge blocks in(9) have the same coefficient gcd.
Since deg A<d and P is irreducible, A has no common original root.
Thus(9) also retains the actual all-root equation A(alpha)=alpha^(2n+1)A*(alpha), without treating A as a monic unit seed or controlling its whole measure for free.

For the root count, the U basis is orthogonal with a positive multiple of the weight sqrt(4-x^2) on(-2,2).
This follows directly from U_(l-1)(2cos theta)=sin(l theta)/sin theta and ordinary sine orthogonality on(0,pi).
The condition c in W therefore gives

    integral_(-2)^2 V_c(x) Q(x) Y(x) sqrt(4-x^2) dx=0
              for every real Y with deg Y<n-s.     (10)

If the nonzero real polynomial V_c Q had fewer than n-s distinct sign changes in(-2,2), multiply it by the product of the corresponding linear factors.
That product has degree below n-s and makes the integrand in(10) of one constant nonzero sign except at finitely many points, a contradiction.
This is exactly the retained L249 sign argument with the changed weight.
Let r be the number of actual Q roots in(-2,2).
These are simple, and nontorsion gives r<=s-1 at the accepted Kronecker scope.
Since Q can contribute at most r sign changes, V_c has at least

    max{0,n-s-r} sign changes in(-2,2).             (11)

Whenever n>=s+r, (11) implies h>=n-s-r+1, hence b<=s+r-1.
At least2+2(n-s-r) roots of F/t^b lie on the unit circle, counting the forced endpoints; the number of remaining slots is at most

    2(s+r-1-b)<=2(s+r-1)<=2d-4.                   (12)

For n<s+r use the trivial2h-2 bound instead of a negative slot count.
This bounds the NUMBER of possible exterior slots independently of the enlarged n, not their moduli or beta.
Complete Mahler cost is exactly |beta| times the product over every reciprocal root pair in(8) of max(1,|z_j|,|z_j|^-1).
Therefore a circle-root count alone still does not pay leading/exterior expense.
Equations(9)--(12) apply to actual rational projection directions, whereas arbitrary coefficient-grid rounding out of W need not preserve them.

<a id="actual-anti-column-near-one-boundary"></a>
### 5. Uniform actual-column excess and the precise near-one expense

For a fixed real C>2 take n=ceil(C s), so n/s lies in[C,C+1].
The actual F from Section2 can have a monomial factor t^b; removing it gives primitive F_0 of actual degree T=2h<=2n and leaves its complete resultant, S_2 and rho unchanged.
Equations(4) and the full radial charge give

    B(F_0)-Tm/d >=(1/2)log(C/2)-(C+1)m.             (13)

This is a uniform positive excess for all sufficiently small positive TOTAL m, conditional on such inputs existing.
The exact realized window is no longer merely an arbitrary real norm-form maximizer: it is a selected single paired-monomial residual, with(6),(9)--(12).
The trace argument behind(13) is still a specialization of L237 and does not claim new generic scalar existence.
Its exact-column height is paid by Delta in(7); L292's independent polynomial-height ambient approximation does not by itself retain the column origin or the root-count structure.

The original [L168 uniform cyclic cost](Yin_C_G0391_v1.md#bounded-power-degree-escape) gives, uniformly for every k<=n along any hypothetical m->0 family,

    log Z_(2k)/d=o(1),
    B(F_0)=-(1/2)log(2ell_k)+o(1).                  (14)

Indeed2k<=2n<=2(C+1)s=(C+1)d, so its original-degree/time hypothesis is exactly met even when alpha^(2k) loses degree.
This is the accepted full cyclic-cost theorem, with its Pri11/source-proof boundary unchanged.
Thus(13) does not manufacture the missing same-exponent linear cyclic income: the projection scale and energy are the decisive surplus mechanism, and that mechanism already has a joint-coherence price.

Let u=(C+1)m.
On the actual L229 domain0<u<=h_0, its increasing epsilon and the exact nonzero F_0 give the necessary inequality

    (rho-1)epsilon(u)+4rho u >=(C/2)exp(-2u)-1.      (15)

This follows from B(F_0)>=(1/2)log(C/2), Tm/d<=u and L229, before any limit.
For fixed C>2 its right side tends to C/2-1>0; hence these actual columns cannot have rho epsilon(u)->0.
Equivalently,

    rho >=[(C/2)exp(-2u)-1+epsilon(u)]
                                      /[epsilon(u)+4u].       (16)

This is a necessary cost, not a new uniform upper estimate.
Radial cost, number of exterior roots, or the positive column surplus cannot be substituted for the missing signed coefficient/conjugate control.
In particular(12) and(15) can both hold: a polynomial with almost all roots on the circle can still have the required large coefficient interaction or leading expense.

<a id="actual-anti-column-quadratic-all-window-control"></a>
### 6. A nontorsion all-window control and exact leading expense

Take the actual irreducible quadratic P=t^2-a t+1 with integer a>=3.
Its discriminant a^2-4 lies strictly between(a-1)^2 and a^2, so it is not a square; P is irreducible, reciprocal and nontorsion.
Put alpha=(a+sqrt(a^2-4))/2>1, m=log alpha, and

    r_l=U_(l-1)(a)=(alpha^l-alpha^-l)/(alpha-alpha^-1),
    H_n=sum_(l=1)^n r_l^2.

The row space W is spanned by the integral vector r=(r_1,...,r_n), with r_1=1 and r_l positive and strictly increasing.
Thus Pi e_k=r_k r/H_n, and EVERY column has the same primitive anti polynomial

    F_n=sum_(l=1)^n r_l(t^(n+l)-t^(n-l)),
    q_k=H_n/r_k,
    Res(P,F_n)=(4-a^2)H_n^2,
    S_2(F_n)^2=2H_n,
    B(F_n)=(1/2)log[(a^2-4)H_n/2].                 (17)

The minimum diagonal selects k=1.
For a=3,n=2 the other column has q_2=10/3, giving the promised actual rational-scale control; primitive normalization cannot be treated as content dividing the old integer scalar without checking the original remainder.
The displayed signed resultant follows either from(4) or directly from the two original reciprocal values, with their product negative.

Here r=0 in the root-count notation of Section4.
Consequently ALL2n roots of F_n lie on the unit circle, including both endpoints, and its complete measure is EXACTLY its leading coefficient r_n.
For n=1 this leading coefficient is1; for n>=2 it is greater than1 and grows at the explicit fixed-input exponential rate m.
There are no hidden exceptional roots in this control.
Nevertheless its FULL radial excess is negative for EVERY n>=1:

    B(F_n)-n m
       < -(1/2)log[2(1-alpha^-2)]<0,
    lim_(n->infinity)[B(F_n)-n m]
       =-(1/2)log[2(1-alpha^-2)].                    (18)

For proof, (a^2-4)H_n=sum_(l=1)^n(alpha^l-alpha^-l)^2 is strictly smaller than sum_(l=1)^n alpha^(2l), which in turn is smaller than alpha^(2n)/(1-alpha^-2).
Since alpha>=(3+sqrt5)/2>sqrt2, the last logarithmic constant is negative.
Dividing the exact sum by alpha^(2n) gives the stated geometric-series limit, the terms -2n and sum alpha^(-2l) vanishing after that division.
The actual degree is2n, so n m is exactly Tm/d here.
The coefficient interaction is also fully explicit: rho=2(sum r_l)^2/H_n.
No numerical scan is involved.

The same control embeds in genuine unbounded degrees without becoming near one.
For each odd prime p use the accepted [L193 irreducible input](Yin_C_G0463_v1.md#exact-resultant-content-collapse) P_p(t)=t^(2p)-3t^p+1.
Its actual degree is2p and m(P_p)=log((3+sqrt5)/2), fixed positive.
In anti window index p n, the projection of the paired column with index p k is the coefficient lift of the quadratic Pi e_k through t->t^p.
To see this directly, decomposition by exponent residues modulo p is orthogonal in coefficient space and multiplication by P(t^p) preserves each residue.
Anti reflection pairs residues r and -r, and the residue-zero block is invariant and is exactly the base anti space after substitution.
Projection of a residue-zero input therefore remains there.
This is the same exponent-residue separation mechanism already used in [L4's time dilation](../ledger/Yin_L_G0004_v1.md#degree-window-tests), not a new radical irreducibility theorem.

The primitive output is F_n(t^p), with the same coefficients, height, S_2, rho and full Mahler measure r_n.
Every root beta of the base P has all p preimages, and F_n(alpha^p)=F_n(beta), so its signed resultant is Res(P,F_n)^p, including multiplicity.
Its original normalized B equals(17), its actual degree is2pn, and its radial charge is again n m.
Thus(18) survives at unbounded ACTUAL degree with all roots and costs retained.
This is a fixed-positive-total-measure control, not a hypothetical near-one counterexample or a uniform obstruction there.
These are actual columns, not a claim that a lifted column minimizes all diagonals in the larger space.

<a id="actual-anti-column-torsion-exact-control"></a>
### 7. Exact prime torsion columns: positive surplus with bounded support

This section deliberately replaces nontorsion by the actual prime cyclotomic polynomial P=Phi_p, p odd prime, d=p-1=2s.
Put n=K p with integer K>=1.
The zero projection columns at multiples of p are excluded; they are precisely the vanished cyclic root values.
For1<=j<=s the actual projection is

    (Pi e_j)_l=[1_(l=j mod p)-1_(l=-j mod p)]/(2K),
    ell_j=1/(2K).                                    (19)

Indeed the real sine evaluation matrix with entries2sin(2pi i l/p),1<=i<=s,1<=l<=n has row Gram2n I_s by the finite geometric-series identity.
The inner product of columns j,l is p times the indicated residue difference.
Multiplication by1/(2n) gives(19), using precisely the actual row space W of L292.
This is its sine identity specialized to a single projection column, not an independent-phase model.

There are exactly2K nonzero anti coordinates in(19), each of absolute value1/(2K).
Clearing that denominator gives the primitive integral polynomial

    F_j(t)=t^j(1-t^(p-2j)) sum_(a=0)^(2K-1)t^(ap),
    q=2K,
    |Res(P,F_j)|=p(2K)^(p-1),
    S_2(F_j)^2=4K, rho(F_j)=4K,
    M(F_j)=1,
    B(F_j)=(1/2)log K+log p/(p-1).                 (20)

To verify the polynomial, first sum t^(n+l)-t^(n-l) over l=j modulo p and subtract the sum over l=-j modulo p.
The two geometric sums combine into the displayed(1-t^(p-2j)) times the2K-term progression.
The two sets of exponents do not overlap because0<p-2j<p, so all4K coefficients have absolute value1 and the polynomial is primitive.
Its monomial factor is exactly t^j; after removing it the actual degree is2(n-j).
Both nonconstant displayed factors have only roots of unity and leading coefficient of absolute value1, proving the complete Mahler value, not just a circle-zero count.
At a primitive pth root alpha the progression is2K, and raising alpha to the nonzero residue p-2j permutes the original conjugates.
Thus the complete product of1-alpha^(p-2j) is Phi_p(1)=p, establishing the whole resultant with no omitted factor.

For any fixed K>=2 and p->infinity, these actual primitive columns have uniform positive B, bounded rho=4K, zero radial cost, all roots on the circle and leading magnitude1.
Their degree/original-degree ratio remains bounded.
This exactly demonstrates why an actual-column realization, a root-count bound and bounded effective support cannot by themselves imply nontorsion: the input is torsion.
It does not contradict L229, which requires nontorsion and positive h and uses actual powered-degree escape.
No torsion column at a multiple of p is used to invoke a nonzero norm.

<a id="actual-anti-column-contribution-and-boundary"></a>
### 8. Outcome, complete costs and remaining discriminator

The changed interface is now explicit.
In every enlarged anti window the rational row space has actual single paired-monomial residuals.
Nontorsion ensures EVERY one of their cyclic evaluations is nonzero, so a minimum diagonal yields a true primitive auxiliary with(4),(13).
Its complete primitive scalar can be rational and its prime depths are exactly(6); no all-root floor is manufactured.
Its signed full product has the two-edge form(9), and only O(d) nontrivial auxiliary slots can leave the circle even while n grows.
The exact torsion columns show that these structural properties can coexist with cheap support at measure zero.
The all-window quadratic control and its actual prime radicals instead pay a leading coefficient that recreates the full positive radial expense.

The positive margin argument reuses L237's projection trace, the quotient space and norm normalization reuse L292/L257, the root count reuses L249's sign-change method, and the radical block separation reuses L4.
These are precise adaptations, not claimed as newly invented tools or as new generic scalar existence.
The useful new output is their fully connected single-column/cyclic/edge/root interface and its two exact actual-input controls.
No optimized512 constant, new complete theorem from an uninspected source, finite computer experiment or alleged near-one family is part of this proof.

L168 makes the selected cyclic norm only o(d) in the genuine near-one regime; the rest of the positive surplus must still be paid through actual coefficient/conjugate interaction.
L229 records that price in(15)--(16).
The statements here do not provide an upper bound paying it, a polynomial exact-column height bound, a low-degree leading/exterior norm estimate, or a way to replace the full original measure by m/d.
They do not turn the edge A into a monic seed, and they do not realize these auxiliaries as the old adjacent-centered differences.
The next changed test is the joint arithmetic of the actual low-degree edge A and its complete denominator q/cyclic remainder: control of that signed pair, or a demonstrably different nonquadratic comparison, would need to distinguish(20)'s torsion behavior while respecting(18)'s leading loss.
All mathematical routes remain active and the unrestricted Task unresolved.

Author self-check completed: the actual REAL rank-s quotient and positive column diagonals; rational primitive scale and complete signed original resultant; both coefficient contents and their original-degree exponents; integrality in the actual order including every bad prime; monomial removal and actual degree; the complete anti edge band with its sign and shift2n+1; weighted partial orthogonality and all small-window/degree-drop boundaries; exact cyclic-cost uniformity and L229's restricted small-h domain; every quadratic/root/leading/radial calculation; actual prime-radical irreducibility and coefficient-residue projection; and the entire torsion column, complete factorization and all4K coefficients were checked.
The a=3 endpoint in the quadratic lower bound is non-strict as required.
No J was allocated or program executed for this proof-only round; every displayed control is an all-parameter direct calculation.
This self-check does not replace the complete separate noncontributor review required before fixed adoption.


Final author freeze: 2026-10-10T05:54.
Complete Sections1--8, equations(1)--(20), all source/reuse boundaries, exact controls and self-check are frozen for a whole separate noncontributor review.
The scoped material check passed before this freeze line and is rerun below.
No fixed adoption or unrestricted gap is asserted.


Pre-adoption review clarification and author re-freeze, 2026-10-10T05:55: root's complete written review noted that Section4's former phrase "any integral scalar multiple" literally included the zero scalar, while the degree and root factorization require nonzero F.
The author changed ONLY that phrase to "any nonzero integral polynomial proportional to C_c".
All formulas and every nonzero case are unchanged; no computation or source change was made.
The complete corrected author body is frozen for root's final finding.




## Complete primitive-order and signed-edge argument

<a id="anti-column-order-reuse"></a>
### 1. Exact question, hypotheses and reused inputs

The changed question is whether the rational primitive scale of an ACTUAL anti projection column admits an integral arithmetic decomposition, and what restrictions the complete signed edge places on its original norm.
The actual Task and applicable identity and knowledge-reuse rules were checked.
The resultant_research AI develops this argument for Yin; root supplied the broad question and no derivation.
No program, numerical scan or new external theorem is needed below.

The direct inputs are [L296](#single-anti-column-cyclic-realization), [L292's actual anti window](Yin_C_G0545_v1.md#statement), [L66's exact trace-order direct sum](Yin_C_G0243_v1.md#reciprocal-trace-order-index), and [L168's uniform original cyclic cost](Yin_C_G0391_v1.md#bounded-power-degree-escape).
L168 retains its accepted Pri11 statement/proof-inspection boundary.
In particular the trace-field degree, inverse involution and integral direct sum below are REUSED from L66, not newly discovered.
[L74](../ledger/Yin_L_G0074_v1.md#aggregate-cyclic-norm-criterion) already distinguishes scalar content from the complete norm.
[L237](Yin_C_G0570_v1.md#monomial-projection-uniform-margin) already establishes unrestricted scalar positive-margin auxiliaries.
The result here is an exact primitive lattice/finite-group interpretation in the actual anti class, together with an all-input unit-edge realization; it does not rediscover that existence theorem.

A bounded local screen of the adjacent ledgers for primitive remainders, trace orders, cokernels, fixed subrings and integer row spaces found L66's direct sum and L296's rational-scale warning.
L61's commutator cokernel has a different domain; its unimodular pairing is not used here.
The required remaining steps are direct integer-matrix calculations and a substitution into L296's full edge identity.
This screen supplies a workable local route; no general priority or exhaustive absence claim is made.
No Hilbert-90 theorem, maximal-order assertion or Smith-normal-form theorem is imported.

Let P be monic irreducible reciprocal in Z[t], of degree d=2s, constant term1, and nontorsion.
Write P=t^s Q(t+t^-1), let alpha be an original root and tau=alpha+alpha^-1.
Q is its actual monic irreducible trace polynomial of degree s.
Put K=Q(alpha), K_+=Q(tau), O=Z[alpha], B=Z[tau], and m=log M(P)>0.
All original complex and p-adic conjugates, including repeated reductions, are retained.
Fix an integer n>=s.
With U_0=1, U_1=x, U_(j+1)=x U_j-U_(j-1), use

    C_c(t)=sum_(l=1)^n c_l(t^(n+l)-t^(n-l))
          =t^n(t-t^-1)V_c(t+t^-1),
    V_c=sum_(l=1)^n c_l U_(l-1),
    R[:,l]=coefficients of rem_Q U_(l-1),
    H=R R^T, Delta=det H, W=image_R(R^T),
    Pi=R^T H^-1 R.                                      (1)

R has s rows, in the basis1,x,...,x^(s-1).
Its first s columns form a triangular unimodular matrix R_0, since U_(l-1) is monic of degree l-1.
H is positive definite integral and Delta is a positive integer.
As in L296, W is the rational Euclidean row space, even when some trace conjugates are nonreal.
For every1<=k<=n, r_k=R e_k is nonzero by nontorsion, c_k=Pi e_k is nonzero, and

    ell_k=(Pi)_kk=||c_k||^2>0,
    sum_k ell_k=s,
    C_(c_k)(alpha)=alpha^(n-k)(alpha^(2k)-1).             (2)

The subscript k on c_k denotes a VECTOR.
S_2 is the Euclidean norm of all polynomial coefficients; for C_c it is sqrt(2)||c||.
The effective coefficient support is rho=S_1^2/S_2^2, with full coefficient l1 norm S_1.
This rho is not a mean degree.

<a id="anti-row-integral-lattice"></a>
### 2. The exact integral row lattice and its primitive norm

The first s columns in(1) give the exact equality

    W intersect Z^n=R^T Z^s,
    content(R^T w)=content(w) for w in Z^s.               (3)

Indeed, if R^T w is integral for a real w, its first s coordinates R_0^T w are integral.
The inverse of R_0^T is integral, hence w is integral.
For integral w every common divisor of w divides R^T w, and every common divisor of R^T w divides R_0^T w and then w.
This includes rational directions whose first presentation used denominators.

For w in Z^s let v_w(x) be the degree-below-s polynomial with coefficient vector H w.
Then R(R^T w)=H w, so at every original root

    C_(R^T w)(alpha)=alpha^n(alpha-alpha^-1)v_w(tau),
    Res(P,C_(R^T w))
       =P(1)P(-1) Norm_(K_+/Q)(v_w(tau))^2,
    S_2(C_(R^T w))^2=2 w^T H w.                         (4)

For the sign, product_i alpha_i=1 and product_i(alpha_i-alpha_i^-1)=product_i(alpha_i^2-1)=P(1)P(-1), since d is even.
Each trace conjugate occurs exactly twice.
If w!=0, H w!=0 and its polynomial has degree below the irreducible Q, so its value and norm are nonzero.
Primitive w gives a primitive C by(3), with no assertion that its leading coefficient is1.
The auxiliary's actual degree is at most2n, and every leading, monomial and exceptional-root factor remains present.

<a id="primitive-column-cokernel-order"></a>
### 3. An integer order behind every primitive column

Define delta_k=content(r_k)>0 and the primitive integral vector u_k=r_k/delta_k.
We also write u_k(x) for its degree-below-s polynomial.
Set

    v_k=adj(H) u_k, gamma_k=content(v_k),
    L_k=Delta/gamma_k, w_k=v_k/gamma_k.                   (5)

These are nonzero, and gamma_k DIVIDES Delta.
Indeed H v_k=Delta u_k implies that gamma_k divides every coordinate of Delta u_k; a Bezout integer combination of the primitive coordinates u_k gives gamma_k|Delta.
Hence L_k is a positive integer, w_k is a primitive integral vector, and H w_k=L_k u_k.

Equivalently, L_k is EXACTLY the additive order of u_k in the finite group Z^s/H Z^s.
Finiteness follows directly from Delta Z^s subset H Z^s.
If L' u_k=H z for an integral z, then z=(L'/L_k)w_k.
Since w_k is primitive, this is integral only when L'/L_k is an integer, again by a Bezout combination.
Conversely all such multiples work.
This is a proved order characterization, not a determinant treated as uncharged norm income.

Since H^-1 r_k=(delta_k/L_k)w_k, the EXACT primitive column is

    q_k=L_k/delta_k>0 rational,
    F_k=C_(R^T w_k)=C_(q_k c_k),
    F_k(alpha_i)=L_k alpha_i^n(alpha_i-alpha_i^-1)u_k(tau_i),
    Res(P,F_k)=L_k^d P(1)P(-1)
                            Norm_(K_+/Q)(u_k(tau))^2,
    S_2(F_k)^2=2(L_k/delta_k)^2 ell_k.                   (6)

Primitivity follows from(3).
This agrees with L296's q=Delta/content(R^T adj(H) r_k): by(3) that content is delta_k gamma_k.
In general delta_k need not divide L_k; q_k remains genuinely rational.

Every factor multiplying L_k in the root-value identity(6) is integral in the ACTUAL order O.
More precisely,

    F_k belongs to (P,L_k) in Z[t],
    v_p(F_k(alpha_i))=v_p(L_k)
         +v_p(alpha_i-alpha_i^-1)+v_p(u_k(tau_i))
       >=v_p(L_k) for every original p-adic root alpha_i. (7)

For the ideal assertion, alpha^n(alpha-alpha^-1)u_k(tau) has an integral polynomial representative in O, because P is monic with unit constant term.
Subtract L_k times this representative from F_k and divide by the monic P.
The quotient is integral and the remainder vanishes.
The valuations use v_p(p)=1; every other factor in(7) is integral at each original root.
Summing over all d labels gives precisely the valuation of(6), including ramification and repeated reductions.
There is no index-prime assumption or replacement of individual depths by an average.

The full all-root scalar income is d log L_k.
After paying the EXACT coefficient energy its normalized remainder is

    log L_k-log S_2(F_k)
       =log delta_k-(1/2)log(2ell_k).                    (8)

For a minimum-diagonal index ell_k<=s/n this is at least(1/2)log[n/(2s)].
Thus the specific L296 column has a genuine all-root integer floor, at the primes dividing L_k, despite its possibly rational q_k.
This is not necessarily a dyadic floor.
It sharpens the finite-place interpretation of that already established positive-margin auxiliary, without improving scalar existence.
When n>2s the right side is positive, forcing L_k>=2 because a nonzero integral F_k has S_2(F_k)>=1.

All residual factors are retained in(6).
With Z_(2k)=|Res(P,t^(2k)-1)| one has exactly

    Z_(2k)=delta_k^d |P(1)P(-1)|
                          |Norm_(K_+/Q)(u_k(tau))|^2.   (9)

In particular delta_k^d divides Z_(2k).
This does NOT assert L_k^d|Z_(2k): L_k is an order modulo the coefficient Gram lattice, not the multiplicative order of alpha modulo a prime.
Every original exponent2k remains separate.
No income at different times is summed.

<a id="near-one-primitive-trace-remainders"></a>
### 4. What small TOTAL measure actually forces

Fix C>=1 and take s<=n<=C s.
Along any hypothetical sequence of the actual inputs above with m->0, L168 gives uniformly for1<=k<=n

    log Z_(2k)/d=o(1), since 2k<=2n<=C d.
    Thus delta_k=1 for EVERY k<=n,
    once m is sufficiently small in terms of C.         (10)

This is discrete: delta_k>=2 would give log Z_(2k)/d>=log2 by(9).
Uniform convergence excludes it simultaneously for all k, with one threshold depending on C only.
No near-one sequence is constructed.
Powered degree loss is already paid by L168's actual degree/height proof; its accepted Pri11 theorem is not strengthened or re-audited here.

Consequently ALL these primitive scales in the actual near-one domain satisfy

    q_k=L_k in Z_(>0),
    F_k(alpha_i)=L_k alpha_i^(n-k)(alpha_i^(2k)-1),
    log|Res(P,F_k)|/d=log L_k+o(1),
    log L_k-log S_2(F_k)=-(1/2)log(2ell_k).               (11)

This does not make L296's rational-scale warning false on general inputs.
The weaker conclusion that the denominator eventually disappears also follows immediately from its b^d|Z_(2k).
The changed information here is the explicit L_k and primitive trace vector, not that simple corollary in isolation.

For n=ceil(C s) with fixed C>2, replace C by C+1 in(10).
Removing a monomial from F_k changes no original resultant, S_2, rho or content.
Its actual degree T<=2n, height<=Delta as retained in L296, M(F_k)<=S_2(F_k), rho<=2n, and radial charge Tm/d<=(C+1)m all remain paid.
The complete [L229 coefficient/conjugate inequality](Yin_C_G0570_v1.md#actual-resultant-coefficient-energy-bound) and L296's necessary lower cost for rho remain applicable.
Nothing here bounds rho epsilon((C+1)m) above by a vanishing quantity, or Delta uniformly cheaply.
Thus(10)--(11) do not contradict hypothetical small m or produce same-exponent linear CYCLIC income.
The potentially large d log L_k belongs to the different auxiliary F_k, with its equally real coefficient and conjugate costs.

<a id="whole-signed-edge-trace-parametrization"></a>
### 5. Every actual signed edge comes from the trace order

L66 supplies O=B direct_sum alpha B as B-modules and the nonidentity involution sigma(alpha)=alpha^-1=tau-alpha.
Its integral fixed subring is consequently EXACTLY

    O^sigma=B.                                         (12)

Indeed, for u,v in B, the equality u+alpha v=u+(tau-alpha)v forces (2alpha-tau)v=0.
Here 2alpha-tau=alpha-alpha^-1 is nonzero, so v=0.
There is no appeal to the ring of integers of either field, and(12) is just the direct specialization of the retained direct sum.

Let c be a nonzero integral vector in W and F=C_c.
L296 gives the unique low edge A in Z[t] satisfying

    P F=A-t^N A*, N=2n+1,
    deg A<=d-1, A*=t^(d-1)A(1/t).                     (13)

The reversal has FORMAL degree d-1 even when the actual degree of A drops.
The two coefficient blocks have disjoint supports since N>d-1.
Evaluating at alpha gives

    A(alpha)=alpha^(2(n+s)) A(alpha^-1),
    a:=alpha^(-(n+s)) A(alpha) belongs to B.             (14)

The element a is integral because alpha is a unit; it is sigma-fixed by the first equality and hence belongs to B by(12).
It is nonzero because A!=0 has degree below the irreducible P.

Conversely, for EVERY nonzero a in B, let A_n(a) be the unique integral polynomial of degree below d representing alpha^(n+s) a in O.
This representative exists by monicity and the actual integral direct sum; if a is written as an integer polynomial in tau, negative powers introduced by tau=alpha+alpha^-1 are still integral polynomials in alpha because alpha is a unit.
Then

    A_n(a)(alpha)=alpha^(n+s) a,
    A_n(a)*(alpha)=alpha^(s-n-1) a,
    F_n(a):=[A_n(a)-t^(2n+1)A_n(a)*]/P
                       belongs to Z[t] and is nonzero. (15)

For divisibility it suffices to evaluate the numerator at alpha, where the two terms agree.
Monic division gives an integral quotient.
The numerator is nonzero because the two edge blocks are disjoint and A_n(a)!=0.
It is anti-reciprocal at formal degree2n+d, so F_n(a) is anti-reciprocal at formal degree2n and has a unique expression C_c with c in Z^n.

This c actually belongs to W.
The middle coefficient band of P F_n(a), from d through2n, vanishes by construction.
For each1<=j<=n-s, the coefficient inner product of F_n(a) with P(t)(t^(n-s+j)-t^(n-s-j)) is therefore zero: by reciprocal P these are exactly the coefficients at n+s+j and n+s-j of P F_n(a).
These relation polynomials span the full anti kernel of R, since the trace multiples of Q have dimension n-s.
Thus c is orthogonal to ker R, hence lies in W.
For n=s there are no such relations and W=R^n, which is the same conclusion.
This explicitly proves the converse realization, rather than assuming every low-degree seed can be freely assigned an actual column origin.

Extending both maps by zero, equations(14)--(15) define inverse Z-linear bijections

    B <--> {C_c : c in W intersect Z^n},
    a |-> F_n(a),
    content(a)=content(A_n(a))=content(F_n(a)).          (16)

Here content(a) is the gcd of its coefficients in1,tau,...,tau^(s-1).
To prove the content assertion, the L66 direct sum makes these basis vectors, together with their alpha multiples, an integral basis of O.
Thus content in B equals content in O.
Multiplication by alpha^(n+s) is an invertible integral map of O and preserves content, as does passage to its ordinary power basis, giving equality with content(A_n(a)).
Finally the two disjoint blocks in(15) show that the numerator has the same content as A_n(a).
Multiplication by the primitive monic P preserves content: after division by any common prime power, reduction modulo that prime is a product of two nonzero polynomials over a field.
This proves equality with content(F_n(a)), without losing a scalar or a prime at an index divisor.

The COMPLETE original norm of the edge is now fixed exactly:

    Res(P,A_n(a))=Norm_(K/Q)(alpha^(n+s)a)
                 =Norm_(K_+/Q)(a)^2>=1.                 (17)

Norm_K(alpha)=1, and the trace norm is repeated twice.
The signed resultant here is positive; this is different from the possibly negative P(1)P(-1) in the auxiliary norm(6).
At every original p-adic root, v_p(A_n(a)(alpha_i))=v_p(a(tau_i)), since alpha_i is a unit.
These are equal on the inverse pair and retain all original multiplicities.
Formula(17) makes no assertion that the edge is monic, that a is a unit, or that its individual complex conjugates are small.

Combining(3) and(16), the map from w in Z^s to the trace coefficient vector of its edge element a is an integral unimodular matrix E_n.
This requires no independent determinant computation: both maps are Z-linear bijections of the indicated integral lattices, so E_n and its inverse have integer entries.
Accordingly the full auxiliary norm uses the trace vector H w in(4), whereas the full EDGE norm uses E_n w in(17), and the energy is2 w^T H w.
Keeping these three objects distinct is essential.
Selecting a trace unit constrains the edge norm; it does not preserve the auxiliary norm or its coefficient energy.
No height or operator-norm bound for E_n or E_n^-1 is inferred from unimodularity.

<a id="unit-edge-all-input-obstruction"></a>
### 6. Universal unit edges and an exact complete-cost control

Take a=1 in(15).
For EVERY actual input P in this paper and EVERY n>=s there is a primitive nonzero integral anti polynomial F_n(1) in the actual row space W, with edge

    A_n(1)=rem_P(t^(n+s)),
    A_n(1)(alpha_i)=alpha_i^(n+s),
    Res(P,A_n(1))=1.                                  (18)

Thus a proposed strictly positive edge-norm income for EVERY primitive admissible edge fails on each actual input, including on any near-one input if such inputs exist.
This is an all-input exact obstruction, not just a control at one fixed measure.
It does NOT say that F_n(1) is a single paired-monomial projection, or the minimum-diagonal selected column from Section3.
It is an actual integral direction in W, equal to its own projection, with the complete edge identity.
A conjecture restricted to that smaller selected class requires a separate argument.

All complex and leading costs in(18) remain real.
In particular

    sum_i log^+|A_n(1)(alpha_i)|=(n+s)m.                (19)

This equality charges evaluation at all ORIGINAL conjugates, not the auxiliary Mahler measure.
For any actual A=b product_j(t-z_j), its full measure is |b| product_j max(1,|z_j|), and that quantity is NOT determined by Res(P,A)=1.
Likewise the auxiliary F has the complete L296 factorization after removing its monomial: beta(t^2-1) times all quadratic factors from its trace polynomial.
Its leading beta, every exterior pair, actual degree, coefficient energy and rho are retained.
Neither(18) nor the low edge degree d-1 provides an upper estimate paying the L229 coherence term.

There is an explicit all-window nontorsion control in which the entire selected class does have unit edges, but it pays growing leading expense.
Reuse L296's actual irreducible P=t^2-a t+1, a an integer>=3, and alpha=(a+sqrt(a^2-4))/2.
Set r_l=U_(l-1)(a), H_n=sum_(l=1)^n r_l^2.
Here s=1, every primitive column is the same

    F_n=sum_(l=1)^n r_l(t^(n+l)-t^(n-l)),
    A_n=-r_n+r_(n+1)t,
    P F_n=A_n-t^(2n+1)A_n*, A_n*=t A_n(1/t),
    A_n(alpha)=alpha^(n+1), Res(P,A_n)=1,
    M(A_n)=r_(n+1), M(F_n)=r_n.                       (20)

For the edge, multiply P into the displayed F_n and use r_(l+1)=a r_l-r_(l-1), r_0=0, r_1=1: every middle coefficient cancels and the low coefficients are -r_n,r_(n+1).
The identity alpha r_(n+1)-r_n=alpha^(n+1) follows directly from r_l=(alpha^l-alpha^-l)/(alpha-alpha^-1).
The only root of A_n is r_n/r_(n+1) in(0,1), so its complete Mahler measure is its leading coefficient r_(n+1).
The full M(F_n)=r_n and circle-root assertion are precisely L296's retained all-window proof, not a fresh root-count argument.
These measures grow at the fixed-input exponential rate log alpha; the norm1 edge does not make them cheap.

For every column k here, delta_k=r_k, u_k=1, L_k=H_n and q_k=H_n/r_k.
In particular a=3,n=2,k=2 gives delta_k=3, L_k=10, q_k=10/3, and the actual primitive polynomials

    F=3t^4+t^3-t-3, A=-3+8t,
    Res(P,F)=-500, S_2(F)^2=20,
    F(alpha_i)=10 alpha_i^2(alpha_i-alpha_i^-1),
    Res(P,A)=1, M(A)=8, M(F)=3.                       (21)

All these values follow by direct substitution into the displayed formulas; no computation was run.
The new scalar floor10 is at primes2 and5 and is valid at every original root, whereas the old q=10/3 is rational.
The complete original resultant is negative, and both actual degrees4 and1 and both leading costs are explicit.
This control is at fixed positive TOTAL m=log((3+sqrt5)/2); its particular values cannot disprove an input-uniform near-one theorem.
The all-input assertion(18) has the broader admissible-row-space scope stated there.

<a id="anti-column-order-cost-boundary"></a>
### 7. What changes, and the remaining joint cost

The exact primitive column is now governed by two distinct arithmetic data: the content delta_k of a cyclic TRACE remainder and the additive order L_k of its primitive class modulo the actual Gram lattice H Z^s.
Equations(5)--(9) give an integer all-root floor and its fully paid energy, with no common-time substitution.
Small TOTAL m forces delta_k=1 at all degree-linear k, but does not make L_k, Delta, the coefficient l1 norm or the conjugate correlation cheap.
The uniform scalar margin of L237/L296 remains an established input, not a newly solved existence gate.

The signed edge class has an exact integral parametrization by the trace order, preserving primitive content and squaring its whole norm.
The choice a=1 rules out an edge-norm income lower bound across this entire class on EVERY actual input.
The strongest useful next discriminator is consequently a SELECTED-column restriction on the associated a, or a joint inequality involving both its unit-sized norm and the full energy/leading/conjugate distribution.
Simply demanding edge norm growth, counting circle roots, or adding the L_k income while omitting its coefficient cost cannot provide that discriminator.
No upper coherence bound, actual near-one family, input-uniform Mahler gap, finite-time return conclusion or coverage of a changed auxiliary class is asserted.

The argument applies to all irreducible reciprocal nontorsion units, including multiple expanding conjugates, with the original d=2s throughout.
All equations concern the actual orders O and B.
Formal degrees in(13)--(16) do not replace actual auxiliary degrees when charging Tm/d.
Endpoint factors, trace norms, prime multiplicities and integral contents remain explicit.
The torsion case is not used to infer nonzero cyclic values or the uniform limit(10).


## Current assessment
[Selected decision](#decision-isolated-whole-review-adoption-20261022)

## Assessment history

### Decision complete-home-open

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:30 |
| status | open |
| reason | Register the precise complete retained mathematics with every real hypothesis, original cost, source/native/negative limit and frozen input; actual current whole checking follows separately. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Complete enlarged anti class](Yin_C_G0545_v1.md#statement) | Actual real row/quotient dimension, U remainder matrix and enlarged anti coefficient/norm conventions only; original degree-d class is distinct. |
| dependency | [Complete coefficient/projection tools](Yin_C_G0570_v1.md#statement) | Original nonzero-resultant coefficient bound and actual small-h domain, full trace-projection existence mechanism and signed partial-orthogonality method; no new generic mechanism claimed. |
| dependency | [Actual cyclic-cost theorem](Yin_C_G0391_v1.md#bounded-power-degree-escape) | Uniform original-degree linear-time cyclic norm decay with actual powered degree and accepted Pri11 boundaries. |
| dependency | [Actual trace-order direct sum](Yin_C_G0243_v1.md#reciprocal-trace-order-index) | Exact monogenic O=B direct_sum alpha B, degree-two inversion and integral-basis/content scope, without maximal-order/total-reality assumptions. |
| dependency | [Actual odd-prime radical inputs](Yin_C_G0463_v1.md#statement) | Exact irreducible t^(2p)-3t^p+1 degree2p, p odd prime>=3, all roots and fixed positive total measure. |
| support | [Original complete column proof/input](../ledger/Yin_L_G0296_v1.md#complete-retained-proof-and-review) | Full Sections1--8/equations1--20, actual2026-10-10T05:54 freeze and2026-10-10T05:55 nonzero clarification, both all-parameter controls, original author/source/no-program limits and R195. |
| support | [Original complete order/edge proof/input](../ledger/Yin_L_G0300_v1.md#complete-retained-proof-and-review) | Full Sections1--7/equations1--21 and unnumbered E_n consequence; actual2026-10-10T06:27 author whole self-check and R199 original inputs/limits. |

### Decision complete-current-whole-self-adoption

| Field | Value |
| --- | --- |
| date | 2026-10-22T19:33 |
| status | proved |
| reason | Adopt the entire actual anti object after complete current Statement and BOTH entire proof chains were actually checked under SELF, preserving all column/whole-row/torsion distinctions, full prime/root/content/energy/radial costs and original negative/source limits. No independent review or research resumption is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Complete enlarged anti class](Yin_C_G0545_v1.md#statement) | Actual real row/quotient dimension, U remainder matrix and enlarged anti coefficient/norm conventions only; original degree-d class is distinct. |
| dependency | [Complete coefficient/projection tools](Yin_C_G0570_v1.md#statement) | Original nonzero-resultant coefficient bound and actual small-h domain, full trace-projection existence mechanism and signed partial-orthogonality method; no new generic mechanism claimed. |
| dependency | [Actual cyclic-cost theorem](Yin_C_G0391_v1.md#bounded-power-degree-escape) | Uniform original-degree linear-time cyclic norm decay with actual powered degree and accepted Pri11 boundaries. |
| dependency | [Actual trace-order direct sum](Yin_C_G0243_v1.md#reciprocal-trace-order-index) | Exact monogenic O=B direct_sum alpha B, degree-two inversion and integral-basis/content scope, without maximal-order/total-reality assumptions. |
| dependency | [Actual odd-prime radical inputs](Yin_C_G0463_v1.md#statement) | Exact irreducible t^(2p)-3t^p+1 degree2p, p odd prime>=3, all roots and fixed positive total measure. |
| support | [Original complete column proof/input](../ledger/Yin_L_G0296_v1.md#complete-retained-proof-and-review) | Full Sections1--8/equations1--20, actual2026-10-10T05:54 freeze and2026-10-10T05:55 nonzero clarification, both all-parameter controls, original author/source/no-program limits and R195. |
| support | [Original complete order/edge proof/input](../ledger/Yin_L_G0300_v1.md#complete-retained-proof-and-review) | Full Sections1--7/equations1--21 and unnumbered E_n consequence; actual2026-10-10T06:27 author whole self-check and R199 original inputs/limits. |
| review | [Actual complete current SELF](../audits/reviews/Yin_R_G0754_v1.md#actual-anti-orders-and-edges-whole-self) | Entire Statement and both complete Arguments, every exact selected interface and all original correction/source/no-program boundaries. |


### Decision isolated-whole-review-adoption-20261022

| Field | Value |
| --- | --- |
| date | 2026-10-22T21:00 |
| status | proved |
| reason | Adopt the exact complete current Statement and entire Argument after the actual isolated whole review completed2026-10-22T20:49 UTC, with all original domains, costs, failed/negative scopes, source depth and finite-evidence limits retained. The dated original reviews and current SELF findings keep their actual inputs and relationships; this decision neither backfills old review acts nor resumes research. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Complete statement](#statement) | Every domain, parameter, quantifier, actual input, cost and negative qualification in the complete statement above. |
| argument | [Entire argument](#argument) | The complete original mathematical proof below, with all original source/evidence/author/failed-scope boundaries retained at their actual inputs. |
| dependency | [Complete enlarged anti class](Yin_C_G0545_v1.md#statement) | Actual real row/quotient dimension, U remainder matrix and enlarged anti coefficient/norm conventions only; original degree-d class is distinct. |
| dependency | [Complete coefficient/projection tools](Yin_C_G0570_v1.md#statement) | Original nonzero-resultant coefficient bound and actual small-h domain, full trace-projection existence mechanism and signed partial-orthogonality method; no new generic mechanism claimed. |
| dependency | [Actual cyclic-cost theorem](Yin_C_G0391_v1.md#bounded-power-degree-escape) | Uniform original-degree linear-time cyclic norm decay with actual powered degree and accepted Pri11 boundaries. |
| dependency | [Actual trace-order direct sum](Yin_C_G0243_v1.md#reciprocal-trace-order-index) | Exact monogenic O=B direct_sum alpha B, degree-two inversion and integral-basis/content scope, without maximal-order/total-reality assumptions. |
| dependency | [Actual odd-prime radical inputs](Yin_C_G0463_v1.md#statement) | Exact irreducible t^(2p)-3t^p+1 degree2p, p odd prime>=3, all roots and fixed positive total measure. |
| support | [Original complete column proof/input](../ledger/Yin_L_G0296_v1.md#complete-retained-proof-and-review) | Full Sections1--8/equations1--20, actual2026-10-10T05:54 freeze and2026-10-10T05:55 nonzero clarification, both all-parameter controls, original author/source/no-program limits and R195. |
| support | [Original complete order/edge proof/input](../ledger/Yin_L_G0300_v1.md#complete-retained-proof-and-review) | Full Sections1--7/equations1--21 and unnumbered E_n consequence; actual2026-10-10T06:27 author whole self-check and R199 original inputs/limits. |
| review | [Actual isolated whole finding](../audits/reviews/Yin_R_G0776_v1.md#current-anti-columns-orders-and-edges) | The complete current fixed Statement and entire Argument, all necessary mathematical interfaces and actual finite-evidence checks at2026-10-22T20:49 UTC; independently reviewed in the disclosed isolated arrangement, without native discovery/reviewer reruns. |

