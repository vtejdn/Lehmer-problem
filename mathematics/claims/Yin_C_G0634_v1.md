---
author: Yin
---
# Uniform Laurent support constraint and normalized multiplicity-ten exclusion

Human author Yin.
Root supplied the exact A_0=10 original-layer projection and requested a structural analysis of the full complement rather than an extrapolation from a prior multiplicity.
The same_trace contributor derived and checked the parameter-uniform Laurent support lemma, the two exhaustive multiplicity-five trace-space calculations, and the complete original A_0=10 application below.
Both are mathematical contributors; the new proof requires a fresh isolated whole review.
The work continues under the [active all-strategy Task](../tasks/Yin_T_G0001_v1.md#decision-all-strategies-resume-2026-10-23).
Focused local reuse inspected the exact C197/C199 normalization and gate, C609v2's actual parity theorem, C630's full complement/scaling boundaries, and C608's whole-trace Laurent identities.
The existing small cube classifications do not cover this new parameter-uniform support constraint or the multiplicity-ten conclusion.
The trace identities below are reused at their exact polynomial scope; all finite-field projections, local orders, degree arguments and two small tables are proved explicitly.
No external source theorem, numerical scan, new J or native mathematical calculation is used.

## Statement

### Uniform Laurent support and endpoint constraint

Let m>=1 be any integer.
Put phi=X^2+X+1 and chi=Xphi^2 in F_2[X].
Let f in F_2[X] be nonzero, prime to phi, with

    X^m dividing f,
    deg f<5m.

Let A(t) in F_2[t] be any polynomial with A(0)=1, of unrestricted degree.
Assume

    [f(X)A(chi(X))]^3=1 modulo phi^(4m).        (LS1)

Then there exists sigma in{1,2} such that every nonzero Laurent coefficient of

    F(z)=f(z+z^(-1))

has exponent n congruent to sigma or -sigma modulo5.
Moreover

    ord_X f>=2m.                               (LS2)

The local cube-root constant1 is impossible; the two possible nontrivial constants supply the two choices of sigma as proved below.
This is a necessary condition, not a sufficient criterion for (LS1).
There is no assumption that f is globally square or a complete cyclotomic product.

At m=5, the same hypotheses also force ord_Xf to be EVEN.
Equivalently, there is no monic B prime to phi with deg B<20 and even ord_XB, and no polynomial A(t) with A(0)=1, satisfying

    [X^5 B(X) A(chi(X))]^3=1 modulo phi^20.     (LS3)

This last assertion includes arbitrary auxiliary degree and every auxiliary coefficient.
It is not a claim that odd ord_Xf is impossible for every m, or that all A_0 congruent to2 modulo4 are excluded.

### Entire normalized multiplicity-ten branch

Let P in Z[z] be monic irreducible reciprocal nontorsion, with constant coefficient1 and degree d=2r.
For an original root alpha set K=Q(alpha), delta=alpha+alpha^(-1), and suppose F=Q(delta) is totally real.
Let T in Z[X] be the actual monic degree-r minimal polynomial of delta, so P(z)=z^rT(z+z^(-1)) and [K:F]=2.
Use C_p(z+z^(-1))=z^p+z^(-p) and the actual integral divided monic remainders

    theta_p=rem_T(T(C_p))/p, p=2,3,5,
    a=theta_2(delta), b=theta_3(delta), c=theta_5(delta).

Assume a,b,c are nonzero and, for one s in{1,-1},

    2c^2=3a^5,
    b^2-a^3+s(c^3-2b^5)=0,
    g=c^3-2b^5!=0.

Put G=rem_T(theta_5^3-2theta_3^5), w=deg G<r, U=T mod2 and R_G=G mod2.
Assume the normalized circle Haar integral of log(G(z+z^(-1))^2), using the integrable logarithm at circle zeros, is0.
Assume also

    ord_phi R_G<ord_phi U,
    ord_psi R_G>=ord_psi U for every irreducible psi dividing U,
                                             psi!=phi.

Let q=2^k be the actual maximal power of2 for which U is a q-th power, and retain the canonical U=U_0^q and R_G=R_0^q supplied by C199.
Set A_0=ord_XU/q and add ONLY A_0=10.
There is no such original P,T and residual data.
This covers every complete complement, every original q, all integer cyclotomic layers and arbitrary complete higher5 support on this zero-Haar and unique-unsaturated domain.

Together with the [adopted C630 remaining-range conclusion](Yin_C_G0630_v1.md#statement), the remaining normalized multiplicities on this exact domain are even A_0>=12.
There is no power-of-two restriction.
Multiple unsaturated factors, positive Haar, other original domains and the unrestricted G0001 objective remain outside this exclusion.

## Argument

### Exact local constants and the fifth-root coordinates

Write N=deg f, and work in an algebraic closure of F_2 containing a primitive fifth root xi.
Such a root exists because z^5-1 has five distinct roots in characteristic2.
For j=1,2,3,4 put x_j=xi^j+xi^(-j).
The exact identities

    X(z)=z+z^(-1)=(z+1)^2/z,
    phi(X(z))=z^(-2)(z^4+z^3+z^2+z+1),
    chi(X(z))=z^5+z^(-5)=(z^5+1)^2/z^5          (LS4)

show that phi(X(z)) has a simple zero at each xi^j, while X(z) has order2 at z=1 and chi(X(z)) has order2 at every fifth root.
The four nonidentity traces x_j are nonzero roots of phi and lie in F_4.

Choose an integer a with 2^a>=4m and put beta=X^(2^a) in F_2[X]/phi^(4m).
Then beta^2+beta+1=phi^(2^a)=0, and the three cube-one units are exactly1,beta,beta^2.
Indeed, after dividing by the matching residue-field constant, a principal unit1+h with h in(phi) satisfies

    (1+h)^3-1=h(1+h+h^2),

whose order is the order of h unless h=0 in the quotient.
Thus (LS1) gives

    f A(chi)=gamma modulo phi^(4m),
    gamma in{1,beta,beta^2}.                    (LS5)

Because A(0)=1, there is h(t) in F_2[t], of degree below2m, such that A(t)h(t)=1 modulo t^(2m).
Every substitution chi^(2m) has order4m at the four nonidentity fifth roots.
Consequently (LS5) supplies the following local expansions for F(z)=f(X(z)):

    F(z)=gamma_j h(chi(X(z)))
                              modulo (z-xi^j)^(4m), j=1,2,3,4.

For gamma=1, each gamma_j=1.
For either nontrivial gamma there is ONE sigma in{1,2}, valid for all four j, such that

    gamma_j=x_j^sigma=xi^(sigma*j)+xi^(-sigma*j).  (LS6)

This follows directly from the Frobenius powers beta and beta^2 on F_4.
Their polynomial representatives differ from the constants gamma_j only at order at least4m, so no truncated root precision is enlarged here.

### The constant1 case is impossible for every m

Suppose gamma=1.
Set D(z)=F(xi z)+F(z).
The function chi(X(z)) is unchanged by z going to xi z.
At each of the three points z=xi,xi^2,xi^3, both arguments correspond to nonidentity fifth roots, so the preceding local expansions give a zero of D of order at least4m.
The Laurent polynomial D has exponents only between -N and N.
Multiplication by z^N therefore gives a polynomial of degree at most2N<10m, with three distinct nonzero roots of total multiplicity at least12m.
It must vanish identically.
Hence F(xi)=F(1).
But X^m divides f, so F(1)=f(0)=0, whereas (LS5) and A(0)=1 give F(xi)=1.
This contradiction excludes gamma=1 without any restriction on m beyond m>=1.

### Exact fifth-root projection of the complete Laurent polynomial

Now use a nontrivial gamma and its sigma from (LS6).
For each residue s modulo5 define the Laurent polynomial

    F_s(z)=sum_(j=0)^4 xi^(-s*j) F(xi^j z).     (LS7)

Since5=1 in characteristic2, root-of-unity orthogonality gives exactly

    F_s(z)=sum_(n congruent s mod5) [z^n]F(z) z^n.

This follows by summing xi^((n-s)j): the sum is1 if n=s modulo5 and0 otherwise.
No positivity, analytic Fourier theorem or limiting argument is used.

Consider expansions at z=1.
For j=1,...,4, (LS6) gives F(xi^jz)=gamma_j h(chi(X(z))) modulo (z-1)^(4m).
For j=0, the divisibility X^m dividing f and (LS4) give F(z)=0 modulo (z-1)^(2m).
Set gamma_0=0, which equals xi^0+xi^0.
Thus every term in (LS7) has the uniform comparison

    F(xi^jz)=gamma_j h(chi(X(z)))
                                    modulo (z-1)^(2m).

For s other than sigma and -sigma, the weighted sum of the five gamma_j is0.
Therefore F_s has a zero of order at least2m at1.
The exact identity F_s(xi z)=xi^s F_s(z) then gives the same order at ALL five fifth roots.
But z^N F_s is a polynomial of degree at most2N<10m.
Five distinct roots of total multiplicity at least10m force F_s=0.
This proves that F has only the two residue classes sigma,-sigma, including negative exponents and every original coefficient.

### Local inversion forces the stronger endpoint order

Write F=F_sigma+F_(-sigma).
The symmetry F(z)=F(z^(-1)) and uniqueness of residue-class components imply

    F_(-sigma)(z)=F_sigma(z^(-1)).

The map z going to xi^2/z fixes z=xi and preserves chi(X(z)) exactly.
Both local expansions at xi use the SAME constant gamma_1.
It follows that F(z)+F(xi^2/z) has a zero of order at least4m at xi.

Put z=xi t and write A_sigma(t)=F_sigma(t).
The two exact residue classes and inversion symmetry give

    F(xi t)=xi^sigma A_sigma(t)+xi^(-sigma)A_sigma(t^(-1)),
    F(xi/t)=xi^sigma A_sigma(t^(-1))+xi^(-sigma)A_sigma(t).

Adding yields

    F(xi t)+F(xi/t)
       =(xi^sigma+xi^(-sigma))F(t).

The scalar is nonzero because xi is primitive of odd order5.
Hence F(t) has a zero of order at least4m at t=1.
By X(t)=(t+1)^2/t and the nonzero polynomial f, its exact order there is2ord_Xf.
This proves ord_Xf>=2m and completes the uniform assertion (LS2).

### Polynomial trace bases and the exhaustive m=5 reduction

For n>=1 define C_n by

    C_n(z+z^(-1))=z^n+z^(-n).

These are monic polynomials of degree n; together with1 they form a triangular basis of F_2[X].
The substitution is injective because the highest positive Laurent exponent of a nonzero polynomial equals its degree.
Direct multiplication of Laurent expressions gives

    C_a C_b=C_(a+b)+C_|a-b|, C_0=0,
    C_(ab)=C_a(C_b),
    C_(2n)=C_n^2.                              (LS8)

For odd n let B_n be the complete nonidentity trace polynomial with the [C608 normalization](Yin_C_G0608_v1.md#argument).
Its explicit Laurent identity

    B_n(z+z^(-1))=z^(-(n-1)/2)(z^n+1)/(z+1)

gives, after squaring and multiplication by X=(z+1)^2/z,

    C_n=X B_n^2.
    B_1=1, B_3=X+1,
    B_(n+2)=X B_n+B_(n-2).                     (LS9)

These exact identities also show that C_n has only odd powers for odd n, and only even powers for even n.

Assume m=5 and ord_Xf is odd.
By (LS2), ord_Xf>=11, while deg f<25.
The complete two-class support therefore expresses f uniquely as a sum of C_n with1<=n<=24 and n congruent to sigma or -sigma modulo5.
This range is forced by the strict degree hypothesis, not an arbitrary cutoff.
Its odd-power part f_odd is nonzero, and its even-power part can be written E^2.
The coefficients of these decompositions are in F_2.

For sigma=1, the odd indices are1,9,11,19,21.
For sigma=2, they are3,7,13,17,23.
By (LS9), f_odd=X W^2, where W is the corresponding linear combination of these five B_n.
The lower order11 implies X^5 divides W.
The two COMPLETE coefficient tables modulo X^5 are

| sigma | n | B_n modulo X^5 |
| --- | --- | --- |
| 1 | 1 | 1 |
| 1 | 9 | 1+X^2+X^3+X^4 |
| 1 | 11 | 1+X+X^2+X^4 |
| 1 | 19 | 1+X+X^4 |
| 1 | 21 | 1+X+X^2+X^4 |
| 2 | 3 | 1+X |
| 2 | 7 | 1+X^2+X^3 |
| 2 | 13 | 1+X+X^4 |
| 2 | 17 | 1+X^4 |
| 2 | 23 | 1+X^2+X^3+X^4 |

Every entry follows from the displayed recurrence starting at B_1,B_3, reducing modulo X^5 at each addition and multiplication.
For clarity the intermediate entries are B_5=1+X+X^2, B_15=B_17=1+X^4; these also verify the later rows directly.

In the sigma=1 block, the X^3 coefficient first forces the n=9 coefficient to vanish.
The X^2 coefficient equates the n=11 and21 coefficients; the X coefficient then kills n=19, and the constant coefficient kills n=1.
Its only nonzero kernel vector therefore uses n=11,21.
In the sigma=2 block, the X and X^2 coefficients respectively equate the n=3,13 and n=7,23 coefficients.
The constant coefficient then kills n=17, and the X^4 coefficient equates the two pairs.
Its only nonzero kernel vector uses n=3,7,13,23.
Thus all possible nonzero odd parts have been exhausted, with no high auxiliary coefficient omitted.

### Both exact odd parts fail the phi-unit requirement

For sigma=1, identities (LS8) give

    f_odd=C_11+C_21=C_16 C_5=X^16chi.

Its exact X-order is17.
Since the total f has odd X-order, the even part must have order at least18, so ord_XE>=9.
The complete even-index list is4,6,14,16,24, and hence

    E is in span_(F_2){C_2,C_3,C_7,C_8,C_12}.

The exact basis polynomials are

    C_2=X^2, C_3=X^3+X, C_7=X^7+X^5+X,
    C_8=X^8, C_12=X^12+X^4.

Their coefficients at X^2,X^3,X^5,X^8,X^4, in that order, force every coefficient of E to vanish if ord_XE>=9.
Therefore E=0 and f=X^16chi, which is divisible by phi.
This contradicts the phi-unit hypothesis.

For sigma=2, the exact identities give

    f_odd=C_3+C_7+C_13+C_23
         =C_8(C_5+C_15)
         =X^8chi^3,

because C_15=C_3(chi)=chi^3+chi.
Its exact X-order is11, so the even part must have order at least12, and ord_XE>=6.
Here the complete even-index list is2,8,12,18,22, and

    E is in span_(F_2){C_1,C_4,C_6,C_9,C_11}.

Use the exact polynomials

    C_1=X, C_4=X^4, C_6=X^6+X^2,
    C_9=X^9+X^7+X^5+X,
    C_11=X^11+X^9+X^5+X^3+X.

The coefficients of X^3,X^5,X,X^2,X^4 successively kill C_11,C_9,C_1,C_6,C_4 whenever ord_XE>=6.
Again E=0, now f=X^8chi^3, contradicting the phi-unit condition.
Both values of sigma fail, proving the even endpoint-order assertion at m=5 and its equivalent form (LS3).
The argument uses the complete Laurent support and all coefficients; it does not require enumerating48 local representatives.

### The complete original multiplicity-ten gate supplies (LS3)

Retain the SAME original P,T, fields, divided remainders, sign and complete zero-Haar/unique-unsaturated hypotheses in the statement.
The [C199v4 normalized gate](Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate), [complete complement](Yin_C_G0199_v4.md#normalized-low-degree-complement) and [C199v5 original interfaces](Yin_C_G0199_v5.md#statement) give

    U_0=X^10phi^70Y,
    R_0=rem_(U_0)(U_0(chi)^3),
    H_0=X^10Y, C_00=X^10Y(chi)Psi^70,
    V_0=R_0/phi^60=H_0B,
    D_0=V_0+C_00^3,
    deg B<20, phi prime to B.

Here Y is monic prime to Xphi, and B is the unique COMPLETE monic complement, including every saturated surplus and every extra remainder factor.
The [C197v3 normalized T-support derivative](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) gives X^20 dividing W_U'.
Writing Y=J^2W_U with J(0)=1 gives X^20 dividing Y'.
The [C609v2 actual complete-factor parity](Yin_C_G0609_v2.md#statement) gives even ord_XB.
This is the actual V_0 complete factorization interface; no completeness or global square property of Y alone is assumed.

Keep all original nonnegative a_b and the unchanged indices

    lambda_0=lambda_1=1,
    lambda_b=2^(b-1) for b>=2,
    sum_b a_b lambda_b=60q.

The exact correction window20q<lambda_b<60q contains only32q, at b=k+6.
Therefore

    S_star=epsilon X^16(X+1)^32phi^28,
    epsilon=a_(k+6) mod2.                      (LS10)

All lower layers remain present, and no a_b is divided by q.
Both choices of epsilon are retained.
The unit root Z_0 is defined modulo phi^30 by Z_0^11=H_0C_00^2.
The inherited D_0 in phi^10 makes the complete equation

    Z_0D_0+H_0V_0S_star=0 modulo phi^40

independent of the polynomial lift of Z_0.
By (LS10) this equation forces D_0 in phi^28, and hence H_0B=C_00^3 modulo phi^20.
The exact old relation is H_0^6=C_00^21 modulo phi^40.

Write the complete low-X data as

    Y=sum_(i=0)^9 u_i X^(2i) modulo X^20, u_0=1,
    L(t)=sum_(i=0)^9 u_i t^i,
    Q=X^5Psi^35 L(chi).

All u_i are retained.
The derivative condition excludes the odd coefficients below20, and substitution gives C_00=Q^2 modulo phi^40.
Taking sixth powers of H_0B=C_00^3 modulo phi^20 doubles the error order to at least40.
Use the old relation and divide by the unit C_00^18 to obtain B^6C_00^3=1 modulo phi^40.
After substituting Q^2 and taking exact square-root valuations, this yields

    (BQ)^3=1 modulo phi^20.

Apply (LS3) with the auxiliary polynomial

    A(t)=(1+t+t^2)^35 L(t), A(0)=1.

The actual B has all its required degree, parity and unit properties, so (LS3) is a contradiction.
This excludes the ENTIRE original A_0=10 branch, including all high bits, all complete support and every original q.

### Exact costs, normalization and the remaining scope

The original maximal q and the nonsquare canonical root R_0 are retained from C199.
Neither is inferred from a finite local jet.
The proof uses necessary consequences of the same complete canonical C3/C5 and field residual system, and constructs no free residual, replacement field or monic T.

The full conditional degree identities before contradiction are

    deg U_0=150+deg Y,
    deg R_0=130+deg Y+deg B,
    r=q(150+deg Y),
    w=q(130+deg Y+deg B),
    r-w=q(20-deg B)>0.

The zero-Haar integer cyclotomic factorization has leading coefficient1 or-1, so reduction preserves deg G here.
Every extra factor and saturated surplus stays in the complete degree of B; no endpoint equality or fixed monomial B is assumed.

The Laurent constraint (LS2) holds for every positive m and arbitrary auxiliary degree, so it supplies a structural reduction beyond the single tested multiplicity.
The even endpoint conclusion was proved only at m=5 by its two complete trace spaces.
No assertion that the same two kernels or the same parity conclusion hold for every odd m is made.
The exact A_0=10 layer projection is also not an automatic projection theorem for all remaining even A_0.
The [adopted C630 original exclusion and remaining range](Yin_C_G0630_v1.md#statement) leave even A_0>=10 on this domain; the present result removes10 and leaves even A_0>=12.
That final range statement uses the adopted earlier branch exclusions, while the new Laurent proof does not use their finite support certificates.
No A_0=12 test or larger-support scan is part of this fixed step.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-23)

## Assessment history

### Decision initial

| Field | Value |
| --- | --- |
| date | 2026-10-23T20:05 |
| status | open |
| reason | Register the parameter-uniform Laurent support and endpoint theorem, the complete m=5 odd-order impossibility, and the entire original A_0=10 exclusion. Exact local constants, five-root projections, all multiplicity/degree counts, both trace spaces, original integer layers and canonical costs are retained. The new proof awaits fresh isolated whole review; no universal odd-m exclusion or Task completion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Uniform and original theorem](#statement) | Every m>=1 and unrestricted auxiliary polynomial degree under (LS1), exact m=5 parity/no-solution consequence, complete original A_0=10 exclusion and remaining even A_0>=12 range. |
| argument | [Whole LS1--LS10 proof](#argument) | All local root lifts, exact finite-field projections, three-point and five-point degree contradictions, local inversion and endpoint order, both complete trace-space kernels and original gate application. |
| dependency | [Whole-trace Laurent normalization](Yin_C_G0608_v1.md#argument) | Exact B_n definition, Laurent identity and recurrence used for the displayed ten polynomial rows; no prior finite group certificate or cutoff is invoked. |
| dependency | [Original complete normalized domain](Yin_C_G0199_v5.md#statement) | Actual P/T/field/residual/Haar/unique-unsaturated hypotheses, canonical maximal q and nonsquare root, complete integer layers, normalized gate and old relation. |
| dependency | [Normalized gate proof](Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate) | UR13--UR20 original normalization and exact S_star, root30/error40 precision and original32q layer at A_0=10. |
| dependency | [Complete complement and degree cost](Yin_C_G0199_v4.md#normalized-low-degree-complement) | Unique complete B, all extra factors and saturated surplus, phi-unit property and strict degree below20. |
| dependency | [T-support derivative](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) | Exact normalized X^20 derivative divisibility for W_U and then Y; no identification with the G-unit odd part. |
| dependency | [Actual complete-factor endpoint parity](Yin_C_G0609_v2.md#statement) | Even ord_XB on the full original domain, through actual complete V_0 and its derivative gate. |
| dependency | [Earlier original exclusion and remaining range](Yin_C_G0630_v1.md#statement) | Only the final remaining even A_0>=12 consequence after removing10; not a premise of the uniform Laurent theorem or m=5 contradiction. |

### Decision whole-reviewed-2026-10-23

| Field | Value |
| --- | --- |
| date | 2026-10-23T20:16 |
| status | proved |
| reason | Adopt the entire fixed theorem after main reading of complete C634 and isolated whole R840. The uniform Laurent projection/local inversion proof holds for every m>=1; both exhaustive m5 trace spaces prove the exact odd-order impossibility. The complete original A0=10 gate, all layers/high bits and canonical costs satisfy that contradiction for every actual q. Only the same zero-Haar unique-unsaturated domain now leaves even A0>=12; no universal odd-m exclusion or unrestricted Task conclusion is asserted. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Uniform and original theorem](#statement) | Every m>=1 and unrestricted auxiliary polynomial degree under (LS1), exact m=5 parity/no-solution consequence, complete original A_0=10 exclusion and remaining even A_0>=12 range. |
| argument | [Whole LS1--LS10 proof](#argument) | All local root lifts, exact finite-field projections, three-point and five-point degree contradictions, local inversion and endpoint order, both complete trace-space kernels and original gate application. |
| dependency | [Whole-trace Laurent normalization](Yin_C_G0608_v1.md#argument) | Exact B_n definition, Laurent identity and recurrence used for the displayed ten polynomial rows; no prior finite group certificate or cutoff is invoked. |
| dependency | [Original complete normalized domain](Yin_C_G0199_v5.md#statement) | Actual P/T/field/residual/Haar/unique-unsaturated hypotheses, canonical maximal q and nonsquare root, complete integer layers, normalized gate and old relation. |
| dependency | [Normalized gate proof](Yin_C_G0199_v4.md#normalized-common-frobenius-unit-gate) | UR13--UR20 original normalization and exact S_star, root30/error40 precision and original32q layer at A_0=10. |
| dependency | [Complete complement and degree cost](Yin_C_G0199_v4.md#normalized-low-degree-complement) | Unique complete B, all extra factors and saturated surplus, phi-unit property and strict degree below20. |
| dependency | [T-support derivative](Yin_C_G0197_v3.md#quadratic-primary-odd-part-derivative) | Exact normalized X^20 derivative divisibility for W_U and then Y; no identification with the G-unit odd part. |
| dependency | [Actual complete-factor endpoint parity](Yin_C_G0609_v2.md#statement) | Even ord_XB on the full original domain, through actual complete V_0 and its derivative gate. |
| dependency | [Earlier original exclusion and remaining range](Yin_C_G0630_v1.md#statement) | Only the final remaining even A_0>=12 consequence after removing10; not a premise of the uniform Laurent theorem or m=5 contradiction. |
| review | [Independent whole Laurent and A10 finding](../audits/reviews/Yin_R_G0840_v1.md#whole-laurent-a10-finding) | Entire LS1--LS10, arbitrary auxiliary degree, all local precision and negative Laurent exponents, both exhaustive m5 spaces, full original root30/error40 and complement/parity/cost interfaces; earlier review, source and native scopes retained. |

