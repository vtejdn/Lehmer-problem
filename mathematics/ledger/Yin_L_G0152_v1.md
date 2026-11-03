---
author: Yin
---

# Primitive inversion orbits and the cost of existence-only return certificates

Date: 2026-10-09.
Prepared by assigned AI `growth_arithmetic_status` for Yin during the authorized bounded G0001 continuation.
The author derived and checked the arguments below.
The coordinator requested a new actual-core arithmetic test and a complete written proof, but supplied none of this work's mathematical derivation.
Complete independent review is recorded below.
The coordinator accepted the result for fixed-ledger preservation on 2026-10-09 under Yin's unchanged G0001 exploration authorization.
No numerical calculation, factor search, new source search, or novelty claim is made.

The fixed trace-field interface is [L G0066](Yin_L_G0066_v1.md#reciprocal-trace-domain), and the exact meaning of primitive ideal mass is [L G0078](Yin_L_G0078_v1.md#primitive-cyclotomic-local-layers).
The real-cyclotomic norm identity below is a direct elementary application of this trace construction, not a claim of a newly discovered identity.
The new test distinguishes actual primitive mass from the weaker mass floor obtained solely by closing one primitive witness under inversion.
Its cost comparison permits arbitrary nonnegative cyclotomic weights and the exact joint circle supremum, not only a least-common-multiple lift.

<a id="primitive-inversion-orbits"></a>
## 1. Actual primitive ideals under inversion

Let P be a monic irreducible reciprocal noncyclotomic polynomial in Z[t], of degree d=2s, with constant coefficient one.
Choose a root alpha, put K=Q(alpha), and let O be the maximal ring of integers.
All norms retain these d embeddings; powers of alpha need not preserve degree.
Write m=log M(P)>0.
The map

    sigma(alpha)=alpha^(-1)

is a nonidentity involution of K, with fixed field F=Q(alpha+alpha^(-1)) and [K:F]=2, as in L G0066.

For r>=3, let Q_r be the finite set of prime ideals q of O at which the residue of alpha has exact multiplicative order r.
Such q lie above rational primes p not dividing r.
Set

    w_q=ord_q(alpha^r-1),
    Prim_r=product_(q in Q_r) Norm(q)^(w_q).                 (1)

This is precisely the part coprime to r of D_r=|Norm_(K/Q) Phi_r(alpha)|, by L G0078.
In particular w_q is also the valuation of Phi_r(alpha).
The integer Prim_r may equal one.

The set Q_r is invariant under sigma.
Also residue degree and w_q are constant on each sigma-orbit, because

    sigma(alpha^r-1)=-alpha^(-r)(alpha^r-1)

and the first factor is a unit.
Write Norm(q)=p^f.
There are exactly two possibilities for each orbit.

* If q and sigma(q) are distinct, the orbit contributes p^(2fw_q) to Prim_r.
  The residue order gives r | p^f-1, so its square root is p^(fw_q), congruent to 1 modulo r and at least r+1.
* If q=sigma(q), sigma induces a nonidentity automorphism on O/q.
  Indeed an identity action would give alpha=alpha^(-1) in this residue field and force r<=2.
  A nonidentity automorphism of order two of the finite field with p^f elements requires f even and is its p^(f/2)-power Frobenius.
  Therefore

      r | p^(f/2)+1.

  This orbit contributes p^(fw_q), whose square root p^((f/2)w_q) is congruent to (-1)^(w_q) modulo r and at least r-1.

These arguments require no unramifiedness, good polynomial reduction, or monogenic maximal order.
In the fixed-orbit case the nonidentity residue action is proved from the order r, rather than assumed from the field involution.

Consequently there is a positive integer S_r such that

    Prim_r=S_r^2,       S_r=1 or S_r>=r-1,
    S_r is congruent to 1 or -1 modulo r.                  (2)

More precisely its sign modulo r is (-1) raised to the sum of w_q over the fixed orbits.
If at least one primitive ideal exists, closing it under sigma already certifies

    log Prim_r>=2 log(r-1).                               (3)

For b_r distinct primitive inversion orbits, the same proof gives log Prim_r>=2b_r log(r-1).
Neither (2) nor (3) is an upper bound on actual mass.
Residue field sizes, the number of orbits, and actual depths can give arbitrarily larger lower certificates than (3).

<a id="real-cyclotomic-primitive-norm"></a>
## 2. The exact trace norm and its unchanged archimedean cost

Write z=alpha+alpha^(-1) and P(t)=t^s T(t+t^(-1)), with T monic irreducible integral of degree s, as in L G0066.
For r>=3, inverse pairs of primitive rth roots of unity give the monic integral polynomial

    Psi_r(x)=product_(a in (Z/rZ)^* / {1,-1})
                         (x-2cos(2pi a/r)),
    Phi_r(t)=t^(phi(r)/2) Psi_r(t+t^(-1)).                 (4)

Integrality follows because the displayed roots are algebraic integers and their set is Galois invariant.
Pairing the inverse conjugates of alpha in the norm then gives

    D_r=|Res(T,Psi_r)|^2,
    |Res(T,Psi_r)|=
       |product_(a in (Z/rZ)^* / {1,-1}) T(2cos(2pi a/r))|. (5)

Resultant interchange affects only a sign.
These resultants are nonzero, since a common trace root would make a root of P a root of unity.
Thus S_r in (2) is exactly the part of |Res(T,Psi_r)| coprime to r.
This is an exact way to inspect actual primitive mass in the half-degree trace field; it does not give an additional independent divisibility floor on top of (1).

For finitely many integers r>=3 choose nonnegative integer weights a_r, not all zero, and put

    H(t)=product_r Phi_r(t)^(a_r),
    G(x)=product_r Psi_r(x)^(a_r),
    D=deg H=sum_r a_r phi(r),
    C(H)=max_(|t|=1) |H(t)|=max_(x in [-2,2]) |G(x)|.     (6)

Here D is the degree cost of the auxiliary polynomial, not the input degree d.
In particular H(t)=t^(D/2)G(t+t^(-1)).
The maximum modulus principle for H and its reverse polynomial gives

    |H(t)|<=C(H) max(1,|t|)^D.

Equivalently, if rho(x) is the larger modulus of the two roots of t^2-x t+1, choosing the root of modulus rho(x)>=1 gives |G(x)|<=C(H)rho(x)^(D/2).
Multiplication over the s trace conjugates, using m=sum log rho(z_j), proves exactly

    |Norm_(F/Q) G(z)|<=C(H)^s exp(Dm/2),
    |Norm_(K/Q) H(alpha)|<=C(H)^d exp(Dm).                (7)

The second inequality is the square of the first.
Thus recognizing the square and halving the trace degree halves both logarithmic sides; it does not improve their quotient.
Ordinary Mahler measure m(T) is not substituted for m(P), consistently with L G0066's entropy boundary.
The elementary circle-norm estimate is also the exact interface of [L G0067](Yin_L_G0067_v1.md#scalar-congruence-norm-domain).

<a id="joint-circle-existence-floor-ceiling"></a>
## 3. All weighted joint-circle tests based only on the order floor

Suppose a primitive ideal is known to exist at every selected index.
Define the existence-only certified mass and the actual primitive mass in this weighted test by

    A_cert=2 sum_r a_r log(r-1),
    A_prim=sum_r a_r log Prim_r.                           (8)

Then A_prim>=A_cert.
Repetition of a factor in H really repeats its valuation, so the integer weights in (8) are legitimate.
By (7), both quantities give valid lower certificates for m:

    m>=(A_prim-d log C(H))/D
      >=(A_cert-d log C(H))/D.                             (9)

Suppose every selected r is at least R>=9.
Since H is monic, C(H)>=1.
Even granting its exact circle supremum, (9)'s existence-only value satisfies

    (A_cert-d log C(H))/D
       <= A_cert/D
       <= sup_(r>=R) [2log(r-1)/phi(r)]
       <= 2sqrt(2) log R/sqrt(R).                         (10)

The same bound holds for the positive part of that value.
The elementary bound phi(r)>=sqrt(r/2) was already used and proved prime-power by prime-power in [L G0004](Yin_L_G0004_v1.md), in its finite cyclotomic-order bound: phi(r)^2/r is the product of p^(a-2)(p-1)^2 for p^a exactly dividing r, and the only factor below one can be 1/2 at p=2,a=1.
Finally log(x)/sqrt(x) decreases for x>=9.
This proves (10) without any estimate of C(H) from coefficients.

Consequently, for any R(d) tending to infinity, these certificates have no uniform positive floor across unbounded d if they use only the guarantees (3) at indices r>=R(d).
This statement allows every finite choice of indices, all nonnegative integer weights depending on P and d, and the exact joint archimedean circle optimization.
Its proof even discards the nonnegative circle expense, so improving that expense cannot remove this particular ceiling.

For example the already accepted all-index existence statement in [Ste77 U001](../audits/literature/Ste77/Yin_U001.md#ste77-theorem-one) supplies (3) for all integer r greater than max{2(2^d-1),exp(452)d^67}.
Using only that existence statement in the tests (8)--(9) falls under (10), with R one more than the floor of this threshold.
This does not newly audit the external theorem or bound the actual mass delivered by its primitive ideals.

In contrast, [L G0080](Yin_L_G0080_v1.md#degree-only-primitive-escape) retains more information than mere existence: a selected actual primitive norm already supplies the stated log(2)/(16d) certificate.
Nothing here replaces that lower bound by (3), denies the retained certificate, or applies (10) to its true norm mass.

<a id="common-exponent-primitive-floor-cost"></a>
## 4. All divisor orders at one common return exponent

There is a separate exact comparison with [L G0074](Yin_L_G0074_v1.md#aggregate-cyclic-norm-criterion).
Fix n>=1 and any set E of divisors r>=3 of n at which a primitive ideal is known.
Ideals having distinct residue orders are distinct, even when their rational primes coincide.
Closing one witness at each r under sigma therefore gives a legitimate common-n mass lower bound

    A_common(n)=2 sum_(r in E) log(r-1)<=log C_n,
    C_n=|Norm_(K/Q)(alpha^n-1)|.                            (11)

Indeed alpha^r-1 divides alpha^n-1 in O, so its primitive valuations are retained at n.
Any additional lifting depth is omitted from (11), not bounded above by it.
The same reasoning follows from the exact cyclotomic factorization and primitive layers of L G0078.

Even selecting every available divisor cannot make this specific existence-only certificate larger than

    A_common(n)<=tau(n) log n<=2sqrt(n) log n       (n>=2),
    A_common(n)/n<=2log n/sqrt(n).                         (12)

The first inequality follows from r-1<r and the exact divisor-product identity sum_(r|n) log r=tau(n)log(n)/2; the second pairs divisors below and above sqrt(n).
Empty E gives zero and causes no exception.

In an unbounded-degree family, demanding A_common(n)>=(1+epsilon)d log2 with a fixed epsilon>0 forces n to tend to infinity.
But (12) then makes n/A_common(n) tend to infinity whenever A_common(n)>0.
Thus this existence-only common-exponent construction cannot also satisfy n<=C A_common(n) with fixed C.
It is not an upper bound on log C_n or on actual primitive valuations.

<a id="primitive-mass-next-obligation"></a>
## 5. What a further primitive-return mechanism must add

The classification (1)--(3) concerns actual prime ideals of the original irreducible core.
It remains valid for hypothetical near-one cores, multiple exterior pairs, ramification, and degree-losing powers.
It supplies a stronger order-only floor than a single unpaired residue-field estimate, and (5) gives an exact real-cyclotomic test.
Neither an increase in the number of available indices nor formal degree halving alone pays the full mass and exponent costs.

To state the remaining obligation without conflating a surrogate with actual mass, put

    E_prim=sum_r a_r [log Prim_r-2log(r-1)]>=0.             (13)

For a desired constant kappa>0, the primitive-only certificate in (9) reaches kappa if and only if

    E_prim>=d log C(H)+kappa D-A_cert.                     (14)

In particular if the rightmost ceiling in (10) is at most kappa/2, then reaching kappa requires E_prim>=d log C(H)+(kappa/2)D.
Actual additional primitive orbits, larger residue norms, or deeper valuations could supply this excess; they are not excluded by the argument.
A separately proved nonprimitive mass contribution could also be added with its exact layer accounting.
The present result supplies neither kind of excess.

This closes the specified existence-only stacking and weighted joint-circle test as a way of upgrading the retained all-index existence guarantee to a uniform gap.
It does not close actual all-prime primitive-mass coverage, joint estimates beyond this norm auxiliary class, or G0001, and it assumes no near-one family exists.


The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0052_v1.md#author-check-and-complete-independent-review), with its original inspected scope and relationship.
