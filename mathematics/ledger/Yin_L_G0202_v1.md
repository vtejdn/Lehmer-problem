---
author: Yin
---

# Minimal Frobenius valuation, exact cyclic quotients and prime-power lifts

Date: 2026-10-10.

<a id="minimal-frobenius-fixed-scope"></a>
## Adopted scope

The coordinating AI for Yin retains resultant_research's complete new argument and its own complete separate noncontributor review, including the disclosed earlier dependency contributions.
The hypothesis is only minimal p-adic valuation d of the full powered resultant at the selected prime p; other prime factors are allowed.
Reciprocity is unnecessary for the general quotient and irreducibility statements.

For every exponent n prime to p, the actual p-primary cyclic and cyclotomic quotient rings are the explicitly identified reduced finite F_p algebras, and their exact norm valuations are the degrees of the displayed modular gcds.
Repeated reduced factors contribute only their distinct degrees at this first layer.
The same hypothesis excludes p-th powers inside the original number field and proves that every P(t^(p^k)) is actually irreducible.
Full resultant and cyclic root-fiber identities retain all roots and multiplicities.
The degree-six saturated Salem input and the original Lehmer input give explicit higher-exponent degree-linear p-adic peaks on their full radical lifts.

The peak constants and exponents depend on the fixed base; the actual lifted polynomials have constant positive total Mahler measure.
These results neither establish coverage of near-one inputs nor control varying-input inverse or full complementary-factor costs.
G0001 remains active and unresolved.

The full author proof and complete review follow.
Historical pending-review text preserves chronology; the appended review determines the adopted review scope.
Only heading depth and relative navigation are transformed.

<a id="retained-minimal-frobenius-proof"></a>
## Saturated actual-order inverses and longer cyclic arithmetic

Date: 2026-10-10.
Starting question: Seek a genuinely new varying-input inverse/full-cofactor estimate or a longer-exponent arithmetic consequence of saturation beyond L197 short norms.
Retain the whole near-one coverage boundary, actual orders and all complementary factors.
A fixed-base lift is a control, not a new near-one mechanism.

The full unrestricted Task remains active and unresolved.


<a id="minimal-frobenius-cyclic-quotients"></a>
### 1. A local condition and its complete prime-to-p consequences

Let P in Z[t] be the monic irreducible polynomial of a nontorsion algebraic unit alpha, of actual degree d.
Let p be any rational prime.
Retain all conjugate multiplicities in P^[p], and write

    R_p=Res(P,P^[p]),
    C_n=|Norm(alpha^n-1)|,
    D_n=|Norm(Phi_n(alpha))|.

Assume exactly

    v_p(R_p)=d.                                              (1)

Thus the p-part of the full Frobenius resultant is minimal; surplus at other primes is allowed.
In particular the entire saturated doubling class of L194 satisfies(1) with p=2.
Reciprocity is not needed for Sections1-5.
No theorem asserts(1), or full saturation, for every sufficiently near-one input.

For every n>=1 with p not dividing n, put

    g_n=gcd(P mod p,t^n-1) in F_p[t],
    h_n=gcd(P mod p,Phi_n mod p).

Both gcds are monic and squarefree, regardless of multiplicities in P mod p.
The new claim is the exact ring structure

    (O/(alpha^n-1)O)_(p) isomorphic to F_p[t]/g_n,
    (O/Phi_n(alpha)O)_(p) isomorphic to F_p[t]/h_n,            (2)
    v_p(C_n)=deg g_n,          v_p(D_n)=deg h_n,

where O=Z[alpha] and the subscript(p) means its finite p-primary ring, equivalently tensoring the finite quotient with Z_(p).
These p-primary groups are killed by p and are products of finite fields.
A gcd equal to1 gives the zero ring.
The other prime parts of the complete quotient and norm remain present and uncontrolled; (2) does not say that the full quotient is killed by p, or that p/(alpha^n-1) belongs to O globally.

#### Reuse and exact algebraic input

