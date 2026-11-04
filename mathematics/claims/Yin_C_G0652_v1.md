---
author: Yin
---
# A uniform complete-support norm character and exclusion of monomial complements

Human author Yin.
Root proposed the complete primitive-factor norm formulas, the high-branch norm mechanism, the B_(5^j) calibration and the bounded multiplicity-twenty factor classification.
The same_trace contributor derived and checked the formal-unit quotient, complete-factor bridge, norm precision, trace cancellation, calibrated target formula and necessary congruence, and completed the full argument below.
Both are mathematical contributors; neither is an independent reviewer of this new result.
The [active all-strategy Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23) authorizes this continuation.
Focused reuse inspected the complete trace/divisor identities in C608/C609v2, the combined finite-group method in C621v2/C640, and the exact actual factorization and full CRT of C649/C650.
Targeted local Claim/draft and source-content searches found no retained chi-norm or formal-unit cokernel result with the needed scope.
The leading-coefficient elimination below develops the available algebraic group method directly; no external Coleman or Witt theorem is asserted or used.
No native mathematical computation, growing quotient scan or support-order cutoff is used.
The [D1 norm section](../drafts/Yin_D_G0001.md#uniform-complete-support-norm-candidate) is extraction provenance, not a logical input.
This complete statement and argument are initially open for fresh isolated whole mathematical review.

## Statement

### The formal-unit character and all-order complete-support necessity

Put phi(X)=1+X+X^2 and chi(X)=Xphi(X)^2 over F_2, and let x(t) be the unique formal inverse of chi at0.
Let U=1+tF_2[[t]] with its t-adic topology, and define

    Theta(h)(t)=h(t)^5/h(chi(t)).                              (N1)

There is a unique continuous multiplicative-to-additive homomorphism ell:U->Z_2 with

    ker ell=Theta(U), ell(1+t)=1,
    U=Theta(U) times (1+t)^(Z_2),                              (N2)

where the last expression is an internal direct product and Theta is injective.
For every integer N>=1, the value of ell(h) modulo 2^ceil(log_2 N) is determined by h modulo t^N.
In particular

    ell(h(chi))=5ell(h), ell(h(x))=ell(h)/5.                   (N3)

For positive odd n let B_n be the monic polynomial of traces z+z^(-1) of all nonidentity n-th roots in an algebraic closure of F_2, one trace per inverse pair, with B_1=1.
Let W_n be the corresponding complete primitive order-n trace polynomial for odd n>1.
Thus B_n=product_(d dividing n,d>1)W_d and W_5=phi.
For n^*=(-1)^((n-1)/2)n one has

    ell(phi)=-1, ell(B_n)=(1-n^*)/4.                          (N4)

For Q=2^s>=2 put

    h_Q(X)=1+sum_(i=0)^(s-1)X^(Q-2^i).

Then h_Q=B_(2Q-1) and ell(h_Q)=Q/2.

Write N_chi(p)(t) for the algebraic norm of p(X) from F_2(X) over F_2(t), t=chi(X).
For any finite complete product

    V=X^e product_(n odd,n>1,n!=5) W_n^(b_n),
    e,b_n nonnegative integers,

the endpoint cancels and

    N_chi(V)(t)/V(t) in Theta(U).                            (N5)

All odd support orders and all finite multiplicities are allowed.
No hypothesis that the orders are coprime to5 or3 is imposed.

### Uniform obstruction for the full homogeneous targets

Let m>=1 and let Q be a power of2 with2m<Q<5m.
Let H in F_2[t] have H(0)=1 and5deg H<5m-Q.
Let Sigma(t) be any specified series in t^(2m)F_2[[t]], and define the full formal unit

    Ltilde(t)=[phi(t)^(7m)H(t)h_Q(x(t))]^(-1).

Choose N_0 with2^(N_0)>=8m and2^(N_0) congruent to Q modulo3, and put beta=X^(2^(N_0)) modulo phi^(8m).
Let Y in F_2[X] be prime to Xphi and satisfy the exact two-primary conditions

    Y=Ltilde(X^2) modulo X^(4m),
    Y=X^(5m-7Q)H(chi)^(-7)
       [1+beta X^(-6Q)H(chi)^(-6)Sigma(chi)]
                                             modulo phi^(8m). (N6)

Every high-primary denominator is a unit there.
Suppose the SAME polynomial

    V=X^(m+Q)YH(chi)

has a complete product factorization of the form in (N5).
No completeness assumption is made about Y or H separately.
Put M=2^ceil(log_2(4m)), the least power of2 at least4m.
Then

    ell(N_chi(Y)/Y)
       =(-330m+74Q-660ell(H))/25 modulo M,                  (N7)

and the complete-support hypothesis requires

    m+2ell(H)=0 modulo M/2.                                (N8)

Equivalently, m is even and ell(H)=-m/2 modulo M/4.
Division by5 or25 denotes division by an odd unit in Z_2.
The character value in (N7) is determined by the complete CRT class modulo X^(4m)phi^(8m)=chi(X)^(4m), independently of its polynomial representative.
Every Sigma allowed above gives the SAME necessary condition: its full high-branch norm correction vanishes at the stated precision, rather than being discarded as an extra hypothesis.
In particular H=1 is impossible for every m in this theorem.
For nonconstant H, (N8) is necessary only; no complete-support sufficiency or universal degree estimate for ell(H) is claimed.

### The same original characteristic-zero domain

Let P in Z[z] be monic irreducible reciprocal nontorsion with constant coefficient1 and degree d=2r.
For an original root alpha put K=Q(alpha), delta_original=alpha+alpha^(-1), and assume F=Q(delta_original) is totally real.
Let T in Z[X] be its actual monic degree-r minimal polynomial, so P(z)=z^rT(z+z^(-1)) and [K:F]=2.
Define C_p by C_p(z+z^(-1))=z^p+z^(-p), and use the actual integral divided monic remainders

    theta_p=rem_T(T(C_p))/p, p=2,3,5,
    a=theta_2(delta_original), b=theta_3(delta_original),
    c=theta_5(delta_original).

Assume a,b,c are nonzero and, for one s in{1,-1},

    2c^2=3a^5,
    b^2-a^3+s(c^3-2b^5)=0,
    g=c^3-2b^5!=0.

Put G_can=rem_T(theta_5^3-2theta_3^5), w=deg G_can<r, U=T mod2 and R_can=G_can mod2.
Assume the normalized circle Haar integral of log(G_can(z+z^(-1))^2), using the integrable logarithm at circle zeros, is0.
Assume

    ord_phi R_can<ord_phi U,
    ord_psi R_can>=ord_psi U for every irreducible psi dividing U,
                                               psi!=phi.

Let q=2^k be the ACTUAL maximal power of2 for which U is a q-th power, and retain C199's canonical U=U_0^q and R_can=R_0^q.
Write A_0=ord_XU/q=2m with m>=1, and retain the SAME canonical factors

    U_0=X^(2m)phi^(14m)Y,
    R_0=rem_(U_0)(U_0(chi)^3)=X^(2m)Yphi^(12m)B,
    H_0=X^(2m)Y, V_0=H_0B,
    C_00=X^(2m)Y(chi)phi(chi)^(14m), D_0=V_0+C_00^3.

Here B is the unique COMPLETE monic phi-unit complement with deg B<4m, including every saturated surplus and extra remainder factor.
For n>=3 define the integer trace polynomial F_n by Phi_n(z)=z^(phi(n)/2)F_n(z+z^(-1)), with phi(n) Euler's totient.
Keep the actual zero-Haar integer factorization and every original layer

    G_can=V_int product_(b>=0)F_(2^b*5)^(a_b),
    a_b>=0 integers of finite support,
    lambda_0=lambda_1=1, lambda_b=2^(b-1) for b>=2,
    sum_b a_b lambda_b=12mq,
    S_star=sum_(a_b odd,4mq<lambda_b<12mq)
       X^(lambda_b/(2q))(X+1)^(lambda_b/q)
                          phi^(12m-lambda_b/q).

The sign and all other integer factors stay in V_int; no individual a_b is divided by q or reassigned.
The adopted C650 theorem gives a_b=0 for lambda_b>8mq, m even, and the unique homogeneous form

    B=X^(Q-m)H(chi),
    Q a power of2, 2m<Q<5m,
    H(0)=1, 5deg H<5m-Q,

together with C649's full low/high jets and corrected6m root for the SAME actual Y.
In this original domain, (N8) holds and H must be nonconstant.
Thus EVERY monomial-complement branch is excluded, uniformly in m, q, all support orders and all original integer layers.
Furthermore the complete original branches A_0=16 and A_0=20 are excluded by the bounded hand factor classifications below.
Combining these deductions with C650's already adopted prior range gives the necessary remaining set

    A_0 in{24,28,32,36,...}.                                (N9)

There is no claim of existence at any remaining value or of a complete description of the full finite factor image.
All original degree costs remain

    r=q(30m+deg Y),
    w=q(26m+deg Y+deg B),
    r-w=q(5m-Q-5deg H)>0, deg H>=1.                        (N10)

The actual maximal q, nonsquare U_0,R_0, all-primary canonical identity, original fields and characteristic-zero residual constraints are preserved.
No inference of a global square from a local jet, smaller original input, all-primary sufficiency or unrestricted Task completion is made.

## Argument

### 1. A direct triangular quotient of formal units

Every unit u in U has a unique convergent product

    u=product_(r positive odd)(1+t^r)^(a_r), a_r in Z_2.     (P1)

To construct it, inspect coefficients in increasing order n>=1 and write n=r2^j with r odd.
Multiplication by (1+t^r)^(2^j)=1+t^n toggles the coefficient at n without changing lower coefficients.
This chooses each binary digit of every a_r, and the same first-difference argument proves uniqueness.
Only finitely many factors affect a fixed coefficient, so all products converge.

For odd r>=1, chi(t)^r=t^r+t^(r+2)+higher terms.
Also (1+t^r)^5=1+t^r+t^(4r)+t^(5r), and r+2<4r.
Division by the unit 1+chi(t)^r therefore gives the EXACT leading order

    Theta(1+t^r)=1+t^(r+2)+higher terms.                    (P2)

After taking its2^j-th power the order becomes 2^j(r+2).
These orders are distinct and range over precisely the positive integers that are not powers of2.
At any such order there is exactly one pair r,j, namely j the2-adic valuation and r the odd part minus2.

Eliminate the coefficients of u in increasing order using Theta((1+t^r)^(2^j)) at those orders, and using (1+t)^(2^j)=1+t^(2^j) at the remaining power-of-two orders.
The source order r2^j is at least one third of its eliminated order, so the products of sources converge as well as their images.
This produces u=Theta(g)(1+t)^a for g in U and a in Z_2.
If g!=1, its expansion (P1) has a unique least active value2^j(r+2), so Theta(g)-1 has exactly that non-power-of-two leading order.
If a!=0, (1+t)^a-1 has leading order2^(nu_2(a)), a power of2.
They cannot be equal, proving uniqueness, injectivity and the direct product assertion (N2).
Multiplication of decompositions makes ell additive, and ell(1+t)=1.
If u=1 modulo t^N, the elimination begins at order at least N; every binary digit chosen for a therefore has2^j>=N.
Hence ell(u) is divisible by2^ceil(log_2 N), proving continuity and the stated finite precision.
The normalization and kernel uniquely determine ell through the direct product.
Applying it to Theta(h) and composing with x proves (N3).

### 2. Trace polynomials, index continuity and exact calibration

The [complete Laurent identity in C608](Yin_C_G0608_v1.md#argument) is

    B_n(z+z^(-1))=z^(-(n-1)/2)(z^n+1)/(z+1), n positive odd.

It gives B_1=1, B_3=1+X, B_(n+2)=XB_n+B_(n-2), and B_(-n)=B_n when extended to negative odd indices by the same Laurent formula.
The substitution is injective because a nonzero polynomial of degree d has highest positive Laurent exponent d.
The exact [order-five composition identity](Yin_C_G0609_v2.md#argument), also immediate from this formula, is

    B_(5n)=phi B_n(chi).                                    (P3)

For the matrix A=[[t,1],[1,0]] one has A^2=I+tA.
Repeated squaring gives A^(2^v)=I+t^(2^(v-1))A^(2^(v-1)) for v>=1.
The recurrence vector advances by A when its odd index increases by2, and A is invertible over F_2[[t]].
Thus an index increment divisible by2^(v+1) preserves B_n modulo t^(2^(v-1)), for positive or negative odd indices.
In particular B_n depends continuously on its odd2-adic index at every fixed t-adic precision.

Let c=ell(phi).
Applying (N3) to (P3), and starting from B_1=1, gives

    ell(B_(5^j))=((5^j-1)/4)c, j>=0.                       (P4)

The positive powers of5 are dense in1+4Z_2.
Indeed nu_2(5^(2^v)-1)=v+2: it starts with5-1=4, and each squaring multiplies this difference by a factor with valuation1.
Consequently multiplication by5^(2^v) toggles precisely the next binary choice among units congruent to1 modulo4.
Successively choosing the binary digits of an exponent approximates any such unit modulo each power of2; exponents may be taken positive by adding a sufficiently large power of2.
Choose positive j with5^j tending to-3 in Z_2.
The just-proved index continuity gives B_(5^j) tending to B_(-3)=B_3, whose character is1.
Equation (P4) tends to-c, so c=-1.
For arbitrary odd n, the signed integer n^*=(-1)^((n-1)/2)n belongs to1+4Z_2 and B_(n^*)=B_n.
The same approximation proves (N4) with all divisions interpreted in Z_2.

For Q a power of2, the Laurent geometric sum gives

    B_(2Q-1)=1+sum_(j=1)^(Q-1) C_j.

The sum of C_j over odd j from1 to2Q-1 is X^(2Q-1).
To see this exactly, substitute X=z+z^(-1); every binomial coefficient of (z+z^(-1))^(2Q-1) is1 because2Q-1 has all binary digits1, giving exactly those positive and negative odd Laurent powers.
Since C_(2j)=C_j^2, separating odd and even indices gives

    B_(4Q-1)=B_(2Q-1)^2+X^(2Q-1).

This is also the recurrence h_(2Q)=h_Q^2+X^(2Q-1), with common initial value B_1=h_1=1.
It proves h_Q=B_(2Q-1) for every dyadic Q.
For Q>=2, the signed integer associated to2Q-1 is1-2Q, so (N4) yields ell(h_Q)=Q/2.

### 3. The norm of every complete factor, including higher five-orders

The extension F_2(X)/F_2(chi(X)) has degree5, and its polynomial norm is Res_X(chi(X)-t,p(X)).
For clarity this is also the determinant of multiplication by p on the free rank5 algebra with basis1,X,...,X^4 and relation chi(X)=t.
It gives

    N_chi(X)=t,
    N_chi(B_n)=B_n(t)                         if5 does not divide n,
    N_chi(B_n(chi))=B_n(t)^5                  for every odd n. (P5)

For the middle formula, power5 permutes all nonidentity n-th roots and their inverse pairs, and chi sends each trace to the trace of that fifth power.
Thus the resultant, viewed instead as the monic product over the roots of B_n, has precisely the original trace roots with their multiplicities.
The last formula is the determinant of multiplication by a scalar of the rank5 base algebra.

The corresponding primitive formulas are

    N_chi(W_n)=W_n(t)                         if5 does not divide n,
    N_chi(W_(5d))=W_d(t)^4                    if5 does not divide d,d>1,
    N_chi(W_n)=W_(n/5)(t)^5                   if25 divides n,
    N_chi(phi)=t^2.                                        (P6)

For the second formula every primitive d-th root has four primitive5d preimages and one order-d preimage under power5.
For the third, all five preimages of a primitive(n/5)-th root have order n because25 divides n.
Passing to inverse pairs keeps exactly these multiplicities.
The two traces of primitive fifth roots both map to0, proving the last formula.
Thus no high five-order is missing from (P5) or (P6).

All allowed W_n, with n odd,n>1,n!=5, lie in the rational-function multiplicative group generated by the B_n with5 not dividing n and the D_(5n)=B_(5n)/phi=B_n(chi) for all odd n.
Indeed B_n is the product of W_d over d>1 dividing n, and when5 divides n, D_n deletes exactly W_5.
Divisor induction solves for W_n using its corresponding product and smaller allowed divisors.
Every generator and inverse is a unit at X=0 and at phi, even though the induction can use negative exponents.
Combining (P5) and (N1), coprime-five B_n has norm ratio1 and B_n(chi) has norm ratio Theta(B_n).
The endpoint X also has ratio1.
This proves (N5) for every actual finite nonnegative complete product; its Theta witness can even be a finite rational product of B_n.

For V=X^(m+Q)YH(chi), multiplicativity and N_chi(X)=t yield

    N_chi(V)/V=[N_chi(Y)/Y]Theta(H).

Thus the complete-product hypothesis implies N_chi(Y)/Y in Theta(U), and its character is0.
This is the exact bridge for arbitrary H; replacing it by an unproved complete-factor assertion about Y would be invalid.

### 4. The full rank-five local norm and every correction term

Let A=F_2[[t]][X]/(chi(X)-t).
The formal inverse x(t) is its simple root tending to0; it exists uniquely by solving coefficients, since chi(0)=0 and chi'(0)=1.
Dividing by X-x(t) leaves a monic degree4 factor whose reduction at t=0 is phi^2.
The two factors are coprime modulo t, so the algebra splits as a direct product of its simple branch F_2[[t]] and a free rank4 algebra A_high.
On A_high, X is a unit, and

    N_high(X)=t/x(t)=phi(x(t))^2.                           (P7)

The reduction of A_high modulo t is F_2[X]/phi^2.
Multiplication by any element on this reduction preserves its phi filtration; both two-dimensional successive quotients are F_4 with the same residue multiplication.
Its four-dimensional trace is therefore twice the F_4/F_2 trace, hence0.
It follows that Tr_high(a) lies in tF_2[[t]] for EVERY a in A_high.

There is a unique cube-one unit tau in A_high with residue X^2 modulo phi.
Lift first through the nilpotent phi ideal and then successively through powers of t; the derivative of z^3-1 at that unit is z^2, a unit, so each correction is uniquely determined.
The exact cube-one lift of beta in (N6) is tau^(2Q), because its residue is X^(4Q)=X^Q.
Both lift the same residue and the defining derivative is a unit, so this agrees with the specified beta at every required finite precision.
The trace/Frobenius identity gives

    Tr_high(beta X^(-6Q))
      =Tr_high((tau X^(-3))^(2Q))
      =Tr_high(tau X^(-3))^(2Q) in t^(2Q).                 (P8)

For example the identity follows in the generic separable algebra by summing conjugates and applying Frobenius; the generic algebra is separable because chi'(X)=phi(X)^2 is coprime to chi(X)-t over F_2(t).
It then holds in the free integral algebra itself.

Modulo t^(4m), Sigma^2=0.
The determinant of multiplication by1+Sigma a is therefore1+Sigma Tr_high(a), since every determinant term with at least two factors Sigma vanishes.
For a=beta X^(-6Q)H(t)^(-6), (P8) makes even the linear term vanish, because2Q>4m.
Thus the full high-branch correction in (N6) has norm1 modulo t^(4m).
No choice of Sigma in the theorem has been excluded from this argument.
Taking the high norm of the other factors, and multiplying by the simple-branch value, gives

    N_chi(Y)=Y(x(t))phi(x(t))^(10m-14Q)H(t)^(-28)
                                                modulo t^(4m). (P9)

The precision is intrinsic: A/(t^(4m)) is F_2[X]/chi(X)^(4m), and its CRT factors are exactly F_2[X]/X^(4m) and F_2[X]/phi^(8m).
Norm determinants and all units in this argument are therefore determined by the FULL class (N6).
No precision was inferred from the phi branch alone, and changing a representative by chi(X)^(4m) does not change the norm modulo t^(4m).

### 5. Evaluation of the obstruction and the monomial exclusion

The low jet gives Y(t)=Ltilde(t)^2 modulo t^(4m), and Y(x(t))=Ltilde(x(t))^2 there, because all coefficients are in F_2.
By (N3), (N4) and ell(h_Q)=Q/2,

    ell(Ltilde)=7m-ell(H)-Q/10,
    ell(Ltilde(x))=ell(Ltilde)/5.

Applying ell to (P9) divided by Y(t), with the exact finite precision from (N2), yields

    ell(N_chi(Y)/Y)
      =2(1/5-1)(7m-ell(H)-Q/10)
         -(10m-14Q)/5-28ell(H)
      =(-330m+74Q-660ell(H))/25 modulo M.

This proves (N7).
Since M is the least power of2 at least4m, one has M/2<4m<=M.
The inequalities2m<Q<5m put the dyadic Q strictly above M/4 and strictly below2M, so Q is M/2 or M.
Consequently74Q is divisible by M.
The vanishing character of the complete product therefore requires330(m+2ell(H))=0 modulo M.
As330=2*165 with165 odd, this is exactly (N8).
Here M>=4, so (N8) first forces m even and then gives the stated residue modulo M/4.
When H=1, its character is0, but0<m<M/2; thus (N8) fails for every m.
This proves the uniform monomial-complement exclusion without any bounded support or degree enumeration.

### 6. Exact return to the original input, layers and degree costs

The adopted [C650 full theorem](Yin_C_G0650_v1.md#decision-whole-reviewed-2026-10-23) applies to precisely the original hypotheses stated here.
It gives all upper a_b=0, the homogeneous classified B, the low jet, and applicability of the full [C649 CRT](Yin_C_G0649_v1.md#decision-whole-reviewed-2026-10-23).
For every actual odd layer that remains in S_star put ell_b=lambda_b/q and define

    Sigma(t)=sum_(a_b odd,4m<ell_b<=8m)t^(6m-ell_b/2).

Each ell_b is a power of2, at its original index b=k+j+1 if ell_b=2^j.
It satisfies6m-ell_b/2>=2m, so Sigma lies in t^(2m).
For each such layer C650's exact identity is

    X^(6m)X^(ell_b/2)(X+1)^ell_b phi^(12m-ell_b)
       =chi^(6m-ell_b/2)(1+phi^ell_b).

Its extra term is X^(6m-ell_b/2)phi^(12m), so

    X^(6m)S_star=Sigma(chi) modulo phi^(12m).

Factor the C649 high jet using B=X^(Q-m)H(chi).
Its leading term is X^(5m-7Q)H(chi)^(-7), and its relative correction is

    beta B^(-6)S_star
      =beta X^(-6Q)H(chi)^(-6)Sigma(chi) modulo phi^(8m).

This is exactly (N6), with every original layer retained.
The corrected root remains Z_0=beta^2B^(-1)(1+beta B^(-6)S_star) modulo phi^(6m), as in C649; the norm argument does not replace or shorten that root equation.

The actual V_0=R_0/phi^(12m)=X^(m+Q)YH(chi) has the complete odd-order product factorization inherited from the SAME zero-Haar integer factorization in [C199](Yin_C_G0199_v4.md#argument).
Reduction of the complete integer trace groups has uniform nonnegative multiplicities on every W_n.
The actual common q divides those reduced multiplicities, and extracting that q-th root preserves their uniformity.
Removing the entire W_5-primary factor leaves the endpoint X and all n!=5 factors with their actual normalized nonnegative multiplicities.
This statement concerns those reduced complete multiplicities, not division of the original integers a_b by q.
It proves the exact complete hypothesis needed for (N5), regardless of whether H or Y individually is complete.
Thus (N8) and the uniform exclusion apply to the SAME original input.
The canonical identities from C650 give (N10) directly after substituting deg B=Q-m+5deg H.
Nothing in the norm argument changes q, canonical remainder degrees, original fields or the nonsquare normalized data.

### 7. The complete hand classifications at A_0=16 and20

For m=8, the only dyadic Q in(16,40) is32, and5deg H<40-32 gives deg H<=1.
The only possibilities are1 and1+t, with character0 and1.
Here M=32 and (N8) requires ell(H)=-4=4 modulo8, so neither possibility survives.
This analytic deduction does not use a full finite-image computation at A_0=16.

For m=10, the only Q in(20,50) is32 and5deg H<18 gives deg H<=3.
Every constant-one monic polynomial of degree at most3 is one of the following EIGHT polynomials:

| H | Degree | ell(H) |
| --- | --- | --- |
| 1 | 0 | 0 |
| W_3=1+t | 1 | 1 |
| W_3^2 | 2 | 2 |
| W_5=1+t+t^2 | 2 | -1 |
| W_3^3 | 3 | 3 |
| W_3W_5 | 3 | 0 |
| W_7=1+t^2+t^3 | 3 | 2 |
| W_9=1+t+t^3 | 3 | -3 |

The only degree1 irreducible with constant1 is1+t; the only irreducible quadratic is phi.
A monic cubic with constant1 has the form1+at+bt^2+t^3; it has no root0 and has no root1 exactly when a+b=1, giving the two displayed cubics.
A reducible cubic is therefore W_3^3 or W_3W_5, proving exhaustiveness without a native search.
The identifications W_7=B_7 and W_9=B_9/B_3 follow from the recurrence and complete divisor identity.
Formula (N4) gives ell(W_7)=2 and ell(W_9)=-2-1=-3; multiplicativity gives every other table entry.
Here M=64, and (N8) requires ell(H)=-5=11 modulo16.
None of the eight values has this residue, excluding the entire A_0=20 branch.
Intersecting these two exclusions with the adopted C650 prior range{16,20,24,...} proves (N9).
This finite hand classification is confined to these proved degree bounds; no assumption about complete factors or character size for general H is used.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-23T23:00 |
| status | open |
| reason | Register the full uniform chi-norm/formal-unit theorem, exact2-adic calibration, all-order complete-support bridge, full rank-five norm cancellation and explicit H-character congruence. The complete original domain excludes every monomial complement and the entire A0=16/20 branches, leaving the necessary range{24,28,32,...} with unchanged q/layers/costs. The proof is analytical and author-checked; fresh isolated whole mathematical review remains required. No unrestricted completion, arbitrary H completeness, full-image sufficiency or original realization is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire uniform statement](#statement) | N1--N10, all formal-unit and complete-support quantifiers, full target precision, original hypotheses/layers/costs, uniform monomial exclusion and exact A0=16/20 consequences. |
| argument | [Whole analytical proof](#argument) | All seven sections: direct triangular quotient, exact calibration and sparse identity, all-order norm and factor bridge, rank-four trace and correction cancellation, finite precision and residue, original return and complete bounded hand classifications. |
| dependency | [Complete trace and divisor identities](Yin_C_G0608_v1.md#argument) | B_n/W_n definitions, exact Laurent identity, recurrence, squarefreeness and full divisor support; no finite group result is used. |
| dependency | [Exact five-order composition](Yin_C_G0609_v2.md#argument) | B_(5n)=phi B_n(chi) for all odd n, including all higher five-orders. |
| dependency | [Actual complete group bridge](Yin_C_G0199_v4.md#argument) | SAME integer zero-Haar factorization, complete reduced groups and actual q-th-root multiplicities of V0; no assumption that Y or H individually is complete. |
| dependency | [Adopted actual homogeneous conclusion](Yin_C_G0650_v1.md#statement) | Exact original domain, canonical q/U0/R0/B, upper integer layer vanishing, complete Q/H classification, precise layer identity, original costs and prior remaining range. |
| dependency | [Adopted full homogeneous CRT](Yin_C_G0649_v1.md#statement) | Complete low/high jets and corrected6m root at full8m precision for the SAME Y after homogeneity; all correction layers are retained in the new norm calculation. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T23:10 |
| status | proved |
| reason | Adopt the entire N1--N10 theorem after main reading of complete C652 and isolated whole R863. The convergent formal-unit quotient, exact2-adic calibration, all-order complete norm bridge, full rank-five precision and high trace/correction calculation prove m+2ell(H)=0 modulo M/2 for the SAME complete V0, without separate completeness of H or Y. Every monomial complement is excluded uniformly; exhaustive hand classifications exclude A0=16 and20, leaving the precise necessary range{24,28,32,...}. All actual q, integer layers, canonical fields/factors/degrees and source limits remain. No native computation, sufficiency for arbitrary H, entire finite-image characterization, original realization or unrestricted Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire uniform statement](#statement) | N1--N10, all formal-unit and complete-support quantifiers, full target precision, original hypotheses/layers/costs, uniform monomial exclusion and exact A0=16/20 consequences. |
| argument | [Whole analytical proof](#argument) | All seven sections: direct triangular quotient, exact calibration and sparse identity, all-order norm and factor bridge, rank-four trace and correction cancellation, finite precision and residue, original return and complete bounded hand classifications. |
| dependency | [Complete trace and divisor identities](Yin_C_G0608_v1.md#argument) | B_n/W_n definitions, exact Laurent identity, recurrence, squarefreeness and full divisor support; no finite group result is used. |
| dependency | [Exact five-order composition](Yin_C_G0609_v2.md#argument) | B_(5n)=phi B_n(chi) for all odd n, including all higher five-orders. |
| dependency | [Actual complete group bridge](Yin_C_G0199_v4.md#argument) | SAME integer zero-Haar factorization, complete reduced groups and actual q-th-root multiplicities of V0; no assumption that Y or H individually is complete. |
| dependency | [Adopted actual homogeneous conclusion](Yin_C_G0650_v1.md#statement) | Exact original domain, canonical q/U0/R0/B, upper integer layer vanishing, complete Q/H classification, precise layer identity, original costs and prior remaining range. |
| dependency | [Adopted full homogeneous CRT](Yin_C_G0649_v1.md#statement) | Complete low/high jets and corrected6m root at full8m precision for the SAME Y after homogeneity; all correction layers are retained in the new norm calculation. |
| review | [Independent entire formal-unit norm finding](../audits/reviews/Yin_R_G0863_v1.md#whole-formal-unit-norm-obstruction-finding) | Whole N1--N10 and all seven proof sections, exact convergence/topology/calibration, all-order norm and actual V0 bridge, complete two-primary determinant precision and every correction, exact congruence and exhaustive hand classifications, with original costs and all source limits. |

