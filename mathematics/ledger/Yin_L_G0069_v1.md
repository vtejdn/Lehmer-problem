---
author: Yin
---

# G0001: transfer of the published auxiliary constant to integral scalar congruences

Date: 2026-10-07.

The complete current initial transfer and added arbitrary-prime proof are retained in [C246](../claims/Yin_C_G0246_v1.md#gim%2B10-integral-congruence-transfer), with [current full self-review](../audits/reviews/Yin_R_G0522_v1.md#current-published-transfer-finding).
This dated mathematical input and the separately staged original [R21 findings](../audits/reviews/Yin_R_G0021_v1.md#boundary-and-actual-review) remain at their original scopes.

Bounded proof-interface argument by assigned AI ms25_source for Yin.
This is separate from the source audit [GIM+10-U001](../audits/literature/GIM+10/Yin_U001.md#gim%2B10-u001).
The coordinator requested an explicit check that the published constant survives the general integral scalar-congruence domain, including reduction polynomials divisible by t-1.
No new numerical computation, source search, or degree-preservation assumption is used.

<a id="gim+10-integral-congruence-transfer"></a>
## Transfer domain, without an odd-completion degree loss

Let alpha be a nonzero nontorsion algebraic integer of degree d, let a>=1 be an integer, and assume `(alpha^a-1)/2` is integral.
Put beta=alpha^a.
Use natural logarithms and the absolute logarithmic Weil height; in particular h(alpha)=log M(P_alpha)/d and h(beta)=a h(alpha).
The claim obtained from the inspected source calculation is

    h(beta)>=0.427800,
    log M(P_alpha)>=0.427800 d/a.                     (1)

This does not require P_alpha mod2 to avoid t-1, nor preservation of degree under any power.
We do not deduce it by constructing an odd-coefficient multiple: such a construction can need a larger degree.
Instead we check the exact proof interface.

The source auxiliary is

    g(z)=(z-1)^k(z+1)^l(5z^2+6z+5)^t
         (29z^4+60z^3+78z^2+60z+29)^w
         (3z^2+2z+3)^c
         (33z^4+60z^3+70z^2+60z+33)^e
         (169z^6+490z^5+871z^4+1036z^3+871z^2+490z+169)^s,

    (k,l,t,w,c,e,s)=(3977,780,328,96,24,16,16).

Write D=deg g=k+l+2t+4w+2c+4e+6s=6005 and A=2k+l+4t+8w+3c+8e+12s=11206.
Since beta-1 is divisible by2, u=beta^2-1 is divisible by4.
The seven factors of g(beta^2) are divisible by `4,2,16,256,8,256,4096`, respectively.
For the quartics, use

    a u^4 + 16 b beta^2 u^2 + 256 beta^4,
    (a,b)=(29,11) or (33,12).

For the sextic, use

    169u^6+16*94 beta^2 u^4+256*17 beta^4 u^2+4096 beta^6.

The quadratic identities are `5u^2+16 beta^2` and `3u^2+8 beta^2`.
These are literal polynomial identities, so `g(beta^2)/2^A` is integral.
No probabilistic independence or coprimality between factors is needed.

<a id="gim+10-auxiliary-nonvanishing"></a>
## Direct nonvanishing check for integral inputs

Each auxiliary factor has all its roots on the unit circle.
For the two quadratics this follows from reciprocal trace values -6/5 and -2/3.
The quartic trace polynomials are

    29x^2+60x+20,          33x^2+60x+4,

whose two roots are in (-2,2).
The sextic trace polynomial is

    169x^3+490x^2+364x+56.

At x=-2,-1,-1/2,0 its values are respectively `-64,13,-197/8,56`, so all three roots lie in (-2,0).
The standard reciprocal substitution z+z^(-1)=x now proves the unit-circle claim.
If g(beta^2)=0, the minimal polynomial of the algebraic integer beta^2 divides g, so all its conjugates have modulus1.
Kronecker makes beta, and then alpha, torsion, a contradiction.
This replaces the source's degree-based irreducibility/nonvanishing argument only for our integral domain.
It does not upgrade its claim for arbitrary algebraic numbers.

<a id="gim+10-external-constant"></a>
## The retained external calculation

On the unit circle, `||g||^2=2^D L`, where

    L=max_{-1<=x<=1} (1-x)^k(1+x)^l(5x+3)^(2t)
      (29x^2+30x+5)^(2w)(3x+1)^(2c)
      (33x^2+30x+1)^(2e)(169x^3+245x^2+91x+7)^(2s).

The nonzero norm argument, or the product formula, gives

    h(beta)>=[(2A-D)log2-log L]/(4D).                  (2)

This is precisely source equation(3.5), with `2A-D=16407`.
The source reports a numerical supremum computation producing `0.4278003111...` and states the safely rounded theorem value `0.427800`.
Adoption of that latter rational number in(1) relies on the published evaluation as an external input.
No exact interval certificate, original computation code, fresh supremum calculation or independent audit of that numerical margin has been obtained in this bounded inspection.
The exact expression(2) remains available independently of that numerical acceptance.
Since h(alpha^a)=a h(alpha), (1) then follows with the original degree d.

<a id="gim+10-arbitrary-prime-scalar-transfer"></a>
## The same published constant covers scalar congruences at every prime

Return to the primary algebraic-unit domain.
Let alpha be a nontorsion algebraic unit of degree d, let beta=alpha^a, and suppose that, for some rational prime p and a nonzero scalar residue c,

    (beta-c)/p is integral.                          (3)

The integer representative chosen for c does not affect this condition.
It may be divisibility in Z[alpha], or merely integrality of this quotient in the number field.
Put c_0=0.427800=2139/5000.
Then the transferred statement is

    h(beta)>=c_0,
    m(P_alpha)>=(d/a)c_0.                            (4)

For p=2 the only nonzero residue is 1, so (4) is exactly (1).
The other primes are covered by elementary norm estimates strictly stronger than c_0, without adopting any further numerical source calculation.

For p=3 choose epsilon in {1,-1} representing c and set

    F_epsilon(t)=(t-epsilon)^9(t+epsilon),
    deg F_epsilon=10.

The value is nonzero because beta is not a root of unity, and F_epsilon(beta)/3^9 is integral.
Taking the norm over Q(alpha), with all d embeddings retained, gives the lower bound 3^(9d).
The exact unit-circle supremum, the same for both signs, is

    C(F_epsilon)=2^10 3^9/10^5.

Indeed for epsilon=1 and t=exp(2iu), the squared modulus is 2^20 x^9(1-x), where x=sin^2 u.
Its maximum occurs at x=9/10.
The change t -> -t proves the other sign.
Applying the circle bound inside and outside the unit disk, then multiplying over the embeddings, yields

    3^(9d)<=C(F_epsilon)^d M(P_alpha)^(10a),
    h(beta)>=log(sqrt(10)/2).                        (5)

This constant exceeds c_0 by an exact rational comparison.
The identity (log x)/2=integral_0^((x-1)/(x+1)) dt/(1-t^2) for x>1 gives

    log(sqrt(10)/2)=log(5/2)/2
       >3/7>2139/5000.

For p>=5 choose a balanced representative with 1<=|c|<=(p-1)/2.
The value beta-c is nonzero: if a rational integer were equal to the unit beta it would be 1 or -1, contrary to nontorsion.
Its nonzero norm is therefore at least p^d, whereas

    |Norm(beta-c)|<=(1+|c|)^d M(P_alpha)^a.

Consequently

    h(beta)>=log[p/(1+|c|)]
       >=log[2p/(p+1)]>=log(5/3)>1/2>c_0.           (6)

The strict inequality log(5/3)>1/2 follows from the same integral formula, now with (x-1)/(x+1)=1/4.
Equations (1), (5) and (6) prove (4) for every prime.
In particular, if a<=Cd for a fixed C>0, the scalar-congruence class has the uniform bound

    m(P_alpha)>=0.427800/C.                          (7)

No bounded-prime hypothesis or power-degree guard is used.
The separate [scalar-congruence norm proof](Yin_L_G0067_v1.md#scalar-collapse-root-matrix-interface) shows how squarefree full reduced-root collision implies the stronger order congruence beta-c in p Z[alpha], equivalent to its displayed companion-matrix and polynomial-divisibility conditions.
That stronger condition implies (3); no equivalence with mere maximal-order integrality is asserted here.
This paragraph proves a restricted-class bound, not coverage of the small-Mahler core by exponents a<=Cd.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0021_v1.md#boundary-and-actual-review), with its original inspected scope and relationship.
