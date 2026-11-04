---
author: Yin
---

# Exact dyadic residual precision in odd-coefficient Salem families and irreducible fixed-measure towers

Human author Yin.
Provenance: project deduction under the unchanged [G0001 original contract](../tasks/Yin_T_G0001_v1.md#contract).
Root proposed the varying odd coefficient, generalr valuation table, exact baseline quotient formulas and the fixed-degree2-adic-limit control.
The characteristic_zero_bridge agent verified every actual division, developed the Laurent geometric-sum proof of those quotients, checked all valuation endpoints and supplied the full Salem/irreducibility adaptation.
Root has read the entire integrated LC1--LC23 candidate; both agents are contributors and neither supplies an independent review of this new result.
This fixed candidate awaits fresh isolated whole review; no native computation, coefficient scan or new source acquisition is used.

The direct fixed inputs are [C726's full squarefree binary trace-root calculation](Yin_C_G0726_v1.md#decision-whole-reviewed-2026-10-25) and [C697's actual divided-remainder interface](Yin_C_G0697_v1.md#decision-whole-reviewed-2026-10-25).
The positive-coefficient root proof explicitly adapts the node and torsion-norm method of [C136 Section1](Yin_C_G0136_v1.md#argument); its older q=5^r, coefficient3 theorem is not said to cover the present enlarged family.
The classical inputs actually reused are accepted [Con26d-U001v2 Theorem2.1](../audits/literature/Con26d/Yin_U001.md#con26d-u001), the monic rational-factor integer-coefficient property at its selected-pages scope, and [Smy08-U001's Kronecker characterization](../audits/literature/Smy08/Yin_U001.md#smy08-u001), with its full product/multiplicity convention on printed p322.
Those actual source statements and inspection limits were read; no new full-source proof audit is claimed.

<a id="coefficient-five-actual-eight-family"></a>
<a id="general-odd-coefficient-residual-precision"></a>
## Statement

### Exact algebraic domain and valuation statement

Let D>=2, r>=1 be integers, let u be ANY odd integer of either sign, and set

    mu=1+2^r u, W=C_(D-1), L=2D-1,
    T_mu=C_D-mu W,
    P_mu(z)=z^D T_mu(z+z^(-1))
           =z^(2D)-mu z^(2D-1)-mu z+1.            (LC1)

Use C_0=2,C_1=X,C_(j+1)=X C_j-C_(j-1).
The integer coefficient mu is distinct from the total logarithmic Mahler measure m(P_mu).
Use the SAME actual canonical integer polynomials

    a=rem_(T_mu)(T_mu(C_2))/2,
    b=rem_(T_mu)(T_mu(C_3))/3,
    c=rem_(T_mu)(T_mu(C_5))/5,
    F=rem_(T_mu)(2c^2-3a^5),
    X_s=rem_(T_mu)(b^2-a^3+s(c^3-2b^5)),
    G=rem_(T_mu)(c^3-2b^5), s in{1,-1}.

Write ord_2 for exact coefficient2-adic order, with ord_2(0)=infinity.
For every odd mu the binary U=T_mubar=C_Dbar+Wbar is the SAME squarefree degree-D polynomial from C726, with complete roots {zeta+zeta^(-1):zeta^L=1} over the algebraic closure of F_2, including0 once.
Put J=rem_U(Wbar X).
Then

    Wbar^2=X modulo U, J^2=X^3 modulo U,
    J!=0, rem_U(X^3)!=0, rem_U(X^5)!=0.           (LC2)

The exact dyadic quotient is

    a=rem_(T_mu)[mu(mu-1)W^2/2+(mu-1)]
      =2^(r-1)u rem_(T_mu)(mu W^2+2),
    ord_2(a)=r-1, (a/2^(r-1))bar=X.              (LC3)

For EVERY r>=2 the odd quotients additionally satisfy

    ord_2(b)=ord_2(c)=r+1,
    (b/2^(r+1))bar=(c/2^(r+1))bar=J.             (LC4)

For each separately fixed sign, the complete residual orders are as follows.

| r | ord_2(F) | ord_2(X_s) | ord_2(G) | Exact simultaneous precision min(ord_2(F),ord_2(X_s)) |
| --- | --- | --- | --- | --- |
| 1 | 0 | 0 | No exact order asserted | 0 |
| 2 | 5 | 3 | 9 | 3 |
| 3 | 9 | 6 | 12 | 6 |
| 4 | 11 | 9 | 15 | 9 |
| 5 | 13 | At least13, possibly infinity | 18 | 13 |
| r>=6 | 2r+3 | 2r+2 | 3r+3 | 2r+2 |

These are ACTUAL canonical coefficient orders, not freely chosen field coordinates.
The r=5 lower bound for X_s is deliberately not asserted exact; the exact first order13 already fixes the joint precision.
No irreducibility, total reality, root location or measure premise is required for LC2--LC4 or this table.
All displayed normalized divisions occur in the integer coefficient module before binary reduction.

### Actual positive-coefficient family and its full cost

For EVERY integer mu>2 and EVERY D>=2, P_mu is a monic irreducible reciprocal integer-unit polynomial of constant1 and FULL degree2D.
It is the minimal polynomial of a genuine Salem number beta, with one exterior root beta>1, its positive reciprocal and2D-2 distinct nonreal unit-circle roots.
Its actual degree-D trace minimal polynomial is T_mu, with D-1 simple roots in(-2,2) and one simple root tau>2.
Moreover

    H(P_mu)=mu, S(P_mu)=2mu+2,
    mu<beta<mu+1,
    m(P_mu)=log beta,
    beta->mu and m(P_mu)->log mu
                          as D->infinity at fixed mu. (LC5)

Here H is maximum absolute coefficient, S is the TRUE circle supremum, and m counts every original root with multiplicity.
In particular mu=5, r=2, u=1 gives an ACTUAL irreducible Salem family at every full even degree2D>=4 with H=5, S=12, log5<m<log6 and exact F/X_s/G orders5/3/9.
It solves both residuals modulo8 and the first modulo32, but fails the second modulo16.
The higher-r table gives arbitrary finite joint precision only with its explicitly increasing coefficient, circle and measure costs in the fixed-degree sequence below.
G is a nonzero actual canonical polynomial for every r>=2 by its finite exact order, but Gbar=0; no C691 nonzero binary canonical G or synthetic Haar realization is supplied.

<a id="fixed-degree-two-adic-cyclotomic-limit"></a>
### Fixed degree and unbounded precision have an explicit cyclotomic2-adic limit

Fix ANY D>=2 and take the actual sequence mu_r=1+2^r, r>=2, so u=1 and every P_(mu_r) is genuine Salem of the SAME full degree2D.
Its exact simultaneous precision is the table above, tending to infinity.
Nevertheless

    H(P_(mu_r))=1+2^r,
    S(P_(mu_r))=2^(r+1)+4,
    m(P_(mu_r))>log(1+2^r)>r log2 ->infinity.      (LC16)

The actual coefficients are2-adically compatible:

    T_(mu_(r+1))-T_(mu_r)=-2^r W,
    P_(mu_(r+1))-P_(mu_r)
                    =-2^r(z^(2D-1)+z).           (LC17)

They converge coefficientwise in Z_2 to A=C_D-W and P_1=(z-1)(z^L-1), respectively.
The latter is a reducible product of cyclotomic polynomials, including a double root1, and has logarithmic Mahler measure0.
Every map C_p, p=2,3,5, preserves the entire characteristic-zero trace-root set of A, so each of its actual canonical a,b,c is exactly zero; consequently F,X_s and G are exactly zero as well.
This is a direct fixed-degree example in which irreducibility, nontorsion and an archimedean cost bound do NOT persist under coefficientwise2-adic limiting.
It is not a near-one family: the finite actual total measures diverge, and convergence is asserted only in the2-adic coefficient topology.
The exact nonzero finite G order3r+3 tends to infinity and is compatible with G=0 at the limit.

All finite members have Gbar=0 and therefore leave C691's distinct nonzero binary canonical source unresolved.
No synthetic-to-canonical Haar identification, controlled small-measure realization or unrestricted G0001 conclusion follows.
Pure dyadic composition preserves the stated exact residual orders by C724; the following extension proves irreducibility under its explicit additional nonsquare-norm hypothesis.

<a id="nonsquare-norm-irreducible-bounded-circle-towers"></a>
### An explicit nonsquare norm gives irreducible towers with the same finite precision

Root proposed this extension of the [accepted C711 SL8 nonsquare and positive-root mechanism](Yin_C_G0711_v1.md#complete-argument).
The characteristic_zero_bridge agent directly read that complete mechanism and its adopted scope, checked the converse square criterion, and adapted every field-degree, root-count, norm and coefficient-order step here.
This is part of the author candidate, not an independent review of C711 or of LC1--LC17.
No assumption that the present construction satisfies C711's prescribed coefficient CRT is used; only its proved mechanism is reused, and irreducibility of this new family is proved explicitly below.

For this extension let D>=2 and mu>2 be integers and impose the additional hypothesis

    2(mu+1) is not a square in Z.                  (LC18)

Let beta be the positive Salem root of P_mu in LC5, tau=beta+beta^(-1), K=Q(beta), and F=Q(tau).
For every j>=0 put k=2^j and define

    theta_j=beta^(1/k)>0, eta_j=theta_j+theta_j^(-1),
    P_(mu,j)(z)=P_mu(z^k), T_(mu,j)=T_mu(C_k),
    K_j=Q(theta_j), F_j=Q(eta_j).

Then P_(mu,j) is the actual monic irreducible reciprocal integer-unit minimal polynomial of theta_j, of FULL degree2Dk, and T_(mu,j) is the actual irreducible trace polynomial of degree Dk.
The exact field degrees are

    [K_j:K]=k, [F_j:F]=k, [K_j:F_j]=2,
    [K_j:Q]=2Dk, [F_j:Q]=Dk.                     (LC19)

Every root is retained: P_(mu,j) has exactly k exterior roots of modulus beta^(1/k), k interior roots of modulus beta^(-1/k), and (2D-2)k unit-circle roots, all simple.
Consequently

    H(P_(mu,j))=mu, S(P_(mu,j))=2mu+2,
    m(P_(mu,j))=log beta,
    house(P_(mu,j))=beta^(1/k).                   (LC20)

For j>=1 this original polynomial is not Salem, since k>=2 exterior roots occur.
No total-reality premise is imposed on the higher trace fields.
Every canonical polynomial h in{a,b,c,F,X_s,G} satisfies the exact integer identity h(T_(mu,j))=h(T_mu)(C_k), so its coefficient2-adic order and its zero/nonzero status are unchanged.
Here h(T) denotes the canonical polynomial computed with divisor T, not substitution of T into a separately fixed polynomial h.
The trace derivative obeys

    ord_2(T_(mu,j)')=j+ord_2(T_mu').              (LC21)

If mu is odd, ord_2(T_mu')=0 and the order in LC21 is exactly j.
Thus the entire preceding valuation table persists for every odd mu satisfying LC18, without acquiring any extra residual bit along the tower.

For ANY nonzero g in F, viewed inside F_j and K_j through tau=C_k(eta_j), the actual norms retain every original multiplicity:

    Norm_(F_j/Q)(g)=Norm_(F/Q)(g)^k,
    Norm_(K_j/Q)(g)=Norm_(F/Q)(g)^(2k).           (LC22)

In particular this applies to every nonzero base canonical value g=h(T_mu)(tau), whose tower value is the SAME element by exact covariance.
The absolute logarithmic norm costs are multiplied by k and2k respectively; no degree-normalized or single-root norm is substituted for these full norms.

For mu=5, LC18 is the nonsquare integer12, and EVERY D>=2, j>=0 gives an actual irreducible tower with

    full degree=2D*2^j, trace degree=D*2^j,
    H=5, S=12, log5<m=log beta<log6,
    ord_2(T_(5,j)')=j,
    ord_2(F)=5, ord_2(X_s)=3, ord_2(G)=9.         (LC23)

Both signs are covered and the joint precision is EXACTLY3 at every level.
This supplies genuine irreducible bounded-circle inputs with arbitrarily large derivative order but no corresponding improvement in the residual precision or full measure.
The condition LC18 is only sufficient; when it fails, for example mu=17 with2(mu+1)=36, no assertion about irreducibility of the higher compositions is made here.

## Complete argument

### Complete binary scope and the exact first quotient

C726 gives the full squarefree U and Wbar^2=X on all its roots, including the separately checked zero trace.
At a nonzero root x of U, Wbar(x)^2=x!=0, so Wbar(x)x is nonzero.
Such a root exists for every D>=2 because L>=3 and only zeta=1 has trace0.
This proves J!=0, J^2=X^3 in the quotient, and the nonzero X^3/X^5 remainder assertions of LC2.

The exact identity C_j(C2)=C_j^2-2 gives

    T_mu(C2)=T_mu*(C_D+mu W)
                 +mu(mu-1)W^2+2(mu-1).           (LC6)

Actual monic integer division is linear and commutes with the displayed integer factors.
Since mu(mu-1) is even, division by2 AFTER taking that actual remainder proves LC3.
The normalized reduction is X because u and mu are odd and Wbar^2=X modulo U.
If r=1, abar=X while bbar=cbar=0 from C726's full-root C3/C5 closure and the odd scalar divisions.
Thus Fbar=rem_U X^5 and X_sbar=rem_U X^3, both nonzero, proving the first table row without claiming LC4 there.

### Actual cyclotomic baseline and exact quotient congruences

Put A=C_D-W and P_1=z^D A(z+z^(-1))=(z-1)(z^L-1).
The complete complex root set of A is {zeta+zeta^(-1):zeta^L=1}, including2 from zeta=1.
Inverse pairing at the odd L gives D distinct roots, exhausting the monic degree-D A; the trace root2 is simple even though z=1 is a double root of P_1.
For p in{3,5}, powering preserves this COMPLETE set, including roots mapped to1.
Consequently actual monic integer division gives Q_p in Z[X] with

    A(C_p)=A Q_p.                                 (LC7)

Define the integer geometric sum S_p(z)=1+z+...+z^(p-1).
The Laurent trace identities and the exact factorizations of z^p-1 and z^(pL)-1 give

    z^((p-1)D) Q_p(z+z^(-1))
                       =S_p(z)S_p(z^L).          (LC8)

The cancellation deriving LC8 is in the integral Laurent polynomial domain before evaluating at any root.
There is no division by zeta-1 or zeta^p-1 at a special root.
For EVERY zeta^L=1, including zeta=1, its right second factor is p and (p-1)D=((p-1)/2)(L+1).
Writing x=zeta+zeta^(-1) therefore gives

    Q_p(x)=p[1+sum_(i=1)^((p-1)/2) C_i(x)].

Since A is squarefree, actual integer polynomial congruences follow:

    Q_3=3(X+1) modulo A,
    Q_5=5(X^2+X-1) modulo A.                      (LC9)

They are CONGRUENCES, not claims that the displayed representatives already have canonical degree when D=2.
At x=2 the formula gives Q_p(2)=p^2, and the same identity covers every nonendpoint root whose p-th power is1.
Thus every endpoint and p|L critical branch is included without a derivative quotient singularity.

At EVERY trace root x of A, the relation zeta^L=1 also gives

    W(x)^2=zeta^(2D-2)+2+zeta^(-2D+2)=x+2.

This includes x=2.
Hence W^2=X+2 modulo A as an INTEGER polynomial congruence.
Commuting trace powers yields W(C_p)=C_p(W), so

    W(C3)=W(X-1) modulo A,
    W(C5)=W(X^2-X-1) modulo A.

For the ACTUAL integer polynomials E_p=W Q_p-W(C_p), LC9 gives

    E_3=2W(X+2) modulo A,
    E_5=2W(2X^2+3X-2) modulo A.                   (LC10)

Therefore their actual remainders are even and

    rem_A(E_3)/2=rem_A[W(X+2)],
    rem_A(E_5)/2=rem_A[W(2X^2+3X-2)].

All scalar halves are taken only after the asserted integer divisibility.

### The SAME changing divisor and exact normalized b,c classes

For r>=2, T_mu=A-2^r u W, and the actual baseline Q_p gives

    T_mu(C_p)=T_mu Q_p+2^r u E_p,
    rem_(T_mu)(T_mu(C_p))=2^r u rem_(T_mu)(E_p).  (LC11)

This identity retains the changing-divisor term and does not pretend Q_p is the complete target quotient.
Because T_mu=A modulo4 and both are monic of degree D, integer long division gives

    rem_(T_mu)(E_p)=rem_A(E_p) modulo4.

Indeed each monic long-division step uses only coefficient additions and multiplications, so reduction modulo4 commutes with the complete operation.
LC10 makes both remainders even, and their actual integer halves consequently have the SAME binary reduction

    (rem_(T_mu)(E_p)/2)bar=rem_U(Wbar X)=J.         (LC12)

No division by2 is made inside F_2[X]/U.
For p=3 or5, the defining canonical equation is

    p times the actual p-quotient
                    =2^r u rem_(T_mu)(E_p).

The integer canonical p-quotient exists by the accepted C697 integrality argument.
Since p is odd, LC12 forces it to be divisible by2^(r+1).
After that legitimate coefficient division, reduction of the displayed equation gives the normalized class ubar J=J.
This argument does NOT assert that E_p/p or its half is integral: u is allowed to be divisible by3 or5.
Since J!=0, the resulting coefficient order is EXACTLY r+1, proving LC4 uniformly for every odd u.

### All residual valuations, including the unique tie

For r>=2 write actual integer polynomials

    a=2^(r-1) a_0, b=2^(r+1) b_0,
    c=2^(r+1) c_0,
    a_0bar=X, b_0bar=c_0bar=J.

The integer raw first numerator has its two terms at exponents

    2c^2-3a^5
      =2^(2r+3)c_0^2-3*2^(5r-5)a_0^5.            (LC13)

For r=2 the second term alone has smaller exponent5, with normalized canonical reduction rem_U X^5!=0.
For every r>=3 the first term alone has smaller exponent2r+3, with normalized canonical reduction rem_U J^2=rem_U X^3!=0.
There is no integer r>=2 with 2r+3=5r-5.
Actual monic remainder commutes with these integer factors, so these are the exact F orders in the table.

The four terms of the second numerator have exponents

    b^2:2r+2, -a^3:3r-3,
    s c^3:3r+3, -2s b^5:5r+6.                   (LC14)

For r=2,3,4 the a^3 term alone is smallest and has nonzero normalized reduction rem_U X^3.
For r>=6 the b^2 term alone is smallest and has that SAME nonzero normalized reduction because J^2=X^3 modulo U.
At r=5, both first terms have exponent12 and cancel modulo2 after their actual coefficient division: J^2+X^3=0 in the full quotient.
All other terms have higher exponent, so the actual X_s is divisible by2^13 for BOTH signs.
No stronger exact order is inferred from that first cancellation; X_s=0 is allowed by this particular lower bound.
Since F has exact order13 there, the joint precision is exactly13 regardless of further second-residual cancellation.

Finally the two G terms have exponents3r+3 and5r+6.
The first is strictly smaller for r>=2, and its normalized canonical reduction is rem_U J^3, nonzero at any nonzero trace root because J is nonzero there.
Thus

    ord_2(G)=3r+3, r>=2.                          (LC15)

This proves every table row and every sign, including D=2, using actual coefficient divisions and full monic remainders.
In particular F is always a nonzero canonical polynomial; for r>=2 so is G.

### Explicit extension of the original Salem proof mechanism

Now let mu be ANY integer>2, independently of the congruence restrictions above.
At the D distinct real nodes x_j=2cos(j pi/(D-1)), 0<=j<=D-1, put theta_j=j pi/(D-1).
Then

    T_mu(x_j)=2(-1)^j(cos theta_j-mu).

Every parenthesis is strictly negative, so the signs alternate along those decreasing nodes.
There is one root in each of the D-1 intervening open intervals.
Also T_mu(2)=2-2mu<0 and T_mu is monic, giving a root tau>2.
These D roots exhaust the degree and are all simple; there is no further trace root, including no root at-2 or2.
The exact quadratic trace identity gives one positive reciprocal original pair beta,beta^(-1), beta>1, and2D-2 distinct nonreal unit-circle roots, with every original root counted.

There is NO root of unity in P_mu.
If zeta were one, the integer equation would give mu(zeta^L+zeta)=zeta^(L+1)+1.
Every complex Galois conjugate of the algebraic integer v=zeta^L+zeta has modulus at most2/mu<1, because the conjugate zeta is still a root of the same integer polynomial.
If v were nonzero, its complete nonzero integer norm would have modulus below1, impossible.
Thus zeta^L=-zeta, and substitution gives zeta^2=1.
Since L is odd, this contradicts zeta^L=-zeta in characteristic zero.

The accepted monic rational-factor property permits factorization into monic INTEGER irreducibles, each with constant coefficient+1 or-1 because P_mu has constant1.
The factor containing beta must contain beta^(-1), since otherwise every other available root has modulus1 and its constant coefficient would have absolute value beta>1.
Any remaining factor has all roots on the circle, so the accepted Kronecker characterization makes it cyclotomic, contradicting the just-proved exclusion of all roots of unity.
Therefore P_mu itself is the actual irreducible genuine Salem minimal polynomial of beta, with full degree2D.
A factorization of T_mu would induce one of P_mu through reciprocal trace substitution, so T_mu is the actual trace minimal polynomial of degree D.
This explicitly proves the extension to every D>=2 and integer mu>2; it does not attribute those enlarged quantifiers to the older C136 statement.

The exact values are

    P_mu(mu)=1-mu^2<0,
    P_mu(mu+1)=(mu+1)^L-mu(mu+1)+1>0.

The second expression is positive already at L=3, and L>=3, so mu<beta<mu+1.
The four coefficient positions are distinct and have l1 sum2mu+2, attained on the circle at z=-1.
This gives H(P_mu)=mu and S(P_mu)=2mu+2 exactly.
Only beta is exterior, so m(P_mu)=log beta is the complete logarithmic measure.
The root equation gives

    0<beta-mu=(mu beta-1)/beta^L
          <[mu(mu+1)-1]/mu^L ->0

at fixed mu as D tends to infinity, proving every assertion of LC5.

### Complete nonsquare, field-degree and cost proof of the extension

The already proved base degrees give [K:F]=2, with the nontrivial F-automorphism sigma(beta)=beta^(-1).
There is an exact criterion

    beta is a square in K
      if and only if tau+2 or tau-2 is a square in F.

For necessity, suppose beta=gamma^2 with gamma in K.
Then sigma(gamma)^2=beta^(-1), so sigma(gamma)=gamma^(-1) or -gamma^(-1).
In the first case gamma+gamma^(-1) is fixed by sigma and lies in F, with square tau+2.
In the second case gamma-gamma^(-1) is fixed by sigma and lies in F, with square tau-2.
For sufficiency, if delta in F has delta^2=tau+2, then delta!=0 and ((beta+1)/delta)^2=beta.
If delta^2=tau-2, then delta!=0 and ((beta-1)/delta)^2=beta.
The denominators are nonzero because tau>2, and both constructed square roots lie in K.

Since D>=2, at least one real embedding of the base trace field sends tau into(-2,2).
It sends tau-2 to a negative real number, so tau-2 cannot be a square in F.
The other possibility is excluded by its exact norm:

    Norm_(F/Q)(tau+2)=(-1)^D T_mu(-2)
                    =P_mu(-1)=2(mu+1).

A square in F has a rational-square norm, and a positive nonsquare integer cannot be a rational square.
This proves beta is nonsquare in K using precisely LC18; nonsquareness of the norm is not treated as a necessary condition.

For the positive-root induction, theta_0=beta is nonsquare in K_0=K.
Suppose theta_(j-1) is nonsquare in K_(j-1).
The equation theta_j^2=theta_(j-1) gives an extension of degree2, and K_j=K_(j-1)(theta_j) since theta_(j-1)=theta_j^2.
Its nontrivial automorphism sends theta_j to -theta_j.
The chosen field K_j is contained in R because theta_j is real; composing this inclusion with that automorphism is a real embedding taking theta_j to a negative real number.
A square in K_j has nonnegative image under every real embedding, so theta_j is nonsquare in K_j.
This completes the induction, proves [K_j:K]=2^j, and shows deg_Q(theta_j)=2Dk.
The monic integer polynomial P_mu(z^k) vanishes at theta_j and has exactly that degree, so it is its irreducible minimal polynomial.

The reciprocal trace identity is

    z^(Dk) T_mu(C_k(z+z^(-1)))=P_mu(z^k).

If T_mu(C_k) factored over Q, each monic positive-degree trace factor would yield a nonconstant polynomial factor on the left after its own reciprocal trace substitution, contradicting the proved irreducibility of P_mu(z^k).
Thus T_(mu,j) is irreducible of degree Dk, with eta_j as a root.
The relation C_k(eta_j)=tau gives F contained in F_j.
All degrees in LC19 follow, including [K_j:F_j]=2 and [F_j:F]=k, independently of the higher fields' signatures.
The same-value norm of g in F from F_j to F is g^k and from K_j to F is g^(2k), because the full relative degrees are k and2k.
Taking the remaining norm to Q proves LC22, agreeing with the [actual self-composition norm interface retained in C724](Yin_C_G0724_v1.md#complete-argument).

For each nonzero original root lambda, all k roots of z^k=lambda have modulus |lambda|^(1/k), are distinct, and contribute in total log max(1,|lambda|) to the full logarithmic Mahler measure.
The base polynomial is separable and has nonzero constant term, so these root sets are disjoint and simple.
The base root count therefore gives the stated k/k/(2D-2)k counts and the house and full measure in LC20.
Coefficient insertion preserves H, while the surjective map z to z^k on the complex unit circle preserves the TRUE supremum S.
This establishes all three analytic costs in LC20 without discarding any original factor or conjugate.

For exact canonical covariance use [C724's all-six monic-division identities](Yin_C_G0724_v1.md#complete-argument), with the already proved actual equality T_(mu,j)=T_mu(C_k).
After division by an exact coefficient power of2, composition preserves nonzero binary reduction because C_kbar=X^k and composition by X^k is injective on F_2[X].
This proves the exact-order assertions, not only preservation of a supplied congruence.
The [exact derivative identity of C724](Yin_C_G0724_v1.md#exact-trace-derivative-descent) gives LC21, since C_(2^j)'=2^j times a monic integer polynomial and composition and multiplication by monic polynomials preserve coefficient order.
For odd mu, if D is odd then the leading derivative coefficient D is odd.
If D is even, the coefficient of X^(D-2) in T_mu' is -mu(D-1), also odd, since C_D has no X^(D-1) term and W is monic.
Thus ord_2(T_mu')=0 in all odd-mu cases, including D=2.
Specializing the already proved table to mu=5 proves LC23 and completes the extension.

## Current assessment
[Selected decision](#decision-whole-reviewed-2026-10-25)

## Assessment history

### Decision priced-chebyshev-family-open

| Field | Value |
| --- | --- |
| date | 2026-10-25T17:47 |
| status | open |
| reason | Register the complete LC1--LC23 statement and author argument after both contributors read the entire integrated candidate. Exact SAME-divisor canonical orders, every r/D/u/sign endpoint, actual Salem irreducibility with complete coefficient/circle/measure costs, the fixed-degree cyclotomic2-adic limit, and norm-controlled irreducible dyadic towers are retained. The r=5 second-residual bound remains only a lower bound; the full joint order is exact. These explicit families do not realize C691's nonzero binary canonical source, a near-one family, a passing characteristic-zero certificate or unrestricted Task completion. Fresh isolated whole review and a separate acceptance decision remain outstanding. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire priced-family and tower statement](#statement) | LC1--LC5, the full valuation table, LC16--LC23, all odd-mu algebra versus positive-mu Salem and extra-nonsquare tower domains, r=5 limitation, full degrees/root counts/measure/norm multiplicities, both signs and every endpoint. |
| argument | [Complete canonical, Salem and tower proof](#complete-argument) | LC6--LC15 and the complete root/irreducibility/measure proof of LC5, followed by both directions of the square criterion and every step of the LC18--LC23 positive-root, degree, norm, analytic and exact-precision tower proof. |
| argument | [Complete fixed-degree limit argument](#fixed-degree-two-adic-cyclotomic-limit) | LC16--LC17: actual coefficient compatibility, full diverging archimedean costs, exact cyclotomic product and all six canonical zero limits, with irreducibility/nontorsion and topology limitations. |
| dependency | [Adopted full binary trace-root and canonical calculation](Yin_C_G0726_v1.md#decision-whole-reviewed-2026-10-25) | Full squarefree degree-D U, all odd2D-1 root orders and zero trace, Wbar squared equal to X, nonzero residual remainder witnesses and odd-power closure; the new coefficient-dependent valuations are proved here. |
| dependency | [Adopted actual integer canonical interface](Yin_C_G0697_v1.md#decision-whole-reviewed-2026-10-25) | Integrality of the actual divided monic remainders and DP7 a/b/c/F/X_s covariance only; no higher precision or irreducibility is imported. |
| dependency | [Adopted all-six exact composition and derivative interface](Yin_C_G0724_v1.md#decision-whole-reviewed-2026-10-25) | Actual G covariance, preservation of exact coefficient orders and vanishing, HD8 exact trace-derivative order, full H/S/measure and same-value norm interface. Its C586v2 self-composition norm multiplicities are retained and proved directly here from the actual degrees; no total-reality or bounded-height existence input is imported. |
| dependency | [Accepted monic rational-factor integer-coefficient property](../audits/literature/Con26d/Yin_U001.md#con26d-u001) | Theorem2.1, printed pages2--3, monic integer P factorizations into monic rational factors are integral. Only this accepted statement is used; no Eisenstein assertion or new whole-source proof audit is claimed. |
| dependency | [Accepted Kronecker characterization](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Printed p322 measure-one integer-polynomial characterization, including all cyclotomic factors and multiplicities; applies to a hypothetical leftover monic factor with all roots on the circle and constant coefficient plus or minus1. Preserve the U's recorded inspection limits. |
| support | [Adopted original coefficient-three Salem mechanism](Yin_C_G0136_v1.md#decision-isolated-current-whole-review-20261022-m04) | Attribution for the alternating trace-node and torsion-norm proof mechanism in Section1. Its q=5^r coefficient3 statement does not supply the present every-D and every-positive-mu extension, which is fully proved here. |
| support | [Adopted norm-controlled tower mechanism](Yin_C_G0711_v1.md#decision-whole-reviewed-2026-10-25) | Attribution for SL8 nonsquare and positive-root induction, directly read and explicitly adapted to the exact norm2(mu+1). No claim that the present family satisfies the older prescribed CRT, or that its old review covers this adaptation. |
| support | [Full nonzero-binary source boundary](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | Comparison only: its required nonzero canonical binary R and separate synthetic integer/Haar data. Every finite r>=2 member here has actual nonzero G with Gbar=0, so this family does not realize that source. |

### Decision whole-reviewed-2026-10-25

| Field | Value |
| --- | --- |
| date | 2026-10-25T17:56 |
| status | proved |
| reason | Adopt the complete LC1--LC23 theorem after reading the entire fixed statement, both complete argument locations and fresh independent whole R950. Exact canonical divisions and full-root valuations, all D/r/u/sign endpoints, actual positive-coefficient Salem irreducibility, full circle/height/measure costs, the fixed-degree cyclotomic two-adic limit, both directions of the nonsquare criterion and every irreducible tower degree/root/norm/precision are supported. LC6 product notation was clarified by an explicit multiplication sign, preserving the identity and expansion already explicitly checked in R950. The r=5 second-residual order remains only a lower bound; the nonsquare norm is sufficient only. Actual finite nonzero G has zero binary reduction, and neither this limit nor the towers realize C691, a controlled near-one family or unrestricted G0001 completion. |

| Relation | Target | Scope |
| --- | --- | --- |
| statement | [Entire priced-family and tower statement](#statement) | LC1--LC5, the full valuation table, LC16--LC23, all odd-mu algebra versus positive-mu Salem and extra-nonsquare tower domains, r=5 limitation, full degrees/root counts/measure/norm multiplicities, both signs and every endpoint. |
| argument | [Complete canonical, Salem and tower proof](#complete-argument) | LC6--LC15 and the complete root/irreducibility/measure proof of LC5, followed by both directions of the square criterion and every step of the LC18--LC23 positive-root, degree, norm, analytic and exact-precision tower proof. |
| argument | [Complete fixed-degree limit argument](#fixed-degree-two-adic-cyclotomic-limit) | LC16--LC17: actual coefficient compatibility, full diverging archimedean costs, exact cyclotomic product and all six canonical zero limits, with irreducibility/nontorsion and topology limitations. |
| dependency | [Adopted full binary trace-root and canonical calculation](Yin_C_G0726_v1.md#decision-whole-reviewed-2026-10-25) | Full squarefree degree-D U, all odd2D-1 root orders and zero trace, Wbar squared equal to X, nonzero residual remainder witnesses and odd-power closure; the new coefficient-dependent valuations are proved here. |
| dependency | [Adopted actual integer canonical interface](Yin_C_G0697_v1.md#decision-whole-reviewed-2026-10-25) | Integrality of the actual divided monic remainders and DP7 a/b/c/F/X_s covariance only; no higher precision or irreducibility is imported. |
| dependency | [Adopted all-six exact composition and derivative interface](Yin_C_G0724_v1.md#decision-whole-reviewed-2026-10-25) | Actual G covariance, preservation of exact coefficient orders and vanishing, HD8 exact trace-derivative order, full H/S/measure and same-value norm interface. Its C586v2 self-composition norm multiplicities are retained and proved directly here from the actual degrees; no total-reality or bounded-height existence input is imported. |
| dependency | [Accepted monic rational-factor integer-coefficient property](../audits/literature/Con26d/Yin_U001.md#con26d-u001) | Theorem2.1, printed pages2--3, monic integer P factorizations into monic rational factors are integral. Only this accepted statement is used; no Eisenstein assertion or new whole-source proof audit is claimed. |
| dependency | [Accepted Kronecker characterization](../audits/literature/Smy08/Yin_U001.md#smy08-u001) | Printed p322 measure-one integer-polynomial characterization, including all cyclotomic factors and multiplicities; applies to a hypothetical leftover monic factor with all roots on the circle and constant coefficient plus or minus1. Preserve the U's recorded inspection limits. |
| support | [Adopted original coefficient-three Salem mechanism](Yin_C_G0136_v1.md#decision-isolated-current-whole-review-20261022-m04) | Attribution for the alternating trace-node and torsion-norm proof mechanism in Section1. Its q=5^r coefficient3 statement does not supply the present every-D and every-positive-mu extension, which is fully proved here. |
| support | [Adopted norm-controlled tower mechanism](Yin_C_G0711_v1.md#decision-whole-reviewed-2026-10-25) | Attribution for SL8 nonsquare and positive-root induction, directly read and explicitly adapted to the exact norm2(mu+1). No claim that the present family satisfies the older prescribed CRT, or that its old review covers this adaptation. |
| support | [Full nonzero-binary source boundary](Yin_C_G0691_v1.md#decision-whole-reviewed-2026-10-24) | Comparison only: its required nonzero canonical binary R and separate synthetic integer/Haar data. Every finite r>=2 member here has actual nonzero G with Gbar=0, so this family does not realize that source. |
| review | [Fresh independent whole review](../audits/reviews/Yin_R_G0950_v1.md#whole-priced-chebyshev-family-finding) | Entire LC1--LC23 statement and both argument locations, all actual canonical orders and endpoints, independent Salem extension, fixed-degree limit and complete nonsquare-norm tower, with exact consumed source scopes and exclusions. |

