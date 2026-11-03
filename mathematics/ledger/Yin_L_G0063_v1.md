---
author: Yin
---

# G0001: integral Sylvester modules and the first extra Frobenius valuation

Date: 2026-10-07.

The complete mathematical proof is now retained in [C237](../claims/Yin_C_G0237_v1.md#mixed-sylvester-domain).
This original dated input remains available with its full mathematics; formal review accounts are retained in [R517](../audits/reviews/Yin_R_G0517_v1.md#historical-sylvester-author-finding).
Bounded direct work by assigned AI ms25_source for Yin.
The coordinating AI independently proposed the cyclic-module elimination and its first lifting interpretation.
The actual contributions and review scope are recorded below.
This argument reuses the full-root conventions and degree guards of [L G0059](Yin_L_G0059_v1.md#mixed-power-resultant-identities).
No source acquisition, computational scan or claim of novelty is used.

The useful output is an exact module realizing the normalized Frobenius quotient, a proof that its mandatory mod-p nullity is exactly d at a base exponent of one even with repeated reduced roots, and a concrete polynomial test for an extra p factor.
The base-exponent Sylvester module reduces integrally to the existing degree-d polynomial matrix; merely introducing d-squared variables adds no arithmetic or entropy information.

<a id="mixed-sylvester-domain"></a>
## Hypotheses and the finite integral module

Let alpha be a nonzero nontorsion algebraic integer, let P be its monic minimal polynomial of degree d, and set

    R=Z[t]/(P),       A=multiplication by t on R,
    E=End_Z(R).

Use the power basis 1,t,...,t^(d-1), so A is the integral companion matrix.
In the primary unit scope A is unimodular, but the results below do not need that stronger hypothesis.
For distinct positive integers a,b define

    S_(a,b)(B)=A^a B-B A^b,
    R_(a,b)=product_(i,j)(alpha_i^a-alpha_j^b).

Diagonalizing the separable companion matrix over C gives

    det S_(a,b)=R_(a,b).                               (1)

This is the full-root mixed resultant of L G0059.
If a cross factor vanished, a finite-order Galois automorphism carrying alpha_i to alpha_j would give alpha_i^(a^r)=alpha_i^(b^r) for some r, contrary to nontorsion.
Thus S_(a,b) is injective over Z, its cokernel is finite, and

    |coker S_(a,b)|=|R_(a,b)|.                         (2)

No degree-preservation hypothesis on the separate powers is needed for (1)--(2): both exponents retain all d original conjugates.

<a id="coefficient-pairing-sylvester-presentation"></a>
## A unimodular coefficient pairing gives the actual presentation

Let tau:R->Z take the coefficient of t^(d-1) in the unique reduced representative, and put

    <u,v>=tau(uv).

The Gram matrix J in the power basis has zero entry when i+j<d-1 and entry one when i+j=d-1.
It is anti-triangular with determinant (-1)^(d(d-1)/2), hence unimodular.
Every multiplication map is self-adjoint for this pairing.
This is the coefficient pairing, not the field-trace pairing; its unimodularity does not require inverting the discriminant or assuming unramified reduction.

The map

    R tensor_Z R -> E,
    u tensor v |-> [w |-> u tau(vw)]

is therefore an integral isomorphism.
Under it, S_(a,b) becomes multiplication by x^a-y^b on Z[x,y]/(P(x),P(y)).
Consequently

    coker S_(a,b)
      is isomorphic to Z[x,y]/(P(x),P(y),x^a-y^b)      (3)

as an abelian group, with the indicated natural module structure.
This presentation is valid also when the displayed quotient is not finite, provided one does not apply (2) outside its hypotheses.

At a=1, substituting x=y^b gives the exact integral reduction

    coker S_(1,b) is isomorphic to R/P(t^b)R
                 is isomorphic to coker P(A^b).       (4)

Eliminating the powers of x using the monic relation x-y^b has d(d-1) unit pivots and leaves the d relations P(y^b) in R.
Thus S_(1,b) is unimodularly equivalent to

    I_(d^2-d) direct-sum P(A^b),                       (5)

up to a harmless sign convention.
Alternatively (4) and integer Smith normal form prove (5).
No rational basis change or index division is involved.
For b=1 this gives the useful boundary coker[A,-] isomorphic to R, a free group of rank d; its image is therefore saturated.
The finite determinant claim (2) was only for a!=b.
The separate [adjoint quotient and commutator-torsion construction](Yin_L_G0061_v1.md#commutator-torsion-index) uses this saturated boundary in an integral dynamical system; its entropy and periodic-growth claims are not additional premises here.

<a id="frobenius-intertwiner-floor"></a>
## The mandatory p-to-the-d factor, including nonreduced algebras

Fix a prime p and r>=1, and suppose b=a p^r.
Work first in the possibly nonreduced finite algebra R_bar=F_p[t]/(P mod p).
Let F_r(z)=z^(p^r), an F_p-linear ring endomorphism.
It need not be injective.
It satisfies

    F_r A^a=A^b F_r.

For z in R_bar, multiplication by z commutes with A^b, so m_z F_r obeys the same relation.
Taking adjoints in the reduction of the unimodular coefficient pairing gives

    W_z=(m_z F_r)^*,
    A^a W_z=W_z A^b.                                  (6)

The map z->W_z is injective: its adjoint applied to 1 is (m_z F_r)(1)=z.
Hence

    dim_Fp ker(S_(a,b) mod p)>=d.                      (7)

This explicitly realizes d Frobenius intertwiners without ever inverting F_r.
Assuming its invertibility would incorrectly exclude nonreduced reductions.

There is a corresponding integral quotient.
Lift F_r to the integral linear map F_hat whose j-th power-basis column is the remainder of t^(p^r j) modulo P, so F_hat(1)=1.
Define the integral map W:R->E by W(z)=(m_z F_hat)^*.
The map B->B^*(1) is a left inverse to W, so W(R) is a primitive rank-d summand of E.
By (6), S_(a,b)(W(R)) is contained in pE.
Set

    E'=E+(1/p)W(R) inside E tensor Q.

Then [E':E]=p^d and S_(a,b):E'->E is integral and injective.
This over-lattice depends only on the displayed mod-p intertwiner subspace, not on a choice of lifts of F_r.
There is an exact sequence

    0 -> R/pR -> coker(S_(a,b):E->E)
       -> coker(S_(a,b):E'->E) -> 0.                   (8)

The first map sends z modulo pR to S_(a,b)(W(z))/p modulo S_(a,b)E.
It is well defined, and injective because S_(a,b) is injective over Q and W is primitive.
In particular

    |coker(S_(a,b):E'->E)|=|R_(a,b)|/p^d.              (9)

Thus the normalized integer in L G0059 is the order of a specified finite quotient, not only an integer obtained by determinant division.
This identification alone supplies no lower bound beyond one on that quotient's order.

<a id="base-prime-power-extra-valuation"></a>
## Base exponent one: exact nullity and the first higher lifting test

Take a=1 and b=p^r.
Coefficientwise Frobenius and Cayley--Hamilton give

    P(A^b)=0 modulo p.

Equation (5) therefore proves the stronger exact statement

    dim_Fp ker(S_(1,b) mod p)=d,                       (10)

including every nonreduced P mod p.
Define the integer polynomial of degree less than d

    rho_b(t)=rem_P(P(t^b))/p,
    C_b=P(A^b)/p=rho_b(A).                             (11)

The remainder is coefficientwise divisible by p since P(t^b)=P(t)^b modulo p.
The all-d-column division in (11) is therefore integral.
Equations (4)--(5) give

    |R_(1,b)|/p^d=|det C_b|
                 =|Norm_(Q(alpha)/Q) rho_b(alpha)|.    (12)

The particular over-lattice in (8) uses the full mod-p kernel by (10).
After the unimodular reduction (5), it divides precisely the last d domain directions by p.
Its cokernel is consequently isomorphic to coker C_b.
This proves that the normalized Sylvester quotient is the same degree-d arithmetic object as the Frobenius polynomial quotient, rather than a new invariant.

All additional p-adic length is the one in C_b.
In particular

    v_p(R_(1,b))>d
      iff C_b mod p is singular
      iff gcd(P mod p,rho_b mod p) has positive degree. (13)

The last equivalence holds for arbitrary P mod p: multiplication by rho_b is invertible in F_p[t]/P precisely when rho_b is a unit there, and Bezout characterizes units by that gcd.
No squarefree assumption is required.
Also |R_(1,b)|/p^d=1 precisely when rho_b(alpha) is a unit in R; its inverse then follows from its monic characteristic polynomial of constant coefficient +/-1.

An explicit lifting formulation is useful.
For any integral square matrix S with nonzero determinant, put

    K_p=ker(S mod p),       Q_p=coker(S mod p).

Its first lifting map is

    beta_p:K_p->Q_p,
    x |-> S(x_hat)/p modulo (pE+S(E)),                 (14)

where x_hat is any lift of x.
Changing the lift by p times an integer vector changes the output by S(E), so this map is well defined.
In Smith coordinates it is diagonal with entries s_i/p modulo p over the indices with p dividing s_i.
Thus the dimension of its kernel is the number of Smith factors divisible by p^2.
For S_(1,b), (5) identifies (14) with C_b mod p.
Equation (13) is exactly the failure of this first lifting map to be invertible.
Further valuations require the higher p-adic structure of C_b, not a larger mandatory kernel in (10).

<a id="nonbase-index-and-nullity"></a>
## Nonbase exponents: order indices identify the modular boundary

Let T be any d by d matrix over F_p and q=p^r.
Then

    dim Hom_(F_p[u])(V_(T^q),V_T)>=d,
    equality holds iff T is cyclic.                   (15)

Here is a direct proof, including inseparability.
Extend the field to its algebraic closure; nullity does not change.
For each eigenvalue lambda, the Jordan partition for lambda is the same as that for lambda^q, because T has coefficients in F_p.
In T^q each Jordan nilpotent block J_l is replaced by J_l^q, which splits into blocks of lengths at most l and total length l.
For a fixed eigenvalue, Hom dimension is the sum of min(l,s) over every target block l and every resulting source block s.
If there is a single target block of length l, this sum is l.
If there is more than one target block, the largest block alone contributes the total local dimension: every source block has length at most that largest length.
Each additional target block contributes strictly positively.
The sum is therefore strictly greater than the local dimension.
Equality at every eigenvalue is exactly cyclicity of T.
This proves (15).

For T=A^a mod p, its minimal polynomial is also the minimal polynomial of the element t^a in R_bar: an annihilating polynomial of that multiplication operator is zero if and only if it kills 1.
Thus its degree is the rank of the power-coordinate span 1,t^a,...,t^((d-1)a).
The matrix of that span is C_a of L G0059, with determinant b_a.
Consequently (15) specializes to

    dim ker(S_(a,ap^r) mod p)=d iff p does not divide b_a,
    dim ker(S_(a,ap^r) mod p)>d iff p divides b_a.      (16)

When alpha^a preserves degree, |b_a|=I_a is the index [Z[alpha]:Z[alpha^a]].
For any integral injective square matrix, v_p(det S) is at least its mod-p nullity.
Therefore a prime dividing this order index forces extra valuation beyond the mandatory p^d already at the first modular level.
This does not assert the converse for higher valuations: at a=1, I_1=1 always, yet (13) can still detect extra p factors.

Globally, if I_a=1 the power basis of alpha^a is an integral basis of R, and the same elimination as (4) gives

    coker S_(a,b) isomorphic to coker P^[a](A^b).       (17)

Locally at p this reduction remains valid if p does not divide I_a.
At primes dividing I_a it is not a valid unimodular change of coordinates.
Independently of that module issue, the determinant identity

    |det P^[a](A^b)|=|R_(a,b)|                        (18)

always holds by the full-root product.
For b=ap^r this d by d matrix is again divisible by p, since P^[a] is the characteristic polynomial of A^a and coefficientwise Frobenius applies.
Thus a degree-d determinant still represents the normalized number even where it cannot represent the entire Sylvester cokernel integrally.

For an exact boundary control, take P=t^2-3t+1, its positive root alpha>1, a=3,b=6,p=2.
It is an irreducible reciprocal unit polynomial, and all positive powers preserve degree because the two positive conjugates alpha and alpha^(-1) have distinct powers.
The identity A^2=3A-I gives A^3=8A-3I, so both A^3 and A^6 reduce to I modulo 2.
Hence S_(3,6) is zero modulo 2, its nullity is four rather than d=2, and I_3=8.
Here P modulo 2 is squarefree; the obstruction is the powered order, not ramification of P at 2.
This hand-checked quadratic example lies outside the small-Mahler window and supplies no near-Lehmer example or numerical evidence.

<a id="sylvester-entropy-and-next-condition"></a>
## Entropy scope and the changed arithmetic obligation

All identities retain the original polynomial P and its original Mahler logarithm m(P), the primary companion-flow algebraic entropy.
The endomorphism S_(a,b) has rank d-squared and eigenvalues alpha_i^a-alpha_j^b; its own algebraic entropy is not identified with m(P), or with log|R_(a,b)|.
A finite cokernel alone does not make that identification.
Unimodular elimination preserves the integer module and determinant but does not give a free Euclidean norm bound for an entropy estimate.

At a=1, (4) and (12) show exactly why the Sylvester presentation adds no arithmetic to the previously available polynomial matrix.
The useful sharper obligation is (13): any attempt to force extra p valuation must prove noninvertibility of the specified first Frobenius quotient in R/pR, and then control its higher lifting or the size and frequency of such contributions.
At nonbase levels, (16) separates additional first-layer factors coming from powered order indices.
Neither condition is automatic or quantitatively uniform under the stated hypotheses.

The existing Lehmer control in [J G0009](../computations/programs/Yin_J_G0009/readme.md) has normalized base resultants of absolute value one at p=2,3.
In this module language both corresponding C_b are unimodular, hence there is no additional finite quotient to exploit at those two choices.
This is reuse of a retained computation, not a new calculation or a refutation of a general growth law.
Other primes, exponent levels and genuinely new uniform arithmetic information remain outside this finite structural result.

<a id="sylvester-review-scope"></a>
## Actual contribution and review scope

Original drafting, actual elimination/lifting contribution and remaining whole-review accounts are retained in [R517](../audits/reviews/Yin_R_G0517_v1.md#historical-sylvester-author-finding).
The original 2026-10-07 date, actual contributions and full check scopes remain there, with current finding-specific relationships.
No new source, computation, uniform arithmetic estimate or resolution of G0001 is asserted.