The local screen read [L63's normalized Frobenius quotient and first-lifting criterion](Yin_L_G0063_v1.md), [L78's complete local cyclotomic layers](Yin_L_G0078_v1.md#old-layer-exception-threshold), [L197's short-return and odd-prime restrictions](Yin_L_G0197_v1.md#saturated-short-cyclic-fixed-scope), and the actual controls in L200 and J10.
The prime-binomial root-product argument below is reused from [L159](Yin_L_G0159_v1.md#irreducible-lehmer-radical-control); its earlier accepted degree-only source bound is not used here.
The construction below proves its finite-ring lifting step directly and adopts no new p-adic or external source theorem.
A bounded local screen found no matching all-prime-to-p quotient or p-power radical conclusion; no literature-priority claim is made.

Define the integral Frobenius defect

    E_p(t)=[P(t^p)-P(t)^p]/p.                                (3)

Coefficientwise Frobenius proves integrality.
At alpha, E_p(alpha)=P(alpha^p)/p.
The complete powered polynomial gives

    Norm(P(alpha^p))=Res(P^[p],P)=(-1)^(d^2) R_p.

Consequently multiplication by E_p(alpha) in the actual monic power basis of O has determinant with p-valuation zero under(1).
Its reduction is invertible on F_p[t]/Pbar, so

    gcd(Pbar,E_p mod p)=1.                                  (4)

This uses only a unit modulo p, not a unit of O at every prime.
Equation(4) is the normalized Frobenius criterion already present in L63; the new use is on prime-to-p cyclic quotients.

### 2. Elementary proof of the entire quotient, including bad reduction

First take N(t)=t^n-1, p not dividing n, and work in the finite free ring

    A=(Z/p^2 Z)[t]/N(t).

The substitution sigma:t -> t^p is an automorphism: choose an inverse exponent modulo n.
Reduction modulo p is the ordinary Frobenius automorphism on

    Abar=F_p[t]/N,

a product of finite fields because N'=n t^(n-1) is coprime to N.
Let ebar be its idempotent equal to1 precisely on the factors where Pbar vanishes, and zero on all other factors.
Its component ring ebar Abar is F_p[t]/g_n.

Every idempotent of Abar has a unique idempotent lift e to A.
Here is the elementary square-zero argument.
Lift ebar arbitrarily to e_0.
Correct it by p u.
The idempotence equation modulo p^2 is

    (e_0^2-e_0)/p+(2 e_0-1)u=0 modulo p.

The coefficient 2 ebar-1 has square1 and is invertible.
This determines u uniquely modulo p and gives the required lift.
The ring A is free over Z/p^2, so the division of the known multiple of p and the correction modulo p are well defined.
Since sigma reduces to Frobenius and fixes every idempotent of Abar, uniqueness gives sigma(e)=e.

On eA, one has eP in p eA, so eP^p=(eP)^p=0 modulo p^2.
The identity(3) in A therefore gives

    e sigma(P)=p e E_p,
    eP=p sigma^(-1)(e E_p).                                (5)

By(4), e E_p is a unit of eA modulo p, hence a unit of eA: an inverse modulo p lifts by the finite geometric correction for the square-zero ideal p eA.
Equation(5) shows that the ideal generated by eP is exactly p eA.
On (1-e)A, P is already a unit modulo p and thus is a unit in that component.
It follows that

    A/(P) isomorphic to eA/p eA
                      isomorphic to F_p[t]/g_n.             (6)

Now let C=Z[t]/(P,N), which is finite because P is nontorsion.
Its reduction C/p^2 C is exactly(6).
If its finite p-primary additive group had a Smith factor divisible by p^2, then C/p^2 C would have an element of additive order p^2.
Equation(6) rules this out.
Thus the p-primary part of C is killed by p, and reduction modulo p identifies it, as a ring, with C/pC=F_p[t]/g_n.
This proves the first statement of(2), not just a lower bound from mod-p nullity.

For the second statement use N=Phi_n.
It remains a squarefree divisor of t^n-1 modulo p, and t -> t^p is an automorphism of Z[t]/Phi_n when p is coprime to n, with the inverse exponent modulo n.
The same proof applies verbatim, giving the second ring and valuation formulas.
No squarefree reduction of P, discriminant restriction, maximal-order assertion or preservation of degree under alpha -> alpha^p is used.

Equivalently, factor the reduction into distinct irreducibles as

    Pbar=product_phi phi^(e_phi),

and let r_phi be the multiplicative order of a root of phi.
The unit constant coefficient ensures r_phi is defined and prime to p.
The exact formulas become

    v_p(C_n)=sum_(r_phi divides n) deg phi,
    v_p(D_n)=sum_(r_phi=n) deg phi,       p not dividing n.    (7)

The exponents e_phi do not appear.
This is actual initial local depth, including repeated reduction, rather than the original-root multiplicity count used for later stable layers in L78.

<a id="minimal-frobenius-p-power-irreducibility"></a>
### 3. Minimal Frobenius valuation excludes a pth root in the same field

Under(1), alpha is not a pth power in K=Q(alpha).
Suppose instead alpha=gamma^p with gamma in K.
Both gamma and its inverse are integral by the monic equations over the algebraic integers, so gamma is a nontorsion algebraic unit.
Also Q(gamma)=K.
If G is its actual monic minimal polynomial, deg G=d and its complete pth-powered polynomial is P.
Thus

    G mod p=P mod p,

by coefficientwise Frobenius on the elementary symmetric functions of the conjugates.

Choose n prime to p divisible by every reduced root order r_phi, and put

    r=deg rad(Pbar)>=1.

By(2), v_p(C_n(alpha))=r.
On the other hand

    alpha^n-1=(gamma^n-1) S_p(gamma^n),
    S_p(y)=1+y+...+y^(p-1).

Both factors are nonzero.
For any integral multiplication matrix, the p-valuation of its nonzero determinant is at least its nullity modulo p, as follows directly from integer Smith normal form.
Multiplication by a polynomial h in F_p[t]/Gbar has nullity deg gcd(Gbar,h): writing Gbar=g G_1 and h=g h_1 with coprime G_1,h_1 proves this even with repeated factors.

For h=t^n-1 that degree is exactly r.
For h=S_p(t^n), use

    S_p(t^n)=(t^n-1)^(p-1) modulo p,

whose gcd with Gbar has degree at least r.
Norm multiplicativity consequently gives

    v_p(C_n(alpha))
       =v_p(Norm(gamma^n-1))+v_p(Norm(S_p(gamma^n)))
       >=2r,

contradicting the exact value r.
This rules out the pth root without any external lower bound for Mahler measure or any good-reduction assumption.

The elementary prime-binomial argument now proves X^p-alpha irreducible over K.
A proper monic factor of degree1<=a<p would give the product c of its selected roots in K with c^p=alpha^a.
Choosing integers u,v with au+pv=1 would give (c^u alpha^v)^p=alpha, contrary to the preceding result.
If beta^p=alpha, the tower K subset Q(beta) therefore has degree p, and

    P(t^p) is irreducible of degree dp.                      (8)

### 4. All p-power lifts are actual inputs with the same total measure

For any positive integer q, put F(t)=P(t^q).
Even when F has not yet been proved irreducible, full root-fiber evaluation gives

    Res(F,F^[p])=R_p^q,                                     (9)

where F^[p] denotes the complete pth-powered polynomial of F, with every multiplicity.
To avoid assuming a false composition formula when p divides q, compute first the norm product

    product_(beta^q=alpha_i, all i) P((beta^p)^q)
       =[product_i P(alpha_i^p)]^q.

Each factor is repeated q times.
Converting each side from Res(F^[p],F) to Res(F,F^[p]) has total sign exponent d^2(q^2+q), which is even.
This proves the signed identity(9).
It does not assert F^[p]=P^[p](t^q) when p divides q.

In particular its p-valuation is dq under(1).
Combining this preservation with(8) inductively proves

    F_k(t)=P(t^(p^k)) is irreducible of degree d p^k
    for every integer k>=0.                                (10)

It remains a nontorsion algebraic unit; if the base is reciprocal so is each F_k.
Root-fiber grouping also proves M(F_k)=M(P).
The total positive logarithmic measure is fixed along this family, while its p-power reduction is

    F_k mod p=Pbar^(p^k).

Thus (7) gives, simultaneously for every n prime to p,

    v_p(C_n(F_k))=deg gcd(Pbar,t^n-1)<=r,                    (11)

independently of k, even as the actual degree d p^k grows.
This is an exact all-prime-to-p income limitation.
It is distinct from L194's already retained fixed-base odd-lift bounded primitive auxiliary/cofactor cost; no new assertion about that cost is made here.

<a id="p-power-delayed-cyclic-income"></a>
### 5. Exact movement of local income into p-divisible exponents

For a monic polynomial F, write C_n(F) for the absolute product of beta^n-1 over all roots beta of F with multiplicity.
This agrees with the actual field norm when F is irreducible.
For any radical polynomial F(t)=P(t^q), the same full fiber argument gives

    C_n(F)=C_(n/g)(P)^g,             g=gcd(n,q).              (12)

Indeed the nth powers in one qth-root fiber consist of the q/g roots of t^(q/g)-alpha_i^(n/g), each repeated g times.
Evaluating their product against1 gives the claimed absolute norm after multiplying all original fibers.
This proof retains repeated powered roots and needs no within-level degree preservation.

For q=p^k and n=p^j u with p not dividing u, (12) implies, throughout0<=j<=k,

    v_p(C_(p^j u)(F_k))
       =p^j deg gcd(Pbar,t^u-1).                            (13)

Consequently linear p-income A_p(n)=v_p(C_n)log p of at least eta*d p^k, at an exponent with j<=k, requires

    p^(k-j)<=r log p/(eta d).                               (14)

A fixed eta>0 therefore forces v_p(n) to be within a bounded distance of k, or larger than k.
Prime-to-p exponents cannot supply that income along these actual families.
This identifies where the mass is delayed; it does not say that no affordable p-divisible exponent exists.

In fact choose u_0 to be a common reduced-root period.
Then

    v_p(C_(p^k u_0)(F_k))=p^k r,
    (p^k u_0)/(deg F_k)=u_0/d.                              (15)

This is a genuine same-exponent linear local income along each fixed base, with a base-dependent exponent cost.
The order u_0 and the ratio r/d are not controlled uniformly over varying near-one bases.
Neither(15) nor the root-order formula supplies the missing unrestricted L168 coverage.

#### Two actual controls with different repeated reductions

For the [L200 degree-six input](Yin_L_G0200_v1.md#degree-six-principal-saturation-fixed-scope), p=2, P=t^6-t^5-t^3-t+1 and R_2=2^6.
Its reduction is Phi_3^3.
Equations(10)--(13) give actual irreducibility and saturation of every P(t^(2^k)), degree6*2^k, and

    v_2(C_n)=2 if3 divides n, and0 otherwise, for every odd n;
    C_(3*2^k)(P(t^(2^k)))=4^(2^k).                         (16)

The second equality is the complete norm, since L200 gives C_3(P)=4 and(12) gives the whole product.
At that exponent n=(deg F_k)/2 its logarithm is(deg F_k)log2/3.
At all odd exponents the dyadic income is at most2 log2; possible odd-prime income at larger odd exponents is not bounded here.
These statements include highly repeated reduction and actual irreducibility, not cyclotomic padding.

For the original Lehmer base, L66 gives R_2=2^10.
The retained exact [J10 factor/order certificate](../computations/programs/Yin_J_G0010/readme.md) has two distinct degree-five factors modulo2, both with root order31.
The new theorem, reusing those already verified finite facts without a new run, gives irreducibility of every dyadic lift, degree10*2^k, and

    v_2(C_n)=10 if31 divides n, and0 otherwise, for odd n;
    v_2(C_(31*2^k))=10*2^k.                                 (17)

This reaches local income(deg F_k)log2 at exponent31/10 times the degree on this fixed base.
It does not need L159's degree-only source bound or a large-prime cutoff.
Both control families keep their fixed positive base measure; the dyadic lifts generally have many expanding roots and are not asserted Salem or near-one sequences.

### Contribution, checking and next boundary

The assigned resultant_research AI developed all new deductions in Sections1-5.
The coordinator supplied only the broad question and received interim findings, not a derivation.
Fixed reuse consists of L63's normalized Frobenius criterion, L78's existing local-layer comparison, L159's displayed elementary prime-binomial proof, L200's degree-six algebra and L66/J10's original Lehmer resultant and mod-two factors/orders.
No new external theorem, source acquisition, program, numerical run or J is introduced.

Self-check covered the sign in the full resultant/norm conversion, square-zero idempotent lifting in the actual finite ring, the automorphism and its fixed idempotent, passage from the quotient modulo p^2 to the entire finite p-primary group, repeated reduction, n=1, unit and nontorsion assumptions, the same-field degree equality in the pth-root contradiction, both determinant nullities, complete radical fibers, p-divisible q, actual irreducibility induction, all local and complete norm distinctions, and the fixed-measure boundary.
The proof is ready for separately organized full review; no independent review is asserted here yet.

The changed arithmetic result is that minimal Frobenius valuation determines every prime-to-p initial cyclic and cyclotomic layer exactly, including bad reduction, and forces all p-power radical lifts to be genuine irreducible inputs.
The actual lift controls show how growing repeated reduction suppresses all prime-to-p local income while allowing a precisely located linear peak at p-divisible exponents.
They disprove neither a near-one gap nor a uniform estimate essentially using total m tending to zero.
The next useful arithmetic step must control reduced-root periods and radical degree, or the later p-power layers, uniformly as both degree and total measure vary.
The full inverse and complementary auxiliary cost are still uncontrolled on that varying-input domain, and no result puts all near-one inputs under(1).
Other primes, nonsaturated inputs and the parallel routes remain open; G0001 remains active and unresolved.



The original `Yin_R_G0101_v1#minimal-frobenius-complete-independent-review` checked this entire frozen proof and both controls at2026-10-10 day precision; [the later complete comparison](../audits/reviews/Yin_R_G0697_v1.md#l202-and-r101) preserves its actual inputs, verdict, UNKNOWN relationship and original contribution/source/native limits.
