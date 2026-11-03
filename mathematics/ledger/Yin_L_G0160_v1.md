---
author: Yin
---

# Inversion-matched Frobenius returns and their least-prime cost

Date: 2026-10-09 (Asia/Hong_Kong).
Bounded G0001 analysis written by assigned AI `growth_arithmetic_status` for Yin.
That AI proposed the complex-conjugation partial-return mechanism, checked the local norm accounting and splitting-field domain, and performed the bounded source screen.
The coordinating AI supplied the uniform treatment of primes two and three, the explicit quartic control, and the permutation diagnostic separating cycle type from inversion matching.
These contributions were checked and assembled here.
All contributor checks were followed by the complete independent written review recorded below, before fixed-ledger adoption.

The proof reuses the actual local norm identity and automatic lifting from [L74](Yin_L_G0074_v1.md#content-versus-ideal-norm).
Its comparison with existing least-prime inputs uses [L75](Yin_L_G0075_v1.md#chebotarev-period-cost) and [BS96-U001](../audits/literature/BS96/Yin_U001.md#bs96-u001) at their fixed statement-level scopes.
The newly retained source is screened separately in [the CLOZ25 reading note](../audits/literature/CLOZ25/readme.md#cloz25-s8-frobenius-screen); no theorem from that source is needed for the local return proof.
No numerical search, new prime scan, or new uniform Mahler gap is claimed.

<a id="inversion-matched-frobenius-return"></a>
## 1. The exact local relation and its actual norm mass

Let P be a monic irreducible reciprocal noncyclotomic polynomial in Z[t], of degree d=2s and constant coefficient one.
Let alpha be one of its roots, K=Q(alpha), and L its splitting field, realized in C.
Write G=Gal(L/Q), m=log M(P)>0, and

    C_n=|Norm_(K/Q)(alpha^n-1)|>0.

Let u be the number of roots of P on the unit circle.
Complex conjugation restricts to an element c of G.
For a root rho,

    c(rho)=rho^(-1) if and only if |rho|=1.                 (1)

For any tau in G, inversion commutes with tau.
Thus if sigma=tau c tau^(-1), exactly u roots satisfy sigma(rho)=rho^(-1).
These are the tau-images of the roots counted in (1); they need not be the same archimedean subset under the fixed embedding L contained in C.

Let p be a rational prime unramified in L whose Frobenius conjugacy class is the class of c.
Choose a prime ideal Q of O_L above p and let sigma=Frob_Q.
For every x in O_L,

    sigma(x)=x^p modulo Q.

Hence each of the u matched roots satisfies rho^(p+1)-1 in Q.
All roots are algebraic units.
Since p is unramified in L, the integer valuation v_Q has v_Q(p)=1, so

    v_Q(rho^(p+1)-1)>=1

for these u roots.
The signed product over all d original roots is the integer Norm_(K/Q)(alpha^(p+1)-1).
Applying v_Q to this product gives its rational p-adic valuation because v_Q(p)=1.
All other root contributions are nonnegative.
Therefore

    v_p(C_(p+1))>=u,
    log C_(p+1)>=u log p,
    m>=[u log p-d log 2]/(p+1).                            (2)

This counts the norm in the original degree-d field K, not the degree-[L:Q] norm.
Summing valuations of its d factors is exactly the local norm accounting; it does not count a prime ideal twice.
Neither scalar return at every root nor exact order p+1 is assumed.
Different actual residue orders may all divide this common exponent.

Importantly, the hypothesis is that p is unramified in L.
The proof does not require p not dividing disc(P).
Reduction collisions caused by the power-basis index do not affect the product valuation proof.
If one additionally imposes p not dividing disc(P), all the preceding statements remain valid, but that stricter condition must not be silently added to a least-prime theorem excluding only field ramification.
No ramified prime of L is covered by (2) without a separate argument.

## 2. Automatic lifts and the Salem specialization

For any x in O_L with v_Q(x-1)=a>=1 and p unramified, expansion of x^p-1 at 1 gives

    v_Q(x^p-1)>=min(a+1,pa)>=a+1.

Here the intermediate binomial coefficients are divisible by p; possible cancellation only increases the valuation.
Induction on r>=0 applied to the selected u roots therefore proves

    v_p(C_((p+1)p^r))>=(r+1)u,
    m>=[(r+1)u log p-d log 2]/[(p+1)p^r].                 (3)

This is a lower bound for actual valuations, not an assertion of equality or a ceiling on exceptional initial depths.

For a Salem polynomial of degree d>=4 there is exactly one real expanding root and its inverse, with all other roots on the unit circle.
Thus u=d-2.
Suppose a class of such inputs has a common B>0 and, for each input, a prime p as in Section 1 satisfying

    p<=B d log p.                                         (4)

Then these inputs have the following explicit conditional uniform gap.
If p=2, take r=2 in (3), so n=12 and

    m>=(2d-6)log 2/12>=log 2/6.                           (5)

If p=3, take r=1, again n=12, and

    m>=[2(d-2)log 3-d log 2]/12
      >=log(3/2)/3.                                      (6)

For p>=5, take r=0 and use d-2>=d/2, p+1<=6p/5.
Put

    a_0=1/2-log 2/log 5>0.

Equations (2) and (4) give

    m>=a_0 d log p/(p+1)>=5a_0/(6B).                      (7)

Consequently (4), if separately proved with common B, gives

    m>=min{log 2/6, log(3/2)/3, 5a_0/(6B)}>0.             (8)

This implication includes every prime and every Salem degree d>=4.
It does not locate a prime satisfying (4).
For a general reciprocal input, the correct count is u, not d-2; u can be too small or zero.
No Salem reduction of the unrestricted G0001 contract is asserted.
The local proof needs no all-positive-power degree-preservation assumption, and is in particular compatible with that narrower core.

<a id="cycle-type-versus-inversion-matching"></a>
## 3. Cycle type alone does not supply the matching relation

The relation in (1) is a labelled relation involving the intrinsic inverse pairing of the roots.
Merely having cycles of length at most two only gives rho^(p^2)=rho modulo Q, hence the full-return exponent p^2-1.
It need not give rho^(p+1)=1 on the two-cycles.

A finite permutation diagnostic makes the distinction explicit.
For d=2s>=6 label the inverse pairs {x_i,x_i^(-1)}, 1<=i<=s.
Let c_0 fix pair 1 pointwise and invert each pair 2,...,s.
Let b fix pair 1 pointwise, exchange pairs 2 and 3 by sending x_2 to x_3 and x_2^(-1) to x_3^(-1), and invert pairs 4,...,s.
Both permutations have cycle type 1^2 2^(s-1).
But c_0 induces the identity on the set of pairs, whereas b induces a transposition.
They cannot be conjugate inside the inverse-pair-preserving permutation group, since the induced permutation of pairs respects conjugation.
The two cycles exchanging different pairs do not match a root with its inverse.

This is a finite-group diagnostic, not an assertion that every abstract pattern is realized by an actual near-one Salem polynomial.
It shows why a theorem specifying only the ordinary cycle type needs additional input before it supplies the hypothesis of Section 1.

For the same reason the natural Galois action on d>=4 reciprocal roots is contained in the inverse-pair-preserving group (C_2)^s semidirect S_s.
In particular it is not the full S_d in this natural action, and |G|<=(2^s)s!.
A theorem for natural full symmetric Galois groups cannot be transferred by replacing its degree with d.
An unrelated abstract symmetric-group realization would require its own field, action, class, and cost identification.

<a id="quartic-seventeen-partial-return"></a>
## 4. One actual hand-checked control

Use the already retained irreducible quartic Salem polynomial

    P_4(t)=t^4-t^3-t^2-t+1

from [L8](Yin_L_G0008_v1.md) and its earlier actual-family interfaces.
At p=17,

    P_4(t)=(t^2-13t+1)(t^2-5t+1) modulo 17,
    t^2-5t+1=(t-10)(t-12) modulo 17.                      (9)

Indeed the product has t^3 and t coefficients -18=-1 mod17, and t^2 coefficient 67=-1 mod17.
Also 10+12=5 mod17 and 10*12=1 mod17.
The first quadratic has discriminant 13^2-4=12 mod17.
The complete nonzero square set modulo17 is {1,2,4,8,9,13,15,16}; it does not contain12.
That quadratic is therefore irreducible and squarefree.
The second quadratic has two distinct roots.
The difference of the quadratics is -8t, so they have no common root, since their constant coefficients are one.
In particular p does not divide disc(P_4).

The two roots of the irreducible quadratic are interchanged by Frobenius, and their product is one.
Each has its 18th power equal to one.
The corresponding first-layer norm mass is at least 2 log17.
L74, or the same product argument, gives

    v_17(C_18)>=2,
    m(P_4)>=[2 log17-4 log2]/18=log(17/4)/9>0.             (10)

This is an actual partial-return certificate without needing the other two reduced roots to return.
It does not require asserting that the prime's global Frobenius class equals the complex-conjugation class.
The retained quartic has fixed measure above one; it is not a new family approaching one.
All arithmetic in (9)--(10) is the displayed hand check, not an executed prime scan.

<a id="matched-class-least-prime-cost"></a>
## 5. The complete least-prime cost remains unfilled

Write N_L=[L:Q] and D_L=|disc L|.
The adopted BS96 statement, under its stated ERH hypothesis, supplies an unramified prime in the precise class of c with

    p<=U=(4 log D_L+2.5N_L+5)^2.                          (11)

The local proof deliberately permits power-basis-index bad primes, so no additional exclusion of divisors of disc(P) is needed here.
The small primes are covered separately by (5)--(6).
For p>=5, x/log x is increasing, and (11) gives the safe cost bound

    p/(d log p)<=U/(d log U).                             (12)

But U>=(2.5d+5)^2.
The right side of (12), as a guaranteed upper-bound expression over this input range, has a lower envelope growing like d/log d.
It therefore does not supply a common B for (4).
This is a failure of the available upper-bound certificate, not a lower bound on the actual least matching prime.

The existing elementary height relation is

    log|disc K|<=log|disc P|<=d log d+(2d-2)m.              (13)

It is the retained L75/DK25 relation.
Neither disc K nor disc P may replace D_L in (11).
Likewise d may not replace N_L.
Small m has not here been shown to bound N_L/d or give the missing matching prime estimate.
The finite group bound N_L<=(2^s)s! still does not make (12) uniform.
Even the favorable hypothetical case L=K with bounded m leaves the standard square-log-discriminant prime bound at the wrong scale, as already explained in L75.

The bounded new source screen found Cho--Lemke Oliver--Zaman, arXiv:2512.24963v1.
In the following comparison assume c is nonidentity, as it is for every Salem input here.
Its Theorem2.1 applies to rational equivalence classes, which coincide with conjugacy classes for an involution: an order-two cyclic subgroup has a unique nonidentity generator.
The displayed unconditional exponent for this exact class is 1/2, so the source offers p bounded by a G- and epsilon-dependent constant times D_L^(1/2+epsilon).
This does not give (4).
Its Theorem2.3 can lower the exponent after additional Artin holomorphy hypotheses and subgroup/centralizer data; those inputs and uniform costs have not been established here.
Theorems1.2--1.3 for symmetric groups do not bypass Section 3's action restriction.
The exact statement and effectiveness scopes, version, retained PDF, and inspection limits belong to the separate source note.
If c=1, all roots are real and u=0; the local formulas remain valid with zero matching mass.
The relevant complete-splitting comparison is then the existing L75 mechanism, not the order-two discussion.

Compared with L75, the new local relation returns only a selected part of the roots and permits p+1 in place of the generic p^2-1 exponent for an involution.
It is not a prime-cost improvement over the old complete-splitting p-1 mechanism, whose available least-prime cost has the same unresolved degree problem.
It neither repeats L152's existence-only order floor nor provides new primitive excess: the certified mass here is actual local mass forced by the matching relation, with the missing prime coverage explicitly retained.

## 6. Resulting bounded selection

The mechanism is a valid conditional partial synchronization, with the actual control (10).
A new coverage input would have to bound the minimum p/(d log p) over the exact matching Frobenius class, or verify the matching on enough actual reduced roots without requesting that global class.
No inspected theorem supplies this uniformly on the sufficiently-near-one core.
Optimizing a generic Chebotarev constant or substituting an ordinary cycle-type theorem does not fill that missing input.
The present bounded source search is stopped; no new prime/order scan is selected.

G0001 remains unresolved.
The unrestricted reciprocal domain may have far fewer unit-circle conjugates than the Salem specialization, and no positive lower fraction u/d is assumed without proof.
When u=0, this matching mechanism's mass floor is zero even if its Frobenius class is available.
Proving the conditional Salem coverage alone would not establish the unrestricted G0001 contract.



The original review account is retained in [fixed R](../audits/reviews/Yin_R_G0059_v1.md#complete-independent-written-review-and-adoption), with its original inspected scope and relationship.
